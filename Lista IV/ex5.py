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

def calcular(palavra):
  for letra in palavra:
    if letra in 'python':
      return True
  return False


lista = []
for c in txt.split():
    if calcular(c) and len(c) > 4:
        lista.append(c)

print(len(lista))
