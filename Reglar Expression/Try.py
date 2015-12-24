import re
pat=r'\w\d{9}'
string='?wera123A10029876532413123?'
match = re.search(pat,string)
print(match.group())