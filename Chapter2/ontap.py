pm25_values = [12.5, 18.2, 35.1, 28.4, 41.8, 20.6, 30.2]


# Decorator
def log_call(func):
    def wrapper(*args, **kwargs):
        print("Đang gọi hàm:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


# Câu 1
@log_call
def calculate_mean(values):
    """Tính giá trị trung bình của danh sách."""
    return sum(values) / len(values)


# Tạo biến mean
mean = calculate_mean(pm25_values)

print("Giá trị trung bình:", round(mean, 2))


# Câu 2
pm25_over_25 = list(
    filter(lambda x: x > 25, pm25_values)
)

print("PM2.5 > 25:", pm25_over_25)


# Câu 3 - Closure
def make_threshold_checker(threshold):
    def checker(value):
        return value > threshold

    return checker


checker = make_threshold_checker(25)

result = list(filter(checker, pm25_values))

print("Dùng closure:", result)


# Câu 4 - Higher-order function
def transform_values(values, func):
    return [func(value) for value in values]


max_value = max(pm25_values)

normalize = lambda x: x / max_value

normalized_values = transform_values(
    pm25_values,
    normalize
)

print("Giá trị sau chuẩn hóa:")
print([round(x, 3) for x in normalized_values])