import re

#def extract_phone(input):
#    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
#    match = phone_regex.search(input)
#    if match:
#        return match.group()
#    return None

#def extract_all_phones(input):
#    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
#    return phone_regex.findall(input)


#def validating_phone(input):
#    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
#    match = phone_regex.search(input)
#    if match:
#        return True
#    return False

def validating_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False

    
#print(extract_phone("My phone is 432 585-9876"))
#print(extract_phone("432 685-9886 is my number"))
#print(extract_phone("432 785-9896"))
#print(extract_phone("My phone is 432 658-65970"))


#print(extract_all_phones("My phone is 432 785-9876 or 555 555-5555"))
#print(extract_all_phones("432 658-65970 or 432 585-9876 and 432 685-9886"))
#print(extract_all_phones("432 658-65"))
#print(extract_all_phones("432 658-65970"))


print(validating_phone("432 658-6538"))
print(validating_phone("My phone is 432 658-6538"))
print(validating_phone("432 658-6538 is my phone"))




