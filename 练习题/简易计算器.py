num1 = float(input("请输入第一个数字："))
operate = input("请输入符号：+ - * /\n")
num2 = float(input("请输入第二个数字："))
result = 0
if operate == '*':
    result = num1 * num2
elif operate == '+':
    result = num1 + num2
elif operate == '-':
    result = num1 - num2
elif operate == '/':
    if num2 == 0:
        print('除数不能为0')
    else:
        result = num1 / num2
else:
    print("error")
    exit()
print(f'{num1}{operate}{num2}={result}')
