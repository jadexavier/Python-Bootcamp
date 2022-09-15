def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def exp(n1, n2):
    return n1 ** n2

operators = {'+': add, '-': sub, '*': mult, '/': div, '**': exp}

def calculate():

    use_last_var = True
    num1 = float(input("What is the first number?\n"))
    
    while use_last_var == True:
        
        op = input("What operation? (+, -, *, /, **)?\n")
        num2 = float(input("What is the second number?\n"))
        
        operate = operators[op]
        result = operate(num1, num2)
        
        print(f"{num1} {op} {num2} = {result}")
        
        cont = input("Continue with result or exit? (y/n/x)?\n")
        if  cont == 'y':
            num1 = result
        elif cont == 'n':
            use_last_var = False
        else:
            break
            
    if cont != 'x':        
        calculate()
    
calculate()
    
        
        