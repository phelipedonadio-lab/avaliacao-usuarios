#Variáveis que vão guardar as avaliações
total_excelente = 0
total_bom = 0
total_ruim = 0

#Estrutura de repetição (for): vai entrevistar 50 pessoas
for i in range(50):

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    #Exibir opções de avaliação
    print(
        "\nAvalie o serviço prestado:\n" \
    "1 - Excelente\n" \
    "2 - Bom\n" \
    "3 - Ruim")
    opiniao = int(input("Digite o número da opção de avaliação: "))

    #Estrutura decisão (match/case): vai verificar a avaliação escolhida
    match opiniao:
        case 1:
            total_excelente += 1
            print (f"{nome.title()}, sua avaliação foi registrada como Excelente. Muito obrigado!")
        case 2:
            total_bom += 1
            print (f"{nome.title()}, sua avaliação foi registrada como Bom. Obrigado!")
        case 3:
            total_ruim += 1
            print (f"{nome.title()}, sua avaliação foi registrada como Ruim. Obrigado!")
        case _:
            print("Opção inválida. Avaliação não registrada.")

#Exibir resultados finais
print(
    f"\nQuantidade de notas EXCELENTES: {total_excelente}\n"
    f"Quantidade de notas BONS: {total_bom}\n"
    f"Quantidade de notas RUINS: {total_ruim}\n")
