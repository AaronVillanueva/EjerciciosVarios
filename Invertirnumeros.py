def invertirNumero(n):
    inverso=0
    while n>=10:
        digitoDerecho=n%10
        inverso=inverso*10 + digitoDerecho
        print (digitoDerecho)
        n = n // 10
    inverso=inverso*10 + n
    print (n)
    print(inverso)

invertirNumero(123)
