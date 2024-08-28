#PROVA 3 DE LOGICA DE PROGRAMAÇÃO

numero = int(input("Digite um número inteiro de 1 a 10 para gerar a tabuada: "))

if 1 <= numero <= 10:
    print(f"Tabuada de {numero}:")

    for i in range(1, 11):
        resultado = numero * i

        print(f"{numero} X {i} = {resultado}")
        
else:
    print("Número fora do intervalo permitido. Por favor, escolha um número")
