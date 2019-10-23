from random import randint

vetor1 = []
vetor2 = []
vetor3 = []

for c in range(0, 10):
    vetor1.append(randint(1, 100))
    vetor2.append(randint(1, 100))

for c in zip(vetor1, vetor2):
    vetor3.extend(list(c))

print(f'Vetor 1: {vetor1}')
print(f'Vetor 2: {vetor2}')
print(f'Vetor 3: {vetor3}')

#rever conceitos v3.extend(list(x))