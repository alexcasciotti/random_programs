
# smaple input
# 3949 + 9339
def calc():
    expression = input('Enter a mathematical expression...\nValid operators:\n(+)\n(-)\n(*)\n(/)\n(**)\n')
    for x in expression:
        if(x == '+'):
            index = expression.index(x)
            try:
                first_num = float(expression[0:index])
                second_num = float(expression[index+1:])
                return first_num + second_num
            except ValueError:
                print('Enter numbers for the operands...')
        if(x == '-'):
            index = expression.index(x)
            try:
                first_num = float(expression[0:index])
                second_num = float(expression[index+1:])
                return first_num - second_num
            except ValueError:
                print('Enter numbers for the operands...')
        if(x == '*'):
            index = expression.index(x)
            try:
                first_num = float(expression[0:index])
                second_num = float(expression[index+1:])
                return first_num * second_num
            except ValueError:
                print('Enter numbers for the operands...')
        if(x == '/'):
            index = expression.index(x)
            try:
                first_num = float(expression[0:index])
                second_num = float(expression[index+1:])
                return first_num / second_num
            except ValueError:
                print('Enter numbers for the operands...')
        if(x == '**'):
            index = expression.index(x)
            try:
                first_num = float(expression[0:index])
                second_num = float(expression[index+1:])
                return first_num ** second_num
            except ValueError:
                print('Enter numbers for the operands...')
print(calc())