def print_details(id,**keyword):
    print(keyword)
    print(id)
    for i in keyword:
        print(i, keyword[i])
print_details(123, name="shay", age=14)