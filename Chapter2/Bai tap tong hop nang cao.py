# Bài 19. Xây dựng bộ phân tích dữ liệu quan trắc 
from functools import wraps
# 1. Hàm extract_field

def extract_field(records, field):
    """
    Trích xuất một trường dữ liệu từ danh sách records.

    Parameters
    ----------
    records : list
        Danh sách các dictionary.
    field : str
        Tên trường cần lấy.

    Returns
    -------
    list
        Danh sách các giá trị của trường được yêu cầu.
    """

    return list(map(lambda record: record[field], records))

# 2. Closure phân loại PM2.5

def make_pm25_classifier(threshold):
    """
    Tạo một hàm phân loại PM2.5 theo ngưỡng.

    Parameters
    ----------
    threshold : int hoặc float
        Ngưỡng PM2.5.

    Returns
    -------
    function
        Hàm trả về "High" nếu PM2.5 lớn hơn threshold,
        ngược lại trả về "Normal".
    """

    def classifier(value):
        if value > threshold:
            return "High"
        return "Normal"

    return classifier


# 3. Decorator log_call

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"[LOG] Function: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] result: {result}")

        return result

    return wrapper

# 4. Hàm build_report
@log_call
def build_report(measurements, classifier):
    """
    Xây dựng báo cáo phân tích dữ liệu quan trắc.

    Parameters
    ----------
    measurements : list
        Danh sách dữ liệu quan trắc.
    classifier : function
        Hàm dùng để phân loại giá trị PM2.5.

    Returns
    -------
    dict
        Báo cáo gồm số lượng trạm, PM2.5 trung bình,
        PM2.5 lớn nhất, các trạm vượt ngưỡng
        và nhãn phân loại của từng trạm.
    """

    # Lấy danh sách PM2.5
    pm25_values = extract_field(measurements, "pm25")

    # Tính số lượng trạm
    station_count = len(measurements)

    # Tính PM2.5 trung bình
    average_pm25 = sum(pm25_values) / len(pm25_values)

    # Tìm PM2.5 lớn nhất
    max_pm25 = max(pm25_values)

    # Lọc các trạm có PM2.5 > 35
    high_stations = list(
        filter(
            lambda record: record["pm25"] > 35,
            measurements
        )
    )

    # Lấy tên các trạm vượt ngưỡng
    stations_over_threshold = list(
        map(
            lambda record: record["station"],
            high_stations
        )
    )

    # Phân loại từng trạm
    classifications = {
        record["station"]: classifier(record["pm25"])
        for record in measurements
    }
    # Tạo báo cáo
    report = {
        "station_count": station_count,
        "average_pm25": average_pm25,
        "max_pm25": max_pm25,
        "stations_over_threshold": stations_over_threshold,
        "classifications": classifications
    }

    return report

# 5. Dữ liệu
measurements = [
    {"station": "A01", "pm25": 12.5, "temp": 28.2},
    {"station": "A02", "pm25": 37.4, "temp": 31.0},
    {"station": "A03", "pm25": 28.6, "temp": 30.4},
    {"station": "A04", "pm25": 45.2, "temp": 32.1},
    {"station": "A05", "pm25": 18.9, "temp": 29.5}
]

# 6. Tạo classifier với threshold = 35
classifier = make_pm25_classifier(35)

# 7. Tạo báo cáo
report = build_report(measurements, classifier)

# 8. In kết quả
print("\nBÁO CÁO")
print("Số lượng trạm:", report["station_count"])
print("PM2.5 trung bình:", report["average_pm25"])
print("PM2.5 lớn nhất:", report["max_pm25"])
print(
    "Trạm vượt ngưỡng:",
    report["stations_over_threshold"]
)
print(
    "Phân loại:",
    report["classifications"]
)


# ==========================================
# Bài 20. Xây dựng pipeline làm sạch dữ liệu    
from functools import wraps

# ==========================================
# 1. Decorator log_step
# ==========================================

def log_step(func):
    @wraps(func)
    def wrapper(values, *args, **kwargs):

        before_count = len(values)

        result = func(values, *args, **kwargs)

        after_count = len(result)

        print(
            f"[STEP] {func.__name__}: "
            f"{before_count} -> {after_count} phần tử"
        )

        return result

    return wrapper

# ==========================================
# 2. Loại bỏ dữ liệu không phải số
# ==========================================

@log_step
def remove_non_numeric(values):
    """
    Loại bỏ các phần tử không phải số.

    Parameters
    ----------
    values : list
        Danh sách dữ liệu đầu vào.

    Returns
    -------
    list
        Danh sách chỉ chứa các giá trị số.
    """

    return list(
        filter(
            lambda x: isinstance(x, (int, float)),
            values
        )
    )

# ==========================================
# 3. Loại bỏ số âm
# ==========================================

@log_step
def remove_negative(values):
    """
    Loại bỏ các giá trị âm.

    Parameters
    ----------
    values : list
        Danh sách số.

    Returns
    -------
    list
        Danh sách chỉ chứa các giá trị >= 0.
    """

    return list(
        filter(
            lambda x: x >= 0,
            values
        )
    )

# ==========================================
# 4. Giới hạn giá trị lớn nhất
# ==========================================

@log_step
def clip_upper_bound(values, upper=500):
    """
    Giới hạn giá trị tối đa của dữ liệu.

    Parameters
    ----------
    values : list
        Danh sách dữ liệu.
    upper : int hoặc float
        Giá trị giới hạn trên.

    Returns
    -------
    list
        Danh sách sau khi giới hạn giá trị.
    """

    return [
        min(x, upper)
        for x in values
    ]

# ==========================================
# 5. Làm tròn dữ liệu
# ==========================================

@log_step
def round_values(values, digits=1):
    """
    Làm tròn các giá trị trong danh sách.

    Parameters
    ----------
    values : list
        Danh sách số.
    digits : int
        Số chữ số sau dấu thập phân.

    Returns
    -------
    list
        Danh sách sau khi làm tròn.
    """

    return [
        round(x, digits)
        for x in values
    ]

# ==========================================
# 6. Higher-order function run_pipeline
# ==========================================

def run_pipeline(values, functions):
    """
    Thực hiện lần lượt các hàm xử lý lên dữ liệu.

    Parameters
    ----------
    values : list
        Danh sách dữ liệu ban đầu.
    functions : list
        Danh sách các hàm xử lý.

    Returns
    -------
    list
        Dữ liệu sau khi hoàn thành pipeline.
    """

    result = values.copy()

    for func in functions:
        result = func(result)

    return result

# ==========================================
# 7. Dữ liệu thô
# ==========================================

raw_pm25 = [
    12.5,
    -999,
    None,
    18.0,
    "NA",
    35.2,
    -1,
    42.6,
    20.1
]

# ==========================================
# 8. Xây dựng pipeline
# ==========================================

pipeline = [
    remove_non_numeric,
    remove_negative,
    clip_upper_bound,
    round_values
]

# ==========================================
# 9. Chạy pipeline
# ==========================================

clean_data = run_pipeline(
    raw_pm25,
    pipeline
)

# ==========================================
# 10. Thống kê cơ bản
# ==========================================

count = len(clean_data)
total = sum(clean_data)
mean = total / count
minimum = min(clean_data)
maximum = max(clean_data)


# ==========================================
# 11. In kết quả
# ==========================================

print("\nDỮ LIỆU SAU KHI LÀM SẠCH:")
print(clean_data)

print("\nTHỐNG KÊ:")
print("Count:", count)
print("Sum:", total)
print("Mean:", mean)
print("Min:", minimum)
print("Max:", maximum)