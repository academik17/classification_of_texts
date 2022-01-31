from nltk import sent_tokenize, word_tokenize, pos_tag


print('происходит анализ обучающей выборки')
def nouns(s):
    k = 0
    for i in range(len(s)):
        if s[i][1] == 'NN' or s[i][1] == 'NNP' or s[i][1] == 'NNS' or s[i][1] == 'NNPS':
            k += 1 
    return k     

def adjective(s):
    k = 0
    for i in range(len(s)):
        if s[i][1] == 'JJ' or s[i][1] == 'JJR' or s[i][1] == 'JJS':
            k += 1 
    return k  

def verbs(s):
    k = 0
    for i in range(len(s)):
        if s[i][1] == 'VB' or s[i][1] == 'VBG' or s[i][1] == 'VBD' or s[i][1] == 'VBZ' or s[i][1] == 'VBN' or s[i][1] == 'VBP':
            k += 1 
    return k

def pronauns(s):
    k = 0
    for i in range(len(s)):
        if s[i][1] == 'PRP' or s[i][1] == 'PRP$':
            k += 1 
    return k

mas = [[0] * 4 for i in range(4)]
for i in range(4):
    for j in range(3):  
        f = open('C:/Users/davyd/Desktop/RO/readme.txt')
        adr=f.readlines()
        f.close()
        adr1 = adr[i*3+j]
        adr2 = adr1[:(len(adr1)-1)]
        print(adr2)
        f1 = open(adr2)
        text=f1.read()
        f1.close()
        text_word = word_tokenize(text) 
        l = len(text_word)
        pos_text = pos_tag(text_word)
        mas[i][0] += nouns(pos_text)/l 
        mas[i][1] += adjective(pos_text)/l 
        mas[i][2] += verbs(pos_text)/l 
        mas[i][3] += pronauns(pos_text)/l 
for i in range(4):
    for j in range(3): 
        mas[i][j] = mas[i][j]/3
#print(mas)

def mult(a,b):
    k = 0
    for i in range(len(a)):
        k +=a[i]*b[i]
    return k

def minus(a,b):
    for i in range(len(a)):
        a[i] = a[i] - b[i]
    return a

def plus(a,b):
    for i in range(len(a)):
        a[i] = a[i] + b[i]
    return a


v = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def uslovie(b):
    b = True
    for i in range(4):
        for j in range(4):
            if i == j:
                b = b and (mult(mas[i],v[j])>0)
            else:
                b = b and (mult(mas[i],v[j])<=0)
    return b


b = True

while uslovie(b) == False:
    for i in range(4):
        for j in range(4):
            if (i == j) and (mult(mas[i],v[j])<=0):
                v[j] = plus(mas[i], v[i])
            if (i != j) and (mult(mas[i],v[j])>=0):
                v[j] = minus(v[j],mas[i])
print(v)

def proverka(a, b):
    c = [0]*4
    for i in range(4):
        c[i] = mult(a,b[i])
    max = c[0]
    k = 0
    for i in range(4):
        if max < c[i]:
            max = c[i]
            k = i
    if k == 0:
        return 'Художественный стиль'
    if k == 1:
        return 'Научный стиль'
    if k == 2:
        return 'Публицистический стиль'
    if k == 3:
        return 'Деловой стиль'


print('Ведите адрес анализируемого отрывка')
adr = input()
test =[0, 0, 0, 0]
f1 = open(adr)
text=f1.read()
f1.close()
text_word = word_tokenize(text) 
l = len(text_word)
pos_text = pos_tag(text_word)
test[0] += nouns(pos_text)/l 
test[1] += adjective(pos_text)/l 
test[2] += verbs(pos_text)/l 
test[3] += pronauns(pos_text)/l 

print('результат')
print(proverka(test,v))
