import re

#def censor(input):
#    pattern = re.compile(r'([frack])[a-z]+', re.I|re.IGNORECASE)
#    result = pattern.sub('CENSORED', input)
#    return result

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub('CENSORED', input)


print(censor('Frack you'))
print(censor('I hope you fracking die'))
print(censor('You fracking Frack'))



