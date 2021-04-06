#문제3
cnt = int(input())
nums = input()

num_list = nums.split()
int_list = list(map(int, num_list))

num_min = min(int_list)
num_max = max(int_list)

print(num_min, num_max)
