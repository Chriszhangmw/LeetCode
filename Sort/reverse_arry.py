









input_arry = ['p','e','r','f','e','c','t',' ','m','a','k','e','s',' ','p','r','a','c','t','i','c','e']


def reverse_sentence(arry):
    pareant = []
    words = []
    sym_indexs = get_sym(arry)
    print(sym_indexs)
    for index in sym_indexs:
        index = int(index)
        if index not in pareant and len(pareant)>0:
            temp = arry[pareant[-1]+1:index]
        else:
            temp = arry[:index]
        pareant.append(index)

        words.append(temp)
    words.append(arry[sym_indexs[-1]+1:])
    temp = words[2]
    words[2] = words[0]
    words[0] = temp
    sentence = ''
    for word in words:
        word = ''.join(word)
        sentence +=word + ' '
    print(sentence)





    print(words)



def get_sym(arry):
    res = []
    for i in range(len(arry)):
        if arry[i] == ' ':
            res.append(i)
    return res

reverse_sentence(input_arry)





