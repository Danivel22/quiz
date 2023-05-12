import json
import os
import sys
import random
from colorama import Fore, Style

def exibir_menu():

           #Limpar a tela do terminal                      
    os.system('cls' if os.name == 'nt' else 'clear')

    # Tentar carregar perguntas do arquivo de texto
    try:
        with open("perguntas.txt", "r") as f:
            perguntas = json.load(f)
    except FileNotFoundError:
        perguntas = []

    num_perguntas = len(perguntas)

    print(Fore.YELLOW +  f"||                  1. ADICIONAR PERGUNTAS          ||" + Style.RESET_ALL)
    print(Fore.BLUE +    f"||                     2. JOGAR                     ||" + Style.RESET_ALL)
    print(Fore.RED +     f"||                  3. APAGAR PERGUNTAS             ||" + Style.RESET_ALL)
    print(Fore.GREEN +   f"||                     4. SAIR                      ||" + Style.RESET_ALL)
    print(Fore.BLUE + "===================================================")
    print(Fore.RED +    f"(ATUALMENTE {num_perguntas} PERGUNTAS REGISTRADAS)" + Style.RESET_ALL)

escolha = 0
while escolha != 4:
    exibir_menu()
    try:
       while True:
        escolha = int(input("Digite o número correspondente à opção desejada: "))
        break
    except ValueError:
        print("Por favor, digite um número válido.")
    
    if escolha == 1:
    # Adicionar perguntas
        print(Fore.YELLOW + "\nOpção 1 selecionada. Adicionar perguntas.\n" + Style.RESET_ALL)

        # Tentar carregar perguntas do arquivo de texto
        try:
            with open("perguntas.txt", "r") as f:
                perguntas = json.load(f)
        except FileNotFoundError:
            perguntas = []

        while True:
            try:
                num_perguntas = int(input("Quantas perguntas deseja adicionar? "))
                break
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.RED + "Por favor, digite um número inteiro válido." + Style.RESET_ALL)

        for i in range(num_perguntas):
            os.system('cls' if os.name == 'nt' else 'clear')
            pergunta = ""
            print(Fore.YELLOW + f"Pergunta {i+1}: " + Style.RESET_ALL)
            for line in sys.stdin:
                if line.strip() == "":
                    break
                pergunta += line
            
            opcoes = []
            for j in range(5):
                opcao = input(Fore.YELLOW + f"Opção {j+1}: " + Style.RESET_ALL)
                if opcao:
                    opcoes.append(opcao)
                else:
                    break
            
            resposta_correta = input(Fore.YELLOW + "Resposta correta: " + Style.RESET_ALL)
            
            perguntas.append({
                "pergunta": pergunta.strip(),
                "opcoes": opcoes,
                "resposta_correta": resposta_correta
            })

            # Salvar perguntas em um arquivo de texto de forma organizada
            with open("perguntas.txt", "w") as f:
                json.dump(perguntas, f, indent=4)

    if escolha == 2:
        jogando = True

        while jogando:

            os.system('cls' if os.name == 'nt' else 'clear')

            # Jogar
            print("Opção 2 selecionada. Jogar.")

            # Carregar perguntas do arquivo de texto
            try:
                with open("perguntas.txt", "r") as f:
                    perguntas = json.load(f)
            except FileNotFoundError:
                print(Fore.RED + "Nenhuma pergunta encontrada. Por favor, crie perguntas antes de jogar." + Style.RESET_ALL)
                input("Pressione ENTER para continuar...")
                break

            # Embaralhar perguntas aleatoriamente
            random.shuffle(perguntas)

            num_corretas = 0
            num_incorretas = 0

            # Loop através de cada pergunta
            while len(perguntas) > 0:
                pergunta = perguntas.pop(0) # Remove a primeira pergunta da lista
                print(f"\n{Fore.YELLOW}Pergunta{Style.RESET_ALL} {num_corretas+num_incorretas+1}: {pergunta['pergunta']}\n") # Adicionar um caractere de quebra de linha após a pergunta

                # Embaralhar opções de resposta aleatoriamente
                opcoes = pergunta['opcoes']
                random.shuffle(opcoes)

                # Exibir opções de resposta com letras do alfabeto
                letras = ["A", "B", "C", "D", "E"][:len(opcoes)]
                for j, opcao in enumerate(opcoes):
                    print(f"{letras[j]}. {opcao}")

                # Obter resposta do usuário
                while True:
                    resposta_usuario_letra = input("Qual é a resposta correta? ").upper()
                    try:
                        resposta_usuario_indice = letras.index(resposta_usuario_letra)
                        break
                    except ValueError:
                        print("\rPor favor, digite uma letra válida novamente.", end='')
                       



                # Verificar se a resposta está correta ou incorreta
                resposta_correta = pergunta['resposta_correta']
                if resposta_usuario_indice < len(opcoes) and opcoes[resposta_usuario_indice] == resposta_correta:
                    print(Fore.GREEN + "Resposta correta!" + Style.RESET_ALL)
                    num_corretas += 1
                else:
                    print(Fore.RED + f"Resposta incorreta. A resposta correta é: {resposta_correta}" + Style.RESET_ALL)
                    num_incorretas += 1

            # mostrar o resultado em cores diferentes
            print(f"\nFim do jogo! \033[32m acertou\033[m  {num_corretas} perguntas e \033[31merrou\033[m {num_incorretas} perguntas.")


            
            # Perguntar ao jogador se ele deseja jogar novamente
            resposta = input("Digita s para jogar novamente ou pressione Enter para sair.")
            
            if resposta == "s":
                jogando = True
            else:
                jogando = False

                
    elif escolha == 3:
        # Apagar perguntas
        print("Opção 3 selecionada. Apagar perguntas.")
        
    # Carregar perguntas do arquivo de texto
        try:
            with open("perguntas.txt", "r") as f:
                        perguntas = json.load(f)
        except FileNotFoundError:
                    print(Fore.RED + "Nenhuma pergunta encontrada." + Style.RESET_ALL)
                    input("Pressione ENTER para continuar...")
                    continue

        # Exibir cada pergunta e pedir confirmação antes de apagar
        for i, pergunta in enumerate(perguntas):
            print(f"\nPergunta {i+1}: {pergunta['pergunta']}")
            confirmacao = input("Deseja apagar esta pergunta? (s/n) ")
            
            if confirmacao.lower() == "s":
                del perguntas[i]
                print("Pergunta apagada.")
            else:
                print("Pergunta mantida.")
        
            # Salvar perguntas atualizadas no arquivo de texto
            with open("perguntas.txt", "w") as f:
                json.dump(perguntas, f, indent=4)
                
    elif escolha == 4:
          print(Fore.GREEN + "Saindo do programa" + Style.RESET_ALL)         


                           