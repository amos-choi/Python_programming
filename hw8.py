def buy(d):
    print('[구입]')
    while True:
        name = input('상품명?: ')
        if name == '':
            break
        num = input('수량은?: ')
        d[f'{name}'] = num 
        print(f'장바구니에 {name} {num}개가 담겼습니다. \n')
    return False

def show(d):
    print(f'\n >>> 장바구니 보기: {d}')


def find(d):
    print('\n[검색]')
    search = input('장바구니에서 확인하고자 하는 상품은?')
    if search in d :
        search_num = d[search]
        print(f'{search}은(는) {search_num}개 담겨 있습니다')
    else:
         print(f'장바구니에 {search}은(는) 없습니다.')
    
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
           break
show(shopping_bag)
find(shopping_bag)  
