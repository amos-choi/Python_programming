def display_multiplication_table(n) :
    i = 1
    while i <= 9 :
        print(f'{n} x {i} = {n * i:2d}\t', end= '')
        print(f'{n+1} x {i} = {(n+1) * i:2d}\t', end = '')
        print(f'{n+2} x {i} = {(n+2) * i:2d}\t', end = '')
        print(f'{n+3} x {i} = {(n+3) * i:2d}')
        i += 1

n = 2
while n <= 9 :
    display_multiplication_table(n)
    print('')
    n = n+4
