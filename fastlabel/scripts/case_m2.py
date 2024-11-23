"""
Generate models for the CASE library.

Code generated with Copilot using the o1-preview model.
"""

import re
from pathlib import Path
from textwrap import dedent

from rdflib import RDF, RDFS, Graph, Literal, Namespace, URIRef

# Define namespaces
SH = Namespace("http://www.w3.org/ns/shacl#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDFS_NS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# UCO namespaces
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


# Helper function to get the local name of a URI
# TODO: need to return the library it would be in, e.g. uco.core.UcoInherentCharacterizationThing
def get_local_name(uri: str) -> str:
    if isinstance(uri, URIRef):
        return re.split("[#/]", str(uri))[-1]
    return str(uri)


def get_artifacts_dir() -> Path:
    """
    Get a resolved path to `/grr_artifacts`.
    """
    # Go up three directories from this source file
    return (Path(__file__).parents[2] / "case_artifacts").resolve()


def get_target_dir() -> Path:
    """
    Get a resolved path to `/fastlabel/grr`.
    """
    return (Path(__file__).parents[1] / "grr").resolve()


def generate_classes_from_graph(g: Graph) -> str:
    # Stores the generated class definitions
    class_definitions = ""

    # Stores the Enum definitions
    enum_definitions = ""

    # Keep track of vocabularies for Enums
    vocabularies = {}

    # Get all classes that are sh:NodeShape and owl:Class
    classes = set()
    for s in g.subjects(RDF.type, SH.NodeShape):
        if (s, RDF.type, OWL.Class) in g:
            classes.add(s)

    # First, process vocabularies to create Enums
    for s in g.subjects(RDF.type, RDFS_NS.Datatype):
        vocab_name = get_local_name(s)
        members = []
        for value in g.objects(subject=s, predicate=RDF.type):
            members.append(str(value))
        if members:
            vocabularies[vocab_name] = members

    # Generate Enum classes for vocabularies
    for vocab_name, members in vocabularies.items():
        enum_definitions += f"class {vocab_name}(str, Enum):\n"
        for member in members:
            enum_member_name = re.sub(r'\W|^(?=\d)', '_', member).upper()
            enum_definitions += f"    {enum_member_name} = '{member}'\n"
        enum_definitions += "\n"

    # Process each class
    for cls in classes:
        class_name = get_local_name(cls)
        # Get superclass (if any)
        superclasses = [get_local_name(o) for o in g.objects(cls, RDFS.subClassOf)]
        superclass = superclasses[0] if superclasses else 'BaseModel'

        # Get rdfs:comment for docstring
        comment = None
        for o in g.objects(cls, RDFS_NS.comment):
            if isinstance(o, Literal):
                comment = str(o)
                break

        # Start building the class definition
        class_def = f"class {class_name}({superclass}):\n"
        if comment:
            # Indent the docstring correctly
            docstring = '    """' + comment + '"""\n'
            class_def += docstring

        # Get properties
        for prop_list in g.objects(cls, SH.property):
            # For each sh:property
            path = g.value(prop_list, SH.path)
            if not path:
                continue
            field_name = get_local_name(path)

            # Initialize variables
            python_types = []
            validation_messages = []

            # Handle sh:or constraints
            or_list = g.value(prop_list, SH['or'])
            if or_list:
                # If there is an sh:or constraint
                for or_constraint in g.items(or_list):
                    python_type = process_constraint(g, or_constraint, vocabularies)
                    python_types.append(python_type)
            else:
                # Handle single constraint
                python_type = process_constraint(g, prop_list, vocabularies)
                python_types.append(python_type)

            # Handle cardinality
            max_count = g.value(prop_list, SH.maxCount)
            min_count = g.value(prop_list, SH.minCount)
            is_required = False
            if min_count and int(min_count.toPython()) >= 1:
                is_required = True

            is_list = False
            if max_count and int(max_count.toPython()) != 1:
                is_list = True

            # Build the field type
            if is_list:
                if len(python_types) > 1:
                    union_type = f"Union[{', '.join(python_types)}]"
                    python_type = f"List[{union_type}]"
                else:
                    python_type = f"List[{python_types[0]}]"
            else:
                if len(python_types) > 1:
                    python_type = f"Union[{', '.join(python_types)}]"
                else:
                    python_type = python_types[0]
                if not is_required:
                    python_type = f"Optional[{python_type}]"

            # Extract validation messages
            messages = [str(msg) for msg in g.objects(prop_list, SH.message)]
            if messages:
                validation_messages.extend(messages)

            # Build the field definition
            default_value = "..." if is_required else "None"
            field_args = []
            if validation_messages:
                field_args.append(f'description="{"; ".join(validation_messages)}"')
            field_definition = f"{field_name}: {python_type} = Field({default_value}"
            if field_args:
                field_definition += ", " + ", ".join(field_args)
            field_definition += ")"
            class_def += f"    {field_definition}\n"

        class_definitions += class_def + "\n"

    # Combine enum definitions and class definitions
    output = enum_definitions + "\n" + class_definitions
    return output

def process_constraint(g: Graph, constraint_node, vocabularies):
    # Handle datatype
    datatype = g.value(constraint_node, SH.datatype)
    if datatype:
        datatype_str = str(datatype)
        python_type = DATATYPE_MAPPING.get(datatype_str)
        if not python_type:
            # Check if datatype is a vocabulary
            vocab_name = get_local_name(datatype)
            if vocab_name in vocabularies:
                python_type = vocab_name
            else:
                python_type = 'str'
    else:
        # Handle sh:class
        prop_class = g.value(constraint_node, SH['class'])
        if prop_class:
            python_type = get_local_name(prop_class)
        else:
            python_type = 'Any'

    return python_type

if __name__ == "__main__":
    for artifact_file in get_artifacts_dir().glob("*/*.ttl"):
        print(f"Validating {artifact_file}")

        # Load the RDF graph
        g = Graph()
        g.parse(artifact_file, format="turtle")

        class_file = generate_classes_from_graph(g)
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
        target_file = get_target_dir() / f"{artifact_file.stem}.py"
        with open(target_file, "wt+") as fp:
            fp.write(class_file)
