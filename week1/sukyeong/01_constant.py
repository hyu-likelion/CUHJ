num1, num2 = input().split()

def reverse_Num(num):
    num_list = []
    while num > 0:
        temp = num % 10
        num_list.append(int(temp))
        num = (num-temp) / 10
    new_num = 100 * num_list[0] + 10 * num_list[1] + 1 * num_list[2]

    return new_num

def num_Comparison(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)

new_num1 = reverse_Num(int(num1))
new_num2 = reverse_Num(int(num2))

num_Comparison(new_num1, new_num2)


