"""
Generate models for the CASE library.

Code generated with Copilot using the o1-preview model.
"""

import keyword
import re
from collections import defaultdict
from graphlib import TopologicalSorter
from pathlib import Path
from textwrap import dedent
from typing import Any, Optional

from pydantic import BaseModel
from rdflib import RDF, RDFS, BNode, Graph, Literal, Namespace, URIRef

from fastlabel.scripts._util import generate_docstring

# Define standard namespaces
SH = Namespace("http://www.w3.org/ns/shacl#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDFS_NS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# Map XSD datatypes to Python types
DATATYPE_MAPPING = {
    XSD.string: "str",
    XSD.integer: "int",
    XSD.decimal: "float",
    XSD.boolean: "bool",
    XSD.dateTime: "AwareDatetime",  # Use 'datetime' if you handle date parsing
    XSD.nonNegativeInteger: "int",
    XSD.date: "str",
}

UNKNOWN_DATATYPE_VAL = "UNKNOWN.UNKNOWN"


def get_local_name(uri: Any, components: int = 1) -> str:
    """
    Returns a "local" name for a URI, typically the object of a `SubclassOf`
    predicate.

    For example, the URI https://ontology.unifiedcyberontology.org/uco/core/UcoInherentCharacterizationThing
    would return `core.UcoInherentCharacterizationThing`, if `components` is 2.
    It would then be up to you to write logic to determine if this is an external
    import or not.

    :param uri: The URI to get the local name of.
    :param components: The number of components to return.
    :return: The local name of the URI.
    """
    if isinstance(uri, URIRef):
        # Get the last two parts of the URI, which *should* return something like
        # `observable.ObservableObject` or whatever
        return ".".join(re.split("[#/]", str(uri))[-components:])
    return str(uri)


def get_artifacts_dir() -> Path:
    """
    Get a resolved path to `/case_artifacts`.
    """
    # Go up three directories from this source file
    return (Path(__file__).parents[2] / "case_artifacts").resolve()


def get_target_dir() -> Path:
    """
    Get a resolved path to "/fastlabel".
    """
    return (Path(__file__).parents[1]).resolve()


class Property(BaseModel):
    """
    A property in a SHACL graph.
    """

    # The name of the field itself.
    field_name: str

    # This is a non-annotated type, or a class name. It is *not* something like
    # `Optional[...]`; that's generated at runtime.
    python_type: str

    # Based on cardinality, is this required?
    is_required: bool
    # Based on cardinality, is this a list?
    is_list: bool

    # This will determine if `python_type` is considered an external import or not.
    # For example, if the type is `observable.ObservableObject`, and the namespace
    # is NOT `observable`, then it's an external import and will be typed as
    # `observable.ObservableObject`.
    #
    # However, if the namespace is `observable`, then it's an internal import and
    # will be typed as just `ObservableObject`.
    namespace: str

    @classmethod
    def from_property_shape(
        cls, prop_list: URIRef | BNode, namespace: str
    ) -> Optional["Property"]:
        """
        Create a Property instance from a SHACL property shape (sh:property).
        """
        path = g.value(prop_list, SH.path)
        if not path:
            return None

        field_name = get_local_name(path)

        # Handle datatype
        datatype = g.value(prop_list, SH.datatype)
        if datatype:
            # Check if a native mapping exists
            if datatype in DATATYPE_MAPPING:
                python_type = DATATYPE_MAPPING[datatype]
            else:
                # If not, use the URI
                python_type = get_local_name(datatype, 2)
        else:
            # Handle sh:class
            prop_class = g.value(prop_list, SH["class"])
            # print(prop_class)
            if prop_class:
                # Get the field name, up to two components, so we know what
                # namespace it's in
                python_type = get_local_name(prop_class, 2)
            else:
                # The datatype doesn't exist
                python_type = UNKNOWN_DATATYPE_VAL

        # Handle cardinality
        max_count = g.value(prop_list, SH.maxCount)
        min_count = g.value(prop_list, SH.minCount)
        is_required = False
        if min_count and int(min_count.toPython()) >= 1:
            is_required = True

        is_list = False
        if max_count and int(max_count.toPython()) != 1:
            is_list = True

        return cls(
            field_name=field_name,
            python_type=python_type,
            is_required=is_required,
            is_list=is_list,
            namespace=namespace,
        )

    def generate_type_annotation(self, containing_class: str) -> str:
        """
        Generate the actual annotation for this property.
        """
        # If the type is an external import, we need to use the fully qualified
        # name. Otherwise, we can just use the local name.
        python_type = self.python_type
        if self.namespace in self.python_type:
            # This is local
            python_type = self.python_type.replace(f"{self.namespace}.", "")

        # Special: If this is an XMLSchema import, prefix the second component
        # with `xsd_`.
        if self.python_type.startswith("XMLSchema."):
            python_type = f"XMLSchema.xsd_{self.python_type.split('.')[1]}"

        # If this field's type is equal to its containing Pydantic model, then we
        # must perform deferred evaluation of the type annotation. The field name
        # must be in quotes.
        #
        # Note this uses the qualified name, not the local name.
        if self.python_type == containing_class:
            python_type = f'"{python_type}"'

        if self.is_list:
            python_type = f"list[{python_type}]"
        else:
            if not self.is_required:
                python_type = f"Optional[{python_type}]"

        return python_type

    def to_pydantic_field(self, containing_class: str) -> str:
        """
        Convert this property to a Pydantic field definition.
        """
        # Build the field definition
        # TODO: Are there default values that need to be extracted?
        # TODO: Some of these fields get duplicated, which is not great...
        #       Probably the best way is to build an "object" that holds the
        #       field name, type, and default value... a Pydantic model that
        #       serializes to a field lol
        #
        #       In any case, this needs to be aware of the file it's currently
        #       in, so we know whether or not it's an external import or just
        #       a reference to another class in the same file

        # If the field name is a reserved keyword, append an underscore
        field_name = self.field_name
        if keyword.iskeyword(self.field_name):
            field_name += "_"

        # Alternatively, if the field name is exactly that of its corresponding
        # class, append an underscore
        # NOTE: this is hacky, a robust solution would require knowledge of all
        #       the types in use in a single class -- however, there is no place
        #       this is an issue except for "location" fields using the
        #       "location.Location" type
        if self.field_name in self.python_type:
            field_name += "_"

        result = f"    {field_name}: {self.generate_type_annotation(containing_class)}"

        # Decide on the default value
        if self.is_list:
            result += " = []"
        elif not self.is_required:
            result += " = None"

        return result + "\n"


class UCOModel(BaseModel):
    """
    Represents a single UCO model.
    """

    # Qualified class name, e.g. `analysis.AnalyticResultFacet`
    class_name: str

    # Qualified superclass name, e.g. `core.Facet`, unless `BaseModel`
    superclass: str = "BaseModel"

    # The rdfs:comment for this class, if any
    comment: Optional[str] = None

    # List of properties for this class
    properties: list[Property] = []

    # This will determine if the superclass causes an import statement
    # or not. That is, if the superclass is in the same file, we don't
    # need to import it. If it's in another file, we do.
    #
    # In general, this should be the name of the source turtle file (excluding
    # the .ttl extension).
    namespace: str

    @classmethod
    def from_owl_class(cls, owl_class: Any, g: Graph, namespace: str) -> "UCOModel":
        # Get the class name, fully qualified
        class_name = get_local_name(owl_class, 2)

        # Get superclass (if any)
        superclasses = [
            get_local_name(o, 2) for o in g.objects(owl_class, RDFS.subClassOf)
        ]
        superclass = superclasses[0] if superclasses else "BaseModel"

        # Get rdfs:comment for docstring
        comment = ""
        for o in g.objects(owl_class, RDFS.comment):
            if isinstance(o, Literal):
                comment = str(o)
                break

        # Add properties, excluding those that have a unknown datatype
        properties = []
        for prop_list in g.objects(owl_class, SH.property):
            prop = Property.from_property_shape(prop_list, namespace)
            if prop and prop.python_type != UNKNOWN_DATATYPE_VAL:
                properties.append(prop)

        return UCOModel(
            class_name=class_name,
            superclass=superclass,
            comment=comment,
            properties=properties,
            namespace=namespace,
        )

    def to_pydantic_model(self) -> str:
        """
        Convert this UCO model to a Pydantic model.

        Note that you must handle any external imports separately.
        """
        result = ""

        # Convert qualified name to local name
        class_name = self.class_name.split(".")[-1]

        # If the superclass is in the same namespace, drop the namespace part
        superclass = self.superclass
        if self.namespace in self.superclass:
            superclass = self.superclass.replace(f"{self.namespace}.", "")

        class_def = f"class {class_name}({superclass}):"
        docstring = generate_docstring(self.comment)
        result += class_def + "\n" + docstring + "\n"

        # Add properties
        for prop in self.properties:
            result += prop.to_pydantic_field(self.class_name)

        # If this has no properties, add a pass statement
        if not self.properties:
            result += "    pass\n"

        return result

    def get_dependencies(self) -> set[str]:
        """
        Get the dependencies of this UCO model.
        """
        dependencies = {prop.python_type for prop in self.properties}
        dependencies.add(self.superclass)

        # Do not allow cyclic dependencies
        dependencies.discard(self.class_name)
        return dependencies


class VocabularyModel(BaseModel):
    # Qualified class name, e.g. `vocabulary.TriggerTypeVocab`
    class_name: str

    # The rdfs:comment for this enum, if any
    comment: Optional[str] = None

    # List of members for this enum, a 2-tuple of member name and value
    members: list[tuple[str, str]] = []

    # This will determine if the superclass causes an import statement
    # or not. That is, if the superclass is in the same file, we don't
    # need to import it. If it's in another file, we do.
    #
    # In general, this should be the name of the source turtle file (excluding
    # the .ttl extension).
    namespace: str

    @classmethod
    def from_datatype(
        cls, datatype: Any, g: Graph, namespace: str
    ) -> "VocabularyModel":
        enum_name = get_local_name(datatype)

        # Get rdfs:comment for docstring
        comment = None
        for c in g.objects(datatype, RDFS_NS.comment):
            if isinstance(c, Literal):
                comment = str(c)
                break

        # Get the owl:equivalentClass and owl:oneOf list
        members = []
        eq_class = g.value(subject=datatype, predicate=OWL.equivalentClass)
        if eq_class:
            one_of = g.value(subject=eq_class, predicate=OWL.oneOf)
            if one_of:
                # Extract items from the RDF list
                items = list(g.items(one_of))
                for item in items:
                    # Get the string value of each item
                    value = str(item)
                    # Create a valid Python identifier for the enum member
                    member_name = re.sub(r"\W|^(?=\d)", "_", value).upper()
                    members.append((member_name, value))

        return VocabularyModel(
            class_name=enum_name,
            comment=comment,
            members=members,
            namespace=namespace,
        )

    def to_enum(self) -> str:
        """
        Convert this datatype to a string enumeration.
        """
        result = ""

        # If this has no members, return an empty string
        if not self.members:
            return result

        # Convert qualified name to local name
        class_name = self.class_name.split(".")[-1]

        class_def = f"class {class_name}(str, Enum):"
        docstring = generate_docstring(self.comment)
        result += class_def + "\n" + docstring

        # Add members
        for member_name, value in self.members:
            result += f"    {member_name} = '{value}'\n"

        return result + "\n"


def generate_import_list(dependency_graph: dict[str, set[str]], namespace: str) -> str:
    """
    Generate a list of import statements based on the dependency graph.
    """
    # Get all dependencies
    dependencies = set()
    for deps in dependency_graph.values():
        dependencies.update(deps)

    # Don't include types that aren't part of CASE/UCO
    dependencies -= {"str", "int", "float", "bool", "AwareDatetime"}

    # Handle special cases
    for dep in ("Any", "Optional", "List"):
        if dep in dependencies:
            dependencies.remove(dep)

    # Remove any dependencies that are in the same namespace
    dependencies = {dep for dep in dependencies if namespace not in dep}

    # Group imports by namespace (the first component of the class name)
    grouped_dependencies = defaultdict(set)
    for dep in dependencies:
        namespace, name = dep.split(".")
        grouped_dependencies[namespace].add(name)

    # Generate import statements
    # NOTE: we used to import individual objects from each namespace, now we just
    # import the whole namespace -- this is why the code is like this
    imports = ""

    # TODO: right now, there's no consideration whether or not something is in
    #       CASE or UCO -- this is a problem becase we need to know which library
    #       to import from. the workaround is to just manually fix what's broken.
    if grouped_dependencies:
        imports += f"from fastlabel.uco import ({', '.join(sorted(grouped_dependencies.keys()))})\n"
    # for namespace, _ in grouped_dependencies.items():
    #     imports += f"from fastlabel.case import {namespace}\n"

    # Always import these, which can be removed if needed
    imports += "from typing import Any, Optional\n"
    imports += "from enum import Enum\n"
    imports += "from pydantic import AwareDatetime\n"

    return imports


def generate_classes_from_graph(
    g: Graph, namespace: str, library: str
) -> tuple[str, str]:
    """
    Generate Python classes from a SHACL graph.

    The return value is a 2-tuple, where the first element is the import list
    and the second element is the generated Python code for each class.
    """
    # Get all classes that are sh:NodeShape and owl:Class
    classes = set()
    for s in g.subjects(RDF.type, SH.NodeShape):
        if (s, RDF.type, OWL.Class) in g:
            classes.add(s)

    output = ""

    # Process each class

    # Maintain a mapping of class names to UCOModel instances, as well as
    # a dependency graph of class names to their dependent class names.
    names_to_classes: dict[str, UCOModel] = {}
    dependency_graph: dict[str, set[str]] = {}

    for cls in classes:
        model = UCOModel.from_owl_class(cls, g, namespace)

        names_to_classes[model.class_name] = model
        dependency_graph[model.class_name] = model.get_dependencies()

    # Sort the keys of dependency_graph to ensure the class order is deterministic.
    dependency_graph = {k: dependency_graph[k] for k in sorted(dependency_graph)}

    # Topologically sort the classes according to their dependencies.
    # If a dependency cannot be found in this file, it must be external.
    class_order = tuple(TopologicalSorter(dependency_graph).static_order())

    for class_name in class_order:
        if class_name not in names_to_classes:
            continue

        model = names_to_classes[class_name]
        output += model.to_pydantic_model() + "\n"

    imports = generate_import_list(dependency_graph, namespace)

    return imports, output


def generate_enums_from_datatypes(graph: Graph) -> str:
    enum_definitions = ""
    # Find all nodes of type rdfs:Datatype
    for datatype in graph.subjects(RDF.type, RDFS_NS.Datatype):
        model = VocabularyModel.from_datatype(datatype, graph, namespace)
        enum_definitions += model.to_enum()
    return enum_definitions


if __name__ == "__main__":
    # Find all folders in the /case_artifacts directory

    case_artifacts_dir = get_artifacts_dir()

    # Get all directories/libraries in case_artifacts_dir
    directories = [d for d in case_artifacts_dir.iterdir() if d.is_dir()]

    # Recursively search for all .ttl files in each directory
    for directory in directories:
        library = directory.stem

        for artifact_file in directory.glob("*/*.ttl"):
            # The name of the generated Python file. The absolute import path should
            # be `fastlabel.<library>.<namespace>`
            namespace = artifact_file.stem
            target_file = get_target_dir() / library / f"{namespace}.py"

            print(
                f"Processing {artifact_file.relative_to(get_artifacts_dir())} ->"
                f" {'fastlabel' / target_file.relative_to(get_target_dir())}"
            )

            # Load the RDF graph for this file
            g = Graph()
            g.parse(artifact_file, format="turtle")

            vocabularies = generate_enums_from_datatypes(g)

            imports, class_defs = generate_classes_from_graph(g, namespace, library)
            docstring = dedent(
                f'''
                """
                Auto-generated classes from the SHACL graph in {artifact_file.name}.
                
                This file was generated using the `case_models.py` script.
                """
                '''  # noqa: W293
            )

            class_file = (
                docstring + "\n" + imports + "\n" + vocabularies + "\n" + class_defs
            )

            # Write file based on the artifact file name

            with open(target_file, "wt+") as fp:
                fp.write(class_file)
