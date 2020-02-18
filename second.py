import re
'''
if re.search("inform", "We need to inform him with the infoem latestest information."):
    print("Theire is inform")

allinform = re.findall("inform","We need to inform him with the inform latestest information.")

for i in allinform:
    print(i)


str = "We need to inform him with the infoem latestest information."

for i in re.finditer("inform", str):
    loc = i.span()
    print(loc)

str = "sat, hat, mat, bat, pat, zat"

#find all words given regx pattern.
allstr = re.findall("[A-Z,h-z]at", str)

for i in allstr:
    print(i)

# Replace lettter using sub 
regex = re.compile("[m]at")
cat = regex.sub('cat', str)
print(cat)

'''

randomstr = '''
Today is sunny day.
We can except a match.
between india and aus.
'''

print(randomstr)
regex = re.compile("\n")
randomstr = regex.sub(" ", randomstr)
print(randomstr)
