def Operacao(num1, num2, operacao = '+'):
    num1 = int(num1)
    num2 = int(num2)
    if(operacao == '+'):
        return num1+num2
    elif(operacao == '-'):
        return num1-num2
    elif(operacao == '*'):
        return num1*num2
    elif(operacao == '/'):
        return num1/num2
    elif(operacao == '%'):
        return num1 % num2
    elif(operacao == '^'):
        return num1**num2
    else:
        error = "Operacao invalida."  
        return error

continua = True
while(continua):
    num1 = input("digite um numero: ")
    num2 = input("digite outro numero: ")
    op = input("digite a operacao: ")

    resp = Operacao(num1,num2,op)
    print(resp)
    c = input("Deseja fazer outra operacao?(s/n) ")
    if(c == 'n'):
        continua = False
    else:
        continua = True