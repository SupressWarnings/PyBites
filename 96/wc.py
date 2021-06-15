import re


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    file = open(file_).read()
    lines = len(file.splitlines())
    words = len(list(filter(None, re.split("[ \\\\/:|.\\\n]", file))))
    chars = len(file)
    return "\t".join((str(lines), str(words), str(chars), str(file_)))


if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))
