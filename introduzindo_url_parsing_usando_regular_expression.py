import re

# regex para avaliar a url inteira:
# 'https?://www\.[A-za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*'

# regex para avaliar o domínio principal:
# 'https?://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})[-a-zA-Z0-9@:%_\+.~#?&//=]*'

# regex para avaliar se o site é http ou https:
# '(https?)://www\.[A-za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*'

def is_valid_url(input):
    url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
    match_url = url_regex.search(input)
    if match_url:
        print(f'Protocol: {match_url.group(1)}')
        print(f'Domain: {match_url.group(2)}')
        print(f'Complement: {match_url.group(3)}')
    else:
        print('It is not a valid URL')



is_valid_url('http://www.youtube.com/videos')
is_valid_url('http://www.google.com/search/?q=tacos')
is_valid_url('http://@avanzo.netzoada.ubr/$$$/queisso')
is_valid_url('https://www.my-website.com/bio?data=blah&dog=yes')

    
