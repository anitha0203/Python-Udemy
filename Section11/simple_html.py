from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>Sample HTML file</h1>
<p class='subtitle'>This is first paragraph</p>
<p>This is Second paragraph</p>
<ul>
<li>Anitha</li>
<li>Ani</li>
<li>Anu</li>
<li>Sri</li>
</ul>
</body
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

print(simple_soup.find('li').string)

print(simple_soup.find_all('li'))

items = simple_soup.find_all('li')
contents = [e.string for e in items]
print(contents)


para = simple_soup.find('p')
print(para.string)

para = simple_soup.find('p', {'class': 'subtitle'})
print(para.string)

para = simple_soup.find_all('p')
other = [p for p in para if 'subtitle' not in p.attrs.get('class')]
print(para)
