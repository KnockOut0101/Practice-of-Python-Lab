from os import remove


x = "2 * ( 3 + 4 ) - 10 / 4"

def pop(x):
    temp = x[-1]
    x = x[:-1]
    return x,temp


def EvalExpression(x):

    split_list=x.split()

    print(split_list)

    operand = []

    operator = ["(",")","/","*","+","-"]

    for i in range(len(split_list)):
        if(split_list[i].isnumeric()):
            print("if 1")
            operand.append(split_list[i])
            print(operand)
        elif(split_list[i] == operator[0]):
            print("if 2")
            operand.append(split_list[i])
            print(operand)
        elif(split_list[i] == operator[1]):
            print("if 3")
            operand,temp = pop(operand)
            operand.remove('(')
            print(temp)
        elif(split_list[i] == operator[2]):
            print("if 4")
            operand.append('')
        elif(split_list[i] == operator[3]):
        elif(split_list[i] == operator[4]):
        elif(split_list[i] == operator[5]):'''





EvalExpression(x)

