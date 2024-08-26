def double_it(num):
    result = num * 2
    print('inside the function.py file',result)
    return result

double_it(8)
double_it(188)

def sum(num1, num2):
    result = num1 + num2
    return result

total = sum(23, 27)
print('total value:',total)

final = double_it(total)
print('final value is:',final)