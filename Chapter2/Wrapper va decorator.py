# Bài 16. Decorator ghi log
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Function: {func.__name__}")
        print(f"[LOG] args: {args}")
        print(f"[LOG] kwargs: {kwargs}")

        result = func(*args, **kwargs)

        print(f"[LOG] result: {result}")

        return result

    return wrapper

@log_call
def calculate_mean(values):
    """Tính giá trị trung bình của danh sách số."""
    return sum(values) / len(values)

# Test
result = calculate_mean([10, 20, 30])

print("Kết quả cuối cùng:", result)

#Bài 17. Decorator đo thời gian
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        elapsed_time = end - start

        print(
            f"[TIMER] Function: {func.__name__}"
        )
        print(
            f"[TIMER] Execution time: {elapsed_time:.6f} seconds"
        )
        return result

    return wrapper

@timer
def sum_of_squares(n):
    """Tính tổng bình phương từ 0 đến n - 1."""
    return sum(x ** 2 for x in range(n))


# Test với n = 100000
result1 = sum_of_squares(100000)
print("Kết quả:", result1)

print()

# Test với n = 1000000
result2 = sum_of_squares(1000000)
print("Kết quả:", result2)

#Bài 18. Decorator kiểm tra dữ liệu rỗng 
from functools import wraps


def require_non_empty(func):
    @wraps(func)
    def wrapper(values, *args, **kwargs):

        if not isinstance(values, (list, tuple)):
            raise TypeError("Dữ liệu phải là list hoặc tuple")

        if len(values) == 0:
            raise ValueError("Dữ liệu đầu vào không được rỗng")

        return func(values, *args, **kwargs)

    return wrapper


@require_non_empty
def calculate_mean(values):
    """Tính giá trị trung bình."""
    return sum(values) / len(values)


@require_non_empty
def calculate_max(values):
    """Tìm giá trị lớn nhất."""
    return max(values)


@require_non_empty
def calculate_min(values):
    """Tìm giá trị nhỏ nhất."""
    return min(values)


# Test dữ liệu hợp lệ
values = [10, 20, 30, 40, 50]

print("Mean:", calculate_mean(values))
print("Max:", calculate_max(values))
print("Min:", calculate_min(values))