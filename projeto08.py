#Simulador de Lançamento de Dados:
#Crie um programa que simule o lançamento de um dado e conte quantas vezes cada número aparece em um número específico de lançamentos. Use um laço de repetição for para simular os lançamentos.

import random

# Função para simular o lançamento de um dado
def simular_lancamento_dados(n_lancamentos):
    # Dicionário para contar a frequência de cada número
    frequencia_numeros = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    # Realiza os lançamentos e conta a frequência de cada número
    for _ in range(n_lancamentos):
        resultado_lancamento = random.randint(1, 6)
        frequencia_numeros[resultado_lancamento] += 1
    
    return frequencia_numeros

# Solicita ao usuário o número de lançamentos a serem simulados
n_lancamentos = int(input("Digite o número de lançamentos a serem simulados: "))

# Chama a função para simular o lançamento de dados
frequencia_numeros = simular_lancamento_dados(n_lancamentos)

# Imprime a frequência de cada número
print("Frequência de cada número:")
for numero, frequencia in frequencia_numeros.items():
    print(f"Número {numero}: {frequencia} vezes")

#Este código utiliza a biblioteca random para simular o lançamento de um dado. A função simular_lancamento_dados(n_lancamentos) recebe o número de lançamentos desejado como entrada e retorna um dicionário que conta a frequência de cada número observado nos lançamentos. O usuário é solicitado a inserir o número de lançamentos desejado, e então o código exibe a frequência de cada número na saída padrão.


'''Explicando o código acima:

1) Importação da Biblioteca random:
- A primeira linha importa a biblioteca random, que será usada para gerar números aleatórios.

2) Definição da Função simular_lancamento_dados:
- A função simular_lancamento_dados(n_lancamentos) é definida para simular o lançamento de um dado um número específico de vezes e contar a frequência de cada número.
- Um dicionário frequencia_numeros é inicializado para armazenar a frequência de cada número (de 1 a 6).
- Um loop for é utilizado para simular n_lancamentos de dados.
- Dentro do loop, a função random.randint(1, 6) é utilizada para gerar um número aleatório entre 1 e 6, simulando o lançamento de um dado.
- O número obtido é então usado como chave para acessar o valor correspondente no dicionário frequencia_numeros, e este valor é incrementado em 1 para contar a ocorrência do número.
- Após todos os lançamentos, o dicionário frequencia_numeros é retornado.

3) Solicitação do Número de Lançamentos ao Usuário:
- O programa solicita ao usuário que insira o número de lançamentos que deseja simular.

4) Chamada da Função e Impressão dos Resultados:
- A função simular_lancamento_dados() é chamada com o número de lançamentos fornecido pelo usuário como argumento.
- A frequência de cada número é então impressa na saída padrão utilizando um loop for sobre os itens do dicionário frequencia_numeros.

Em resumo, este código simula o lançamento de um dado um número específico de vezes, contando quantas vezes cada número aparece, e então imprime a frequência de cada número na saída padrão.'''
