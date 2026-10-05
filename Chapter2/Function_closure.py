#Bài 13. Hàm kiểm tra ngưỡng
def make_threshold_checker(threshold):
    """
    Tạo một hàm kiểm tra giá trị có đạt ngưỡng hay không.

    Parameters
    ----------
    threshold : int hoặc float
        Giá trị ngưỡng.
    inclusive : bool
        Nếu True, kiểm tra value >= threshold.
        Nếu False, kiểm tra value > threshold.

    Returns
    -------
    function
        Hàm checker dùng để kiểm tra một giá trị.
    """
    def checker(value, inclusive=True):
        if inclusive:
            return value >= threshold
        else:
            return value > threshold
    return checker
#test
check_35 = make_threshold_checker(35)

print(check_35(35))
print(check_35(40))
print(check_35(30))

print(check_35(35, inclusive=False))
print(check_35(40, inclusive=False))

#Bài 14. Hàm chuyển đổi đơn vị có cấu hình 
def make_unit_converter(scale, offset):
    """
    Tạo một hàm chuyển đổi đơn vị.

    Parameters
    ----------
    scale : int hoặc float
        Hệ số nhân.
    offset : int hoặc float
        Giá trị cộng thêm.

    Returns
    -------
    function
        Hàm chuyển đổi theo công thức:
        y = x * scale + offset
    """

    def converter(x):
        return x * scale + offset

    return converter
c_to_f = make_unit_converter(9 / 5, 32)

print(c_to_f(0))
print(c_to_f(25))
print(c_to_f(100))

# Bài 15. Bộ đếm sự kiện
def create_counter():
    """
    Tạo một bộ đếm sử dụng closure.

    Returns
    -------
    function
        Hàm counter có thể tăng giá trị đếm.
    """

    count = 0

    def counter(amount=1):
        nonlocal count

        count += amount

        return count

    return counter
# test ex 15
counter = create_counter()

print(counter())
print(counter(3))
print(counter())