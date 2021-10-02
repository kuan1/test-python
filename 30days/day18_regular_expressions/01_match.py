import re

txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match)
print(match.span())
start,end=match.span()
print(start, end)
print(txt[start:end])

# None
match = re.match('I love to teach english', txt, re.I)
