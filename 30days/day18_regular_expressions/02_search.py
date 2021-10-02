import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# search
match = re.search('first', txt, re.I)
print(match)

# findall
match = re.findall('language', txt, re.I)
print(match)

match = re.findall('language|first', txt, re.I)
print(match)

# Replacing a Substring
print(re.sub('Python|python', 'JavaScript', txt, re.I))
print(re.sub('[Pp]ython', 'JavaScript', txt, re.I))

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

print(re.sub('%', '', txt))

# Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n', txt)) # ['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']

