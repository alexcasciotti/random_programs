import data_structures as ds

def calc(x, y, op):
    if(op == '+'):
        return x + y
    if(op == '-'):
        return x - y
    if(op == '*'):
        return x * y
    if(op == '/'):
        return x / y
    if(op == '**'):
        return x ** y
        
exit = 0
saved_outputs = ds.myStack()
while(exit != 1):
    try:
        x = float(input('X : '))
        y = float(input('Y : '))
        op = input('Operation?\n(+)\n(-)\n(*)\n(/)\n(**)\n')
        result = calc(x, y, op)
        saved_outputs.push(result)
        print(f'{x} {op} {y} = {result}')
        view_saved = input('View saved outputs?(Y or N)')
        if(view_saved.upper() == 'Y'):
            while(saved_outputs.isEmpty() == False):
                print(saved_outputs.pop())
        exit = input('Exit?(Y or N)\n')
        if(exit.upper() == 'Y'):
            exit = 1
    except ValueError:
        print('Operands must be decimal or integer values.')

