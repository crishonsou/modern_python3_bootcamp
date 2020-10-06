#import regex module
import re

#define our phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# search a tring with our regex
res = pattern.search('Call me at 415 555-4242!')
res_all = pattern.findall('Call me at 415 565-4232 or 310 255-9377!')


print(res)
print(res.group())
print(res_all)
    
