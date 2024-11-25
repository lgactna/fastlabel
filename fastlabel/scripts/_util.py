def generate_docstring(comment: str | None, width: int = 76) -> str:
    """
    Break the comment into a multi-line docstring, capped at 80 characters
    per line (including 4 spaces of indentation). Preserves existing line breaks.
    """
    if not comment:
        return ""

    # Replace backslashes with forward slashes to avoid escape sequence issues
    comment = comment.replace("\\", "/")

    lines = []
    paragraphs = comment.split("\n\n")  # Split on double line breaks
    for para in paragraphs:
        para = para.replace("\n", " ")  # Replace single line breaks with space
        words = para.split()
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
        # Add an empty line to separate paragraphs
        lines.append("")
    # Remove any extra blank lines at the end
    while lines and lines[-1] == "":
        lines.pop()

    # Indent the docstring correctly
    docstring = '    """\n'
    for line in lines:
        if line == "":
            docstring += "\n"
        else:
            docstring += f"    {line}\n"
    docstring += '    """\n'
    return docstring
