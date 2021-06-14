INDENTS = 4


def print_hanging_indents(poem):
    lines = poem.split("\n")
    for i in range(1, len(lines)):
        if lines[i - 1] != "" and lines[i] != "":
            lines[i] = f"    {lines[i]}"
    lines
    print("\n".join(list(filter("".__ne__, lines))))
    return
