def generate_docstring(comment: str, width: int = 76) -> str:
    """
    Break the comment into a multi-line docstring, capped at 80 characters
    per line (including 4 spaces of indentation).
    """
    if not comment:
        return ""

    words = comment.split()
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
