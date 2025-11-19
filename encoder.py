import sys

encoding_dict = {
    " ": "%20",
    "!": "%21",
    "\"": "%22",
    "#": "%23",
    "$": "%24",
    "%": "%25",
    "&": "%26",
    "'": "%27",
    "(": "%28",
    ")": "%29",
    "*": "%2A",
    "+": "%2B",
    ",": "%2C",
    "-": "%2D",
    ".": "%2E",
    "/": "%2F",
    ":": "%3A",
    ";": "%3B",
    "<": "%3C",
    "=": "%3D",
    ">": "%3E",
    "?": "%3F",
    "@": "%40",
    "[": "%5B",
    "\\": "%5C",
    "]": "%5D",
    "^": "%5E",
    "_": "%5F",
    "`": "%60",
    "{": "%7B",
    "|": "%7C",
    "}": "%7D",
    "~": "%7E"
}

def encode(input: str) -> str:
    encoded_chars = []
    for char in input:
        encoded_chars.append(encoding_dict.get(char, char))
    return "".join(encoded_chars)

if __name__ == "__main__":
    input_string = sys.argv[1]
    encoded_string = encode(input_string)
    print("Encoded string: ")
    print(encoded_string)