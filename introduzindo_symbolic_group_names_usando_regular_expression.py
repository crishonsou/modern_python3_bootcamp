import re

# regex para separar grupos
# ^(Mr\.|Mrs\.|Ms\.|Mdme\.) ([A-Za-z]+) ([A-Za-z]+)$

def parse_name(input):
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input)
    if matches:
        print(matches.group(0))
        print(matches.group('first'))
        print(matches.group('last'))



parse_name("Mrs. Tilda Swinton")
parse_name("Mdme. Margareth Taetcher")


