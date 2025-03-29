#gerador de cpfs
import random;
#CPF DEVE CONTER 11 DIGITOS E SER GERADO AUTOMATICAMENTE 

numeros = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,]
aleatorio = random.randrange(0,10)
primeiro,segundo,terceiro,quarto,quinta,sexto,setimo,oitavo,nono,decimo, = numeros
print(aleatorio)

print(random.choices(numeros, k = 11))
cpf = random.choices(numeros,k=11)
print(cpf[0])

print(f'o cpf novo e {cpf[0]}.{cpf[1]}.{cpf[2]}.{cpf[3]}.{cpf[4]}.{cpf[5]}.{cpf[6]}.{cpf[7]}.{cpf[8]}.{cpf[9]}.{cpf[10]}')
print("teste")