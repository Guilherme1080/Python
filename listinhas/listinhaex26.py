a = float(input("digite a primeira medida: "))
b = float(input("digite a segunda medida: "))
c = float(input("digite a terceira medida: "))
if(a != b != c):
    print("escaleno")
elif( a == b == c):
    print("equilatero")
elif(a==b or b==a or c==a or a==c or b==c or c==b):
    print("isosceles")
else:
    print("ERROR404")