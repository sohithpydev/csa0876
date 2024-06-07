num = int(input("enter a number:"))
divisor_num = 1
for i in range(2,num//2+1):
    if num % i == 0:
        divisor_num+=i
if divisor_num == num and num!=1:
    print("perfect")
else:
    print("imperfect")
