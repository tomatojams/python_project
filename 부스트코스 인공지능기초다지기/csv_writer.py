line_counter = 0
data_header = []
custom_list = []

with open(
    "data\customer.csv", encoding="UTF-8"
) as customer_data:  # 윈도우에서에러날때 encoding 옵션을 지정
    while True:
        data = customer_data.readline()
        if not data:
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            custom_list.append(data.split(","))
        line_counter += 1

print("header :\t", data_header)
for i in range(0, 10):
    print("Data", i, "\t\t", custom_list[i])
