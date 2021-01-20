PUNCTUATION = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'


def top_3_words(text):
    dict_of_words = dict()

    for index, value in enumerate(text):
        if value in PUNCTUATION:
            text = text.replace(value, ' ')

    list_of_words = text.split()

    for i in list_of_words:
        pu = [j for j in i for i in list_of_words if (j == "'") or (j == '"')]
        if len(pu) == len(i):
            while i in list_of_words:
                list_of_words.remove(i)

    print(list_of_words)
    for i in list_of_words:
        dict_of_words[i.lower()] = text.split().count(i)

    result = sorted(dict_of_words, key=dict_of_words.get, reverse=True)[:3]
    return result


print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e ''"))
