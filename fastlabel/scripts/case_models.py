"""
Generate models for the CASE library.

Code generated with Copilot using the o1-preview model.
"""

import re
from pathlib import Path
from textwrap import dedent
from typing import Any, Optional

from pydantic import BaseModel
from rdflib import RDF, RDFS, Graph, Literal, Namespace, URIRef

# Define namespaces
SH = Namespace("http://www.w3.org/ns/shacl#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDFS_NS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# TODO: UCO namespaces
OBSERVABLE = Namespace("http://example.org/observable#")
CORE = Namespace("http://example.org/core#")

# Map XSD datatypes to Python types
DATATYPE_MAPPING = {
    XSD.string: "str",
    XSD.integer: "int",
    XSD.decimal: "float",
    XSD.boolean: "bool",
    XSD.dateTime: "str",  # Use 'datetime' if you handle date parsing
    XSD.nonNegativeInteger: "int",
    XSD.date: "str",
}


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
    Get a resolved path to `/grr_artifacts`.
    """
    # Go up three directories from this source file
    return (Path(__file__).parents[2] / "case_artifacts").resolve()


def get_target_dir() -> Path:
    """
    Get a resolved path to `/fastlabel/case`.
    """
    return (Path(__file__).parents[1] / "case").resolve()


class Property(BaseModel):
    """
    A property in a SHACL graph.
    """
    
    field_name: str
    python_type: str
    is_required: bool
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
    def from_property_shape(cls, prop_list, namespace: str) -> Optional["Property"]:
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
            python_type = DATATYPE_MAPPING.get(datatype, "str")
        else:
            # Handle sh:class
            prop_class = g.value(prop_list, SH["class"])
            if prop_class:
                python_type = get_local_name(prop_class)
            else:
                python_type = "Any"

        # Handle cardinality
        max_count = g.value(prop_list, SH.maxCount)
        min_count = g.value(prop_list, SH.minCount)
        is_required = False
        if min_count and int(min_count.toPython()) >= 1:
            is_required = True

        is_list = False
        if max_count and int(max_count.toPython()) != 1:
            is_list = True

        if is_list:
            python_type = f"list[{python_type}]"
        else:
            if not is_required:
                python_type = f"Optional[{python_type}]"
                
        return cls(
            field_name=field_name, 
            python_type=python_type, 
            is_required=is_required, 
            is_list=is_list,
            namespace=namespace
        )        
        
    def to_pydantic_field(self) -> str:
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
        
        result = f"    {self.field_name}: {self.python_type}"
        
        if not self.is_required:
            result += " = None"
        
        return result + "\n"

class UCOModel(BaseModel):
    """
    Represents a single UCO model.
    """
    class_name: str
    superclass: str = "BaseModel"
    comment: Optional[str] = None
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
        # Get the class name
        class_name = get_local_name(owl_class)
                
        # Get superclass (if any)
        superclasses = [get_local_name(o, 2) for o in g.objects(owl_class, RDFS.subClassOf)]
        superclass = superclasses[0] if superclasses else "BaseModel"

        # Get rdfs:comment for docstring
        comment = ""
        for o in g.objects(owl_class, RDFS.comment):
            if isinstance(o, Literal):
                comment = str(o)
                break
            
        # Add properties
        properties = []
        for prop_list in g.objects(owl_class, SH.property):
            prop = Property.from_property_shape(prop_list, namespace)
            if prop:
                properties.append(prop)
           
        return UCOModel(
            class_name=class_name,
            superclass=superclass,
            comment=comment,
            properties=properties,
            namespace=namespace
        )
    
    def generate_docstring(self, width: int = 76) -> str:
        """
        Break the comment into a multi-line docstring, capped at 80 characters 
        per line (including 4 spaces of indentation).
        """
        if not self.comment:
            return ""
        
        words = self.comment.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 > width:
                lines.append(current_line)
                current_line = word
            else:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
        if current_line:
            lines.append(current_line)

        # Indent the docstring correctly
        docstring = '    """\n'
        for line in lines:
            docstring += f"    {line}\n"
        docstring += '    """\n'
        return docstring
    
    def to_pydantic_model(self) -> str:
        """
        Convert this UCO model to a Pydantic model.
        
        Note that you must handle any external imports separately.
        """
        result = ""
        
        class_def = f"class {self.class_name}({self.superclass}):"
        docstring = self.generate_docstring()
        result += class_def + "\n" + docstring + "\n"
        
        # Add properties
        for prop in self.properties:
            result += prop.to_pydantic_field()
        
        return result

def generate_classes_from_graph(g: Graph, namespace: str) -> str:
    """
    Generate Python classes from a SHACL graph.
    """
    # Get all classes that are sh:NodeShape and owl:Class
    classes = set()
    for s in g.subjects(RDF.type, SH.NodeShape):
        if (s, RDF.type, OWL.Class) in g:
            classes.add(s)

    output = ""

    # Process each class
    # TODO: maintain dictionary of classes to parent classes, then topologically
    # sort them to determine the order of output
    for cls in classes:
        # TODO: extract namespace
        model = UCOModel.from_owl_class(cls, g, namespace)

        # This is a single class definition
        output += model.to_pydantic_model() + "\n"
    
    # TODO: We have to figure out a valid import order, because the parent class
    #       of some classes are declared later down in the file. Python doesn't do
    #       forward declarations, so we may need to do some kind of topological sort
    #
    #       That is, keep track of all class relationships (which classes are 
    #       dependent on what?), topologically sort them, then write them out in
    #       that order. See:
    #       https://docs.python.org/3/library/graphlib.html
    return output


if __name__ == "__main__":
    for artifact_file in get_artifacts_dir().glob("*/*.ttl"):
        print(f"Validating {artifact_file}")
        
        # The name of the generated Python file. The absolute import path should 
        # be `fastlabel.case.<namespace>`
        namespace = artifact_file.stem

        # Load the RDF graph
        g = Graph()
        g.parse(artifact_file, format="turtle")

        class_file = generate_classes_from_graph(g, namespace)
        docstring = dedent(
            f'''
            """
            Auto-generated classes from the SHACL graph in {artifact_file.name}.
            
            This file was generated using the `case_models.py` script.
            """
            '''  # noqa: W293
        )

        # TODO: Figure out imports based on the inheritance tree, check if the
        # class declarations exist in this file and if they don't, assume they're
        # in the referenced file of the same name
        class_file = docstring + "\n" + class_file

        # Write file based on the artifact file name
        target_file = get_target_dir() / f"{namespace}.py"
        with open(target_file, "wt+") as fp:
            fp.write(class_file)
