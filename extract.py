import re

with open('bibliography.bib', 'r') as f:
    original = f.read()

with open('extractKeys.txt', 'r') as f:
    keys = f.readlines()

regex = '@.*('
for akey in keys:
    akey = akey.rstrip()
    regex = regex + akey+ '|'
regex = regex + 'somebullshitkey)[^@]*'

print regex
res = re.finditer(regex, original)
matches = [ares.group() for ares in res]

print len(matches) ,' where found'
with open('extract.bib', 'w') as f:
    f.write(''.join(matches))
