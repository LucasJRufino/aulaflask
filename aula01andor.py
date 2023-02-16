x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if x > y and x > z:
    result = "x é o maior"
    
elif y > x and y > z:
    result = "y é o maior"
    
elif z > x and z > y:
    result = "z é o maior"
    
else:
    result = "há números iguais"

print(result)

