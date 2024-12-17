"""
Library for taking a list of KapeTargets and converting them to a human-readable 
report.
"""

from typing import Optional

from tabulate import tabulate

from fastlabel.kape.core import KapeTarget

def generate_markdown(targets: list[KapeTarget], header: Optional[str]) -> str:
    """
    Generate a simplified Markdown report of all available modules.
    
    There are three sections:
    - A user-defined header (optional)
    - A summary of all discovered target types
    - A breakdown of files discovered for each target type, with each target type
      being a separate header, and each file being a single bullet point.
    """
    
    output = ""
    
    if header:
        output += f"# Custom Information \n\n{header}\n\n"
        
    # Generate a summary of all discovered target types
    output += "# Summary\n\n"
    
    # Sort targets by name
    targets.sort(key=lambda x: x.name)
    
    headers = ["Target type", "File count"]
    table = []
    for target in targets:
        table.append([target.name, len(target.files)])
        
    output += tabulate(table, headers, tablefmt="github") + "\n\n"
    
    # Generate a breakdown of files discovered for each target type
    output += "# Details\n\n"
    
    for target in targets:
        output += f"## {target.name}\n\n"
        output += f"{len(target.files)} files found:\n\n"
        output += "\n".join([f"- {file.source}" for file in target.files]) + "\n\n"
        
    return output