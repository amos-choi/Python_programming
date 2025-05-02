d = {}
print('[구입]')
while True:
    name = input('상품명?: ')
    if name == '':
        break
    num = input('수량은?: ')
    d[f'{name}'] = num 
    print(f'장바구니에 {name} {num}개가 담겼습니다. \n')

print(f'\n >>> 장바구니 보기: {d}')


print('\n[검색]')
search = input('장바구니에서 확인하고자 하는 상품은?')
if search in d :
    search_num = d[search]
else:
    search_num = 0
    
print(f'{search}은(는) {search_num}개 담겨 있습니다')
