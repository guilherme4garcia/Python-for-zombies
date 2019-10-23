txt = '''The Python Software Foundation and the global
   Python community  welcome  and  encourage participation
   by everyone.  Our  community is  based  on mutual respect,
   tolerance, and encouragement, and we are working to help each
   other live up to  these  principles.  We  want our  community
   to  be  more  diverse: whoever you  are,  and whatever  your
   background, we welcome  you.'''.lower()

import string

for x in string.punctuation:
  txt = txt.replace(x, ' ')

lista = []
for y in txt.split():
    if y[0] in 'python' or y[-1] in 'python':
        lista.append(y)

print(lista)