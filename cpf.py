#gerador de cpfs
import random;
#Digitos Verificadores
#Os nove primeiros algarismos são ordenadamente multiplicados pela 
# sequência 10  , 99, 88, 77, 66, 55, 44, 33, 22 (o primeiro por 1010, o segundo por 99, e assim sucessivamente)
# . Em seguida, calcula-se o resto rr da divisão da soma dos resultados das multiplicações por 1111:
#se esse resto for 00 ou 11, o primeiro dígito verificador é zero (d1=0d1=0); caso contrário, d1=11−rd1=11−r.
nome_forca = ['gato','cachorro']
#CPF DEVE CONTER 11 DIGITOS E SER GERADO AUTOMATICAMENTE 
nomes = ["Vinicius", "Maicon", "Clara", "Andre","Joao","Jose","Joaquin","Rafael","Anne","Pedro","Alan"]
nome_cpf = random.choice(nomes)
numeros = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,]
aleatorio = random.randrange(0,10)
primeiro,segundo,terceiro,quarto,quinta,sexto,setimo,oitavo,nono,decimo, = numeros

cpf = random.choices(numeros,k=11)
print(f'cpf novo e {cpf}')

def calculodigito(int):
    for int in cpf:
        print(f'os int sao {int}')
        


if nome_cpf =="Clara":
    nome_cpf = nome_cpf
    print(f'o cpf do meu amor linda da minha vida {nome_cpf} e {cpf[0]}.{cpf[1]}.{cpf[2]}.{cpf[3]}.{cpf[4]}.{cpf[5]}.{cpf[6]}.{cpf[7]}.{cpf[8]}-{cpf[9]}{cpf[10]}')
elif nome_cpf=="Vinicius":
        print(f'o cpf do amor  lindo da vida da Clara e  {nome_cpf} e {cpf[0]}.{cpf[1]}.{cpf[2]}.{cpf[3]}.{cpf[4]}.{cpf[5]}.{cpf[6]}.{cpf[7]}.{cpf[8]}-{cpf[9]}{cpf[10]}')
        
else:
    print(f'o cpf de {nome_cpf} e {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}')
    calculodigito(cpf[9])

    