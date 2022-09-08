# Quiz: Numero capicua de 5 digitos

print("------------------------------------")
print("------NUMERO-CAPICUA-DE-5-DIGITOS---")
print("------------------------------------")

#input
n=int(input("Digite un numero :"))


#procesing
if (n>=10000 and n<=99999):
    n5= n % 10
    n4= (n % 100) // 10
    n3= (n % 1000) // 100
    n2= (n%10000) // 1000
    n1= n//10000

    if n1==n5 and n2==n4:
        print("El numero",n," es capicua")
    else:
            print("El numero",n,"no es capicua")

else:
    print("El numero",n,"no es de 5 digitos")

#finish
