# Pass multiple arguments to the map() function

def multiply(a, b):
    return a * b


list_1 = [1, 2, 3, 4, 5]

list_2 = [6, 7, 8, 9, 10]

new_list = list(map(multiply, list_1, list_2))
print(new_list)  # 👉️ [6, 14, 24, 36, 50]