import requests

url = "http://www.google.com"
response = requests.get(url)
print(f'Your request to {url} returns status code {response.status_code}')

#res_ok = response.ok
#res_headers = response.headers
#res_text = response.text
#print(response)
#print(res_ok)
#print(res_headers)
#print(res_text)
