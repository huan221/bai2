transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

# bước 1: xóa khoảng trắng ngoài
transaction = transaction.strip()

# bước 2: tách chuỗi
parts = transaction.split("|")

# bước 3: chuẩn hóa từng phần
name = parts[0].strip().title()
course = parts[1].strip()
amount = parts[2].strip()
status = parts[3].strip().upper()

# bước 4: xử lý số tiền
amount = int(amount)
amount_format = "{:,}".format(amount)

# bước 5: in kết quả
print("Học viên:", name)
print("Khóa học:", course)
print("Số tiền:", amount_format, "VND")
print("Trạng thái:", status)