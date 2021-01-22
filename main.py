import re 

def top_3_words(text):
    rgx = r'\'{0,1}[a-zA-Z]+\'*[a-zA-Z]*'
    words = re.findall(rgx, text)
    frq = {}
    for word in words:
        frq.setdefault(word.lower(), 0)
        frq[word.lower()] += 1

    result = sorted(frq, key=lambda x: frq[x], reverse=True)
    
    return result[:3]
