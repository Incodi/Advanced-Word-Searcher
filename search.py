#max for first
word_size = 99

prefixes = [ # put in lowercase
]
suffixes = [
]

contains = [
]

bad_prefixes = [ # put in lowercase
]

bad_suffixes = [

]

bad_contains = [
    
]

collected_vowels = 'aeiouyáéóâêûîôöüèìòãå'

def searchByContain(data, size):
    res = []
    for word in data:
        lower = word.lower()

        # candp
        if (
            len(lower) <= size 
            and not 
            (any(lower.startswith(badprefix) for badprefix in bad_prefixes) 
            or any(lower.endswith(badsuffix) for badsuffix in bad_suffixes)
            or any(lower.__contains__(badcontain) for badcontain in bad_contains)) 
            and
            ((any(lower.startswith(prefix) for prefix in prefixes) 
            or any(lower.endswith(suffix) for suffix in suffixes)
            or any(lower.__contains__(contain) for contain in contains)))
            ):
            res.append(word)
        
    with open("searchresults.txt", "w") as s:
        s.write("\n".join(res))
     
def searchBySize(data, size, oneIfLessThan): # search size only
    res = []
    for word in data:
        # candp
        if oneIfLessThan:
            if (len(word) <= size):
                res.append(word)
        else:
            if (len(word) >= size):
                res.append(word)
        
    with open("searchresults.txt", "w") as s:
        s.write("\n".join(res))

def searchNoVowels(data): # search for words with no vowels only
    res = []
    for word in data:
        # candp
        if not any(vowel in word[:3].lower() for vowel in collected_vowels):
            res.append(word)
        
    with open("searchresults.txt", "w") as s:
        s.write("\n".join(res))
    
def searchByVowelCount(data, vowels): # search for words with no vowels
    res = []
    for word in data:
        # candp
        count = sum(word.lower().count(vowel) for vowel in collected_vowels)
        if count == vowels:
            res.append(word)
        
    with open("searchresults.txt", "w") as s:
        s.write("\n".join(res))

def searchDigits(data): # search for words with digits
    res = []
    for word in data:
        # candp
        if any(num in word.lower() for num in '1234567890'):
            res.append(word)
        
    with open("searchresults.txt", "w") as s:
        s.write("\n".join(res))

def searchPunc(data): # search for words with punctuation
    res = []
    for word in data:
        # candp
        if any(sym in word.lower() for sym in """²»!@#$%^&*()_+-=—"~-`"""):
            res.append(word)
        
    with open("searchresults.txt", "w") as s:
        s.write("\n".join(res))

def getLastSy(word):
    syllables = sy.syllables(word)
    
    if not syllables:
        return False
    
    return syllables[-1]

with open("text.txt", "r") as c1:
    c = c1.read()

c = c.split("\n")
#againstCurrentCriteria(c)
#searchByContain(c, word_size)
#searchBySize(c, 20, 0)
#searchNoVowels(c)
#searchByVowelCount(c, 2)
#searchDigits(c)
#searchPunc(c)

