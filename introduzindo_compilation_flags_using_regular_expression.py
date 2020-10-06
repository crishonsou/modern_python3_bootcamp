import re

def compile_flag(input):
    flag_regex = re.compile(r"""
            ^([a-z0-9_\.-]+) #first part of e-mail
            @                #single @ sign
            ([0-9a-z\.-]+)   #email provider
            \.               #single period
            ([a-z\.]{2,6})$  #ccom, org, net, etc
            """, re.VERBOSE | re.X | re.IGNORECASE)
    match_flag = flag_regex.search(input)
    if match_flag:
        return match_flag.group()
    return (f'{input} has wrong format')



print(compile_flag('dudu.bananinha@gmail.com'))
print(compile_flag('fora.biruleibe@gmail.com'))
print(compile_flag('Fora.Biruleibe@gmail.com'))
print(compile_flag('@Fora.Biruleibe@gmail.commm'))
print(compile_flag('@ Fora.Biruleibe@gmail.commm'))




