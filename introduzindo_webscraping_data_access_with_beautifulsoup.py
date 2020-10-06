from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class="special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
#el = soup.select(".special")[0]
#print(el.get_text())
#for el in soup.select(".special"):
#    print(el.get_text())
#for el in soup.select(".special"):
#    print(el.name)
#    print(el.attrs['class'])

attr1 = soup.find("h3").attrs["data-example"]
print(attr1)
attr2 = soup.find("h3")["data-example"]
print(attr2)
attr3 = soup.find("div")["id"]
print(attr3)

   

