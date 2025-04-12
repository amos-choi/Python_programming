def read_single_digit(input_num):
    if input_num == 0:
        return '영'
    elif input_num == 1:
        return '일'
    elif input_num == 2:
        return '이'
    elif input_num == 3:
        return '삼'
    elif input_num == 4:
        return '사'
    elif input_num == 5:
        return '오'
    elif input_num == 6:
        return '육'
    elif input_num == 7:
        return '칠'
    elif input_num == 8:
        return '팔'
    else:
        return '구'


def read_number(number):
    first_num = int(number[2])
    second_num = int(number[1])
    third_num = int(number[0])
    first_num = read_single_digit(first_num)
    second_num = read_single_digit(second_num)
    third_num = read_single_digit(third_num)
    print(third_num, second_num, first_num)
                    
number = input('세 자리 정수 입력: ')
read_number(number)
