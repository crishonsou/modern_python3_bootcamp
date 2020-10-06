import re

def parse_date(input):
    date_regex = re.compile(r'^(\d\d)[,/.](\d\d)[,/.](\d{4})$')
    date_match = date_regex.search(input)
    if date_match:
        return{
            'd': date_match.group(1),
            'm': date_match.group(2),
            'y': date_match.group(3)
            }
    return None


print(parse_date('01/22/1999'))
print(parse_date('12,04,2003'))
print(parse_date('12.11.2003'))
print(parse_date('12.11.200312'))




