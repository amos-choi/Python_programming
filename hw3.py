def get_fixed_price(rate_) :
        if rate_ >= 100:    #100넘는 수를 넣어보니까, 바로 오류를 일으켜서,, 추가
                return
        a_price = int(input('A 상품의 할인된 가격은?'))
        b_price = int(input('B 상품의 할인된 가격은?'))
        a_real_price = a_price * 100 / (100 - rate_)
        b_real_price = b_price * 100 / (100 - rate_)
        print('A 상품의 정가는 ', a_real_price, ' 원')
        print('B 상품의 정가는 ', b_real_price, ' 원')

rate = float(input('할인율은?'))
get_fixed_price(rate)
