words = ('tomba','dengoso','eletroquimica','ema','borrifar',
'cruzado','multiplicar','etario','esconder','registradora')
vowel = ( 'a', 'e', 'i', 'o', 'u')

# for c in range (0, len(words)):
#     for i in range (0,len(words[c])):
#         print(words[])
#             # print(vowel[i] in words[i])

var = words[0]
for i in words:
    print(f'\nA palavra {i} contém as vogais: ', end='' )
    for c in i:
        if c in 'aeiou':
            print(c, end=' ')
