"""
Generate models for the CASE library.

Code generated with Copilot using the o1-preview model.
"""
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, URIRef, Literal
import re

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
    XSD.string: 'str',
    XSD.integer: 'int',
    XSD.decimal: 'float',
    XSD.boolean: 'bool',
    XSD.dateTime: 'str',  # Use 'datetime' if you handle date parsing
    XSD.nonNegativeInteger: 'int',
    XSD.date: 'str',
}

# Helper function to get the local name of a URI
def get_local_name(uri):
    if isinstance(uri, URIRef):
        return re.split('[#/]', str(uri))[-1]
    return str(uri)

def get_artifacts_dir() -> Path:
    """
    Get a resolved path to `/grr_artifacts`.
    """
    # Go up three directories from this source file
    return (Path(__file__).parents[2] / "case_artifacts").resolve()

if __name__ == "__main__":
    for artifact_file in get_artifacts_dir().glob("*/*.ttl"):
        print(f"Validating {artifact_file}")
        
        # Load the RDF graph
        g = Graph()
        g.parse(artifact_file, format="turtle")
        
        # Get all classes that are sh:NodeShape and owl:Class
        classes = set()
        for s in g.subjects(RDF.type, SH.NodeShape):
            if (s, RDF.type, OWL.Class) in g:
                classes.add(s)

        # Process each class
        for cls in classes:
            class_name = get_local_name(cls)
            # Get superclass (if any)
            superclasses = [get_local_name(o) for o in g.objects(cls, RDFS.subClassOf)]
            superclass = superclasses[0] if superclasses else 'BaseModel'
            
            # Get rdfs:comment for docstring
            comment = None
            for o in g.objects(cls, RDFS.comment):
                if isinstance(o, Literal):
                    comment = str(o)
                    break

            # Start building the class definition
            class_def = f"class {class_name}({superclass}):\n"
            if comment:
                # Split the comment into lines of maximum 88 characters
                words = comment.split()
                lines = []
                current_line = ""
                for word in words:
                    if len(current_line) + len(word) + 1 > 88:
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
                    python_type = DATATYPE_MAPPING.get(datatype, 'str')
                else:
                    # Handle sh:class
                    prop_class = g.value(prop_list, SH['class'])
                    if prop_class:
                        python_type = get_local_name(prop_class)
                    else:
                        python_type = 'Any'
            
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
                default_value = '...' if is_required else 'None'
                class_def += f"    {field_name}: {python_type} = {default_value}\n"

            print(class_def)