# Bài 5. Sắp xếp dữ liệu nhiều tiêu chí 
stations = [ 
    {"id": "A01", "name": "Tan Son Hoa", "pm25": 32.5, "temp": 30.1}, 
    {"id": "A02", "name": "Thu Duc", "pm25": 18.2, "temp": 29.4}, 
    {"id": "A03", "name": "Bien Hoa", "pm25": 41.8, "temp": 31.0}, 
    {"id": "A04", "name": "Nha Be", "pm25": 32.5, "temp": 28.8} 
]
sorted_stations = sorted(stations,
                         key=lambda x: (-x["pm25"], x["temp"])) # dấu "-" dùng để đảo ngược thứ tự tăng dần thành giảm dần. 
                                                                # x["temp"] Nếu có các trạm có chỉ số pm25 bằng nhau, Python sẽ nhìn sang tiêu chí thứ hai này để sắp xếp theo nhiệt độ temp tăng dần (từ thấp đến cao).    
stations_name = list(map(lambda x: x["name"],sorted_stations))

print(sorted_stations)
print(stations_name)

# Bài 6. Biến đổi đơn vị (Đổi Celsius → Fahrenheit)
# 
temperatures_c = [20,25,30,35,40]
temperatures_f = list(
    map(lambda c: round(c * 9 / 5 +35 ,1 ), temperatures_c)
)
labels = list(
    map(lambda c: "hot" if c > 32 else "normal", temperatures_c)
)

print(temperatures_f)
print(labels)

# Bài 7. Lọc dữ liệu hợp lệ
raw_values = [12.5, -999, 18.0, None, 25.4, "error", 30.2, -1]

valid_values = list(
    filter(
        lambda x: isinstance(x, (int, float)) and x >= 0,
        raw_values
    )
)

mean_value = sum(valid_values) / len(valid_values)

print(valid_values)
print(mean_value)

# Bai 8: Trích xuất thuộc tính
records = [
    ("A01", "Tan Son Hoa", 42.5),
    ("A02", "Thu Duc", 28.4),
    ("A03", "Go Vap", 37.2),
    ("A04", "District 1", 25.1)
]
names = list(
    map(lambda record: record[1], records)
)
high_pm25_records = list(
    filter(lambda record: record[2] > 35, records)
)
high_stations = list(
    map(
        lambda record: (record[1], "High"),
        high_pm25_records
    )
)

print(high_stations)