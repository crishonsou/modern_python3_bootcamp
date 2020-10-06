import re

def parse_bytes(input):
    bytes_regex = re.compile(r'\b[0|1]{8}\b')
    return bytes_regex.findall(input)


print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is: 10101010 11110000"))
print(parse_bytes("asdsa"))
