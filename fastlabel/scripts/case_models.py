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
    for cls in classes:
        class_name = get_local_name(cls)
        # Get superclass (if any)
        superclasses = [get_local_name(o) for o in g.objects(cls, RDFS.subClassOf)]
        superclass = superclasses[0] if superclasses else "BaseModel"

        # Get rdfs:comment for docstring
        comment = None
        for o in g.objects(cls, RDFS.comment):
            if isinstance(o, Literal):
                comment = str(o)
                break

        # Start building the class definition
        class_def = f"class {class_name}({superclass}):\n"
        if comment:
            # Split the comment into lines of maximum 80 characters
            words = comment.split()
            lines = []
            current_line = ""
            for word in words:
                if len(current_line) + len(word) + 1 > 80:
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
            class_def += docstring

        # Get properties
        for prop_list in g.objects(cls, SH.property):
            # For each sh:property
            path = g.value(prop_list, SH.path)
            if not path:
                continue
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
                python_type = f"List[{python_type}]"
            else:
                if not is_required:
                    python_type = f"Optional[{python_type}]"

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
            default_value = "..." if is_required else "None"
            class_def += f"    {field_name}: {python_type} = {default_value}\n"

        # This is a single class definition
        output += class_def + "\n"
    
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
