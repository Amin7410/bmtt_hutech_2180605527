def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("list: ", numbers)
print(f"Tuple được tạo từ list: {my_tuple}")