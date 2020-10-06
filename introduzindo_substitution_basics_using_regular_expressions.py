import re

def basic_substitution(input):
    pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
    pattern_sub = pattern.sub("\g<1> \g<2>", input)
    return pattern_sub

text = ('Last night Mrs. Daisy and Mr. White murdered Mr. Chow')

print(basic_substitution(text))
