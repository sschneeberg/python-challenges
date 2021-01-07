# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(str):
    strArray = []
    for s in str: 
        strArray.append(s.lower())
    strArray.sort()
    return strArray

print(alphabetize('hello'))
print(alphabetize('abDGsE'))