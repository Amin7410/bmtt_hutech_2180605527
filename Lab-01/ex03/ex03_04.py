def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]

    input_tuple = eval(input("Nhập vào một tuple: "))
    first, last = truy_cap_phan_tu(input_tuple)

    print(f"Phần tử đầu tiên của tuple là: {first}")
    print(f"Phần tử cuối cùng của tuple là: {last}")