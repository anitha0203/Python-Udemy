import re

email = 'anitha@gmail.com'
expression = '[a-z]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]

domain = f'{matches[1]}.{matches[2]}'

print(name)
print(domain)
 