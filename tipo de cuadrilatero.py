lado1 = input("a = ")
lado2 = input("b = ")
lado3 = input("c = ")
lado4 = input("d = ")

if lado1 and lado2 and lado3 == lado4:
    print("Es un cuadrado")
else: 
    if lado1 == lado2 and lado3 == lado4 or lado1 == lado3 and lado2 == lado4:
        print("Es un rectangulo")
    else:
        print("Es un cuadrilatero")