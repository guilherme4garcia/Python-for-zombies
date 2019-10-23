paisA = 80000
paisB = 200000

count = 0
while paisA < paisB:
    A = paisA * 0.03
    B = paisB * 0.015
    paisA = paisA + A
    paisB = paisB + B
    count = count + 1

print(f'O país A ultrapassa o país B em {count} anos')

