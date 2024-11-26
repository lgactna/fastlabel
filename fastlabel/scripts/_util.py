import keyword
import re


def generate_docstring(comment: str | None, width: int = 76) -> str:
    """
    Break the comment into a multi-line docstring, capped at 80 characters
    per line (including 4 spaces of indentation). Preserves existing line breaks.
    """
    if not comment:
        return ""

    # Replace backslashes with forward slashes to avoid escape sequence issues
    comment = comment.replace("\\", "/")

    # comment = to_valid_pystring(comment)

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


def to_valid_identifier(s: str, remove_underscores: bool = False) -> str:
    # Remove leading and trailing whitespace
    s = s.strip()
    # Replace invalid characters with underscores
    s = re.sub(r"\W+|^(?=\d)", "_", s)

    # Remove underscores (for things like class definitions)
    if remove_underscores:
        s = s.replace("_", "")

    # If it's a reserved keyword, prepend an underscore
    if keyword.iskeyword(s):
        s = "_" + s
    # Ensure the identifier is valid
    if not s.isidentifier():
        s = "_" + s
    return s


def to_valid_pystring(s: str) -> str:
    """
    Convert a string to a valid Python string literal.
    """
    return s.translate(
        str.maketrans(
            {  # type: ignore[arg-type]
                # "-": r"\-",
                # "]": r"\]",
                "\\": r"\\",
                # "^": r"\^",
                # "$": r"\$",
                # "*": r"\*",
                # ".": r"\.",
            }
        )
    )
