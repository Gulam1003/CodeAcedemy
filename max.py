input_times = int(input("Enter how many number :"))
number = [float(input("Enter your number : ")) for ele in range(input_times)]

max_num = number[0]
for ele in number:
    if ele > max_num:
        max_num = ele

print(max_num)


