def get_radius(prompt) :
    r = int(input(prompt))
    return r

def get_circle_area(radius) :
    circle_area_ = radius ** 2 * 3.14
    return circle_area_

result = get_radius("넓이를 구하고자 하는 원의 반지름은? :")
circle_area = get_circle_area(result)
print(f"반지름 {result}인 원의 넓이: 3.14 * {result} * {result} = {circle_area}")



