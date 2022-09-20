def calc(x, y, op):
    if(op == '+'):
        return x + y
    elif(op == '-'):
        return x - y
    elif(op == '*'):
        return x * y
    elif(op == '/'):
        return x / y
    elif(op == '**'):
        return x ** y
    else:
        return 'Invalid input.'
        
exit = 0
saved_outputs = []
while(exit != 1):
    try:
        x = float(input('X : '))
        y = float(input('Y : '))                                           
        op = input('Operation?\n(+)\n(-)\n(*)\n(/)\n(**)\n')
        result = calc(x, y, op)
        saved_outputs.append(result)
        print(f'{x} {op} {y} = {result}')
        view_saved = input('View saved outputs?(Y or N)\n')
        if(view_saved.upper() == 'Y'):
            i = len(saved_outputs) - 1
            while(i >= 0):
                print(saved_outputs[i])
                i -= 1
        exit = input('Exit?(Y or N)\n')
        if(exit.upper() == 'Y'):
            exit = 1
    except ValueError:
        print('Operands must be decimal or integer values.')

