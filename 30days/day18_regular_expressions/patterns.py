# Writing RegExp Patterns

import re

regex_pattern = r'apple'

txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '

matches = re.findall(regex_pattern, txt)
matches = re.findall(regex_pattern, txt, re.I)

print(matches)


# Escape character(\) in RegEx
regex_pattern = r'\d'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# One or more times(+)
regex_pattern = r'\d+'
print(re.findall(regex_pattern, txt))

# Period(.)
regex_pattern = r'[a].'
txt = '''Apple and banana are fruits'''
print(re.findall(regex_pattern, txt, re.I))

regex_pattern = r'[a].+'
print(re.findall(regex_pattern, txt, re.I))

# Zero or more times(*)
regex_pattern = r'[a].*'
print(re.findall(regex_pattern, txt))

# Quantifier in RegEx
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
print(re.findall(regex_pattern, txt))

# Starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'
print(re.findall(regex_pattern, txt))
