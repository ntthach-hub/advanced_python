# nhom 1: Docstring va ham
# bai 1 Bài 1. Hàm tính tổng và trung bình
def summarize(values):
    """
    Tóm tắt các giá trị số trong danh sách.

    Parameters
    ----------
    values : list
        Danh sách các giá trị số.

    Returns
    -------
    dict
        Dictionary gồm:
        - count: số lượng phần tử
        - sum: tổng các phần tử
        - mean: giá trị trung bình
        - min: giá trị nhỏ nhất
        - max: giá trị lớn nhất

    Raises
    ------
    ValueError
        Nếu danh sách values rỗng.
    """
    if not values:
        raise ValueError("Danh sách không được rỗng")
    total = sum(values)

    return {
        "count": len(values),
        "sum": total,
        "mean": total/len(values),
        "min": min(values),
        "max": max(values)
    }
print(summarize([1, 2, 3, 4]))
print(summarize([1.5, 2.5, 3.0]))

# bai 2 Phân loại chất lượng không khí 
def classify_pm25(value):
    """
    Phân loại chất lượng không khí dựa trên giá trị PM2.5.

    Parameters
    ----------
    value: int hoac float
        Gia tri PM2.5 can duoc phan loai.
    
    Returns
    -------
    str
        Good neu PM2.5 < 12
        Moderate neu 12<= PM2.5 <= 35
        High neu PM2.5 > 35.
    Raise
    -----
    TypeError
        neu value khong phai la so 
    """
    if not isinstance(value, (int, float)):
        raise ValueError("PM2.5 phai la mot so")
    if value < 12:
        return "GOOD"
    elif 12 <= value <= 35:
        return "Moderate"
    else:
        return "High"
print(classify_pm25(11.9))
print(classify_pm25(12))
print(classify_pm25(35))
print(classify_pm25(35.1))

# Bai 3 Chuẩn hóa dữ liệu 
def min_max_scale(values):
    """
    Chuẩn hóa các giá trị theo phương pháp Min-Max Scaling.

    Parameters
    ----------
    values : list
        Danh sách các giá trị cần chuẩn hóa.

    Returns
    -------
    list
        Danh sách mới với các giá trị được chuẩn hóa về khoảng [0, 1].
        Nếu max == min thì trả về danh sách toàn bộ giá trị 0.0.
    """
    min_value = min(values)
    max_value = max(values)

    if max_value == min_value:
        return [0.0 for _ in values]

    return [
        (x - min_value) / (max_value - min_value)
        for x in values
    ]
# test
values = [10, 20, 30, 40]

result = min_max_scale(values)

print(result)
print(values)

#Bai 4 Hàm đọc bản ghi cảm biến 
def parse_sensor_record(record):
    """
    Phân tích một bản ghi cảm biến từ chuỗi.

    Parameters
    ----------
    record: str
        chuoi co dinh dang:
        station_id, station_name, timestamp, pm25, temperature

    Returns
    -------
    dict
        dictionary gom: 
            station_id
            station_name
            timestamp
            pm25
            temperature
    
    Raise
    -----
    ValueError
        Neu chuoi khong co dung 5 truong.
    """
    fields = record.split(",")

    if len(fields) != 5:
        raise ValueError("ban ghi phai dung 5 truong.")

    station_id, station_name, timestamp, pm25, temperature = fields
    return { 
        "station_id": station_id,
        "station_name": station_name,
        "timestamp": timestamp,
        "pm25" : float(pm25),
        "temperature": float(temperature)
    }
record = "Tsh01, Tan son hoa, 2026-09-09 09:00, 31.5,29.2"
result = parse_sensor_record(record)
print(result)