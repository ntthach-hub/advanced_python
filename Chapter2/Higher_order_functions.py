#Bài 9. Hàm áp dụng nhiều lần 
def apply_n_times(func, value, n):
    """
    Áp dụng một hàm lên giá trị n lần.

    Parameters
    ----------
    func : function
        Hàm được áp dụng.
    value : any
        Giá trị ban đầu.
    n : int
        Số lần áp dụng hàm.

    Returns
    -------
    any
        Giá trị sau khi áp dụng hàm n lần.

    Raises
    ------
    ValueError
        Nếu n < 0.
    """
    if n < 0:
        raise ValueError("n không được nhỏ hơn 0")
    result = value

    for _ in range(n):
        result = func(result)
    return result
#test
result = apply_n_times(lambda x: x + 2, 1, 4)

print(result)

# Bài 10. Data transformation pipeline 
def run_pipeline(values, functions):
    """
    Áp dụng lần lượt các hàm lên toàn bộ danh sách.

    Parameters
    ----------
    values : list
        Danh sách giá trị ban đầu.
    functions : list
        Danh sách các hàm được áp dụng theo thứ tự.

    Returns
    -------
    list
        Danh sách kết quả sau khi chạy qua toàn bộ pipeline.
    """
values = [3, 6, 9]

functions = [
    lambda x: x * 2,
    lambda x: x + 1,
    lambda x: round(x / 3, 2)
]

result = run_pipeline(values, functions)

print("Final:", result)
print("Original:", values)

#Bài 11. Chọn quy tắc phân loại 
def classify_values(values,classfier):
    """
    Phân loại từng giá trị trong danh sách.

    Parameters
    ----------
    values : list
        Danh sách các giá trị cần phân loại.
    classifier : function
        Hàm nhận một giá trị và trả về nhãn.

    Returns
    -------
    dict
        Dictionary có dạng {value: label}.
    """
    result = {}
    for value in values:
        result[value] = classfier(value)
    result
def classify_temperature(value):
    if value >= 35:
        return "Hot"
    elif value >= 25:
        return "Warm"
    else:
        return "Cool"

def classify_pm25(value):
    if value < 12:
        return "Good"
    elif value <= 35:
        return "Moderate"
    else:
        return "High"

pm25_values = [10, 20, 35, 40]

result = classify_values(
    pm25_values,
    classify_pm25
)

print(result)

# Bài 12. Bộ lọc tùy biến 
def custom_filter(values, predicate):
    """
    Lọc các giá trị trong danh sách dựa trên một điều kiện.

    Parameters
    ----------
    values : list
        Danh sách các giá trị cần lọc.
    predicate : function
        Hàm điều kiện nhận một giá trị và trả về True hoặc False.

    Returns
    -------
    list
        Danh sách các giá trị thỏa mãn điều kiện.
    """

    result = []

    for value in values:
        if predicate(value):
            result.append(value)

    return result


# =========================
# Test 1: Lọc số chẵn
# =========================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = custom_filter(
    numbers,
    lambda x: x % 2 == 0
)

print("Số chẵn:", even_numbers)


# =========================
# Test 2: Lọc số lớn hơn 25
# =========================

numbers = [10, 20, 25, 30, 35, 40]

greater_than_25 = custom_filter(
    numbers,
    lambda x: x > 25
)

print("Số lớn hơn 25:", greater_than_25)


# =========================
# Test 3: Lọc chuỗi có độ dài > 5
# =========================

words = [
    "Python",
    "Data",
    "Engineering",
    "SQL",
    "Programming"
]

long_words = custom_filter(
    words,
    lambda x: len(x) > 5
)

print("Chuỗi có độ dài > 5:", long_words)