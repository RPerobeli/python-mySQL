
def ResolveEquacao2Ordem(inputs):
    a= inputs[0]
    b= inputs[1]
    c = inputs[2]
    delta = b**2-4*a*c
    r1 = (-b - delta**0.5) / (2*a)
    r2 = (-b + delta**0.5) / (2*a)
    return [r1,r2]

#main
inputs = [1,5,4]
raizes = ResolveEquacao2Ordem(inputs)
print(raizes)