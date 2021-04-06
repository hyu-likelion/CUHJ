#문제1
nums = input()
num1 = int(nums.split(" ")[0])
num2 = int(nums.split(" ")[1])
if num1 > num2 :
    print(">")
        
if num1 < num2 :
    print("<")

if num1 == num2 :
    print("==")
