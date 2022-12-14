(number_words, m) = map(int, input().split())   

final_spell = ''   
dict_translator = {}         #dictionary which acts like a translator

for i in range(m):
    (magic, normal) = map(str, input().split())
    dict_translator[magic] = normal        

in_spell = input()        #input of spell

l1 = in_spell.split()     #list of the input spell, split into words



for i in l1:                                          #checking length of words and replacing whenever needed
    if len(dict_translator[i]) < len(i):
        final_spell += dict_translator[i] + ' '
    elif len(dict_translator[i]) >= len(i):
        final_spell += i + ' '

print(final_spell)
