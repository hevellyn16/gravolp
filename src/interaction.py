import time


class Interaction:
    def __init__(self):
        pass

    def start_game(self):
        print('-=-' * 20)
        print('Iniciando o jogo...')
        print('-=-' * 20)
        time.sleep(3)

    def conversa_inicial(self):
        print(''' "Onde... Onde eu estou?
Não consigo me lembrar do que aconteceu..."\n ''')
        time.sleep(3)

        print('<Você se levanta vagarosamente e percebe que está numa praia. \n')
        time.sleep(4)
        print('''Olha ao redor, buscando informações que te lembrassem algo ou alguém
mas tudo que consegue ver é uma floresta e uma outra pessoa desmaiada na praia. \n''')
        time.sleep(6)
        print('Tudo que tem certeza é que seu nome... >\n')
        time.sleep(2)

        print("- Meu nome é Kiara!\n")
        time.sleep(2)

        print("<Ah, oi! Você consegue me ouvir? Ha, ha, ha. Não acredito! Que grande surpresa!>\n")
        time.sleep(3)

        while True:
            escolha1 = input("<Você está pronto para começar?> (sim/não): ").strip().lower()
            time.sleep(1)
            if escolha1 in ['sim', 's', 'si', 'não', 'nao', 'no', 'n', 'na']:
                if escolha1.lower() in ['sim', 'si', 's']:
                    print("\n<Muito bem, venha! Vou lhe explicar tudo que está acontecendo. Serei seu guia.>")
                elif escolha1.lower() in ['nao', 'não', 'na', 'n']:
                    print("\n<Ora, não faça birra, você já está aqui e consegue me ouvir. Vamos. Serei seu guia.>")
                time.sleep(2)

                break
            else:
                print("Opção inválida, por favor insira uma das alternativas mostradas.")

        print("\nVocê acaba seguindo a estranha voz falante.\n")
        time.sleep(2)

        print("- E então, você sabe o que aconteceu para eu vir parar aqui? \n")
        time.sleep(2)

        print("<Ah, bem... Como eu começo isso...>\n")
        time.sleep(1)

        print(' "Parece que a voz está desconfortável em falar sobre isso."\n ')
        time.sleep(2)

        print("- Só quero saber das coisas, leve seu tempo.\n")
        time.sleep(3)

    def conversa_1(self):
        while True:
            self.escolha2 = str(input("Ir na direção da pessoa desmaiada? (sim/não): ")).strip().lower()
            time.sleep(2)
            if self.escolha2.lower() in ['sim', 'si', 's', 'não', 'nao', 'no', 'n']:

                if self.escolha2.lower() in ['sim', 'si', 's']:
                    print("Você vai na direção da pessoa desmaiada.\n")
                    time.sleep(2)

                    escolha3 = str(input("Deseja tentar acordá-la? (sim/nao): "))
                    time.sleep(2)
                    if escolha3.lower() in ['sim', 'si', 's', 'não', 'nao', 'no', 'n', 'na']:

                        if escolha3.lower() in ['sim', 'si', 's']:
                            print("""\nVocê tenta acordar o homem, o balançando levemente, mas nada acontece.
Com uma estranha memória muscular, você leva seus dedos ao pescoço dele e fica pálida ao perceber que ele não só estava desacordado,""")
                            time.sleep(4)

                            print("mas como também estava morto!\n")
                            time.sleep(6)

                            print(
                                "Apavorada com aquilo você se volta para onde a voz anteriormente havia falado com ela.\n")
                            time.sleep(4)

                            print("""- O que é isso? Ele está morto! Me diga AGORA o que aconteceu! Por que estou aqui?
Por que tem um homem morto aqui? Ele morreu afogado? Será que estou presa sozinha
nesse fim de mundo? Eu também vou morrer?\n""")
                            time.sleep(4)

                            print("""Você examina o corpo superficialmente e percebe quão frio e azulado ele estava.
De alguma forma, você sente uma tristeza profunda por ver aquela pessoa naquele estado.
"Será que eu conhecia esta pessoa? O que ela significava para mim?" \n""")
                            time.sleep(10)


                        elif escolha3.lower() in ['nao', 'no', 'n', 'na', 'não']:
                            print("O que prefere fazer, então?\n")
                            time.sleep(1)
                            print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                            time.sleep(1)
                            escolha4 = str(input("Sua decisão: ")).strip()
                            time.sleep(1)

                            if escolha4.lower() == 'a':
                                print("Você vasculha a praia, mas não encontra nada além de conchas e alga marinha.")
                                time.sleep(2)

                                print("O que prefere fazer, então?\n")
                                time.sleep(1)
                                print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                                time.sleep(2)

                                escolha5 = str(input("Sua decisão: ")).strip()

                                if escolha5.lower() == 'b':
                                    print(
                                        "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                    time.sleep(2)
                                    break

                                elif escolha5.lower() == 'c':
                                    print("Você vai atrás de procurar suprimentos e encontra um diário ensopado.")
                                    time.sleep(2)

                                    print("O que prefere fazer, então?\n")
                                    time.sleep(1)
                                    print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                                    time.sleep(2)
                                    escolha7 = str(input("Sua decisão: ")).strip()

                                    if escolha7.lower() == 'b':
                                        print(
                                            "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                        time.sleep(2)
                                        break
                                    elif escolha7.lower() == 'a':
                                        print(
                                            "Você vasculha a praia e encontra um coqueiro, você pega alguns para poder comer depois.")
                                        time.sleep(2)
                                        break
                                    if escolha7.lower() == 'c':
                                        print("Você vai atrás de procurar suprimentos e encontra uma garrafa de água.")
                                        time.sleep(2)
                                        break
                                if escolha5.lower() == 'a':
                                    print(
                                        "Você vasculha a praia, mas não encontra nada além de conchas e alga marinha.")
                                    time.sleep(2)
                                    print("O que prefere fazer, então?\n")
                                    time.sleep(1)
                                    print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                                    time.sleep(2)

                                    escolha10 = str(input("Sua decisão: ")).strip()
                                    if escolha10.lower() == 'a':
                                        print(
                                            "Você vasculha a praia, mas não encontra nada além de conchas e alga marinha.")
                                        time.sleep(3)
                                        break

                                    elif escolha10.lower() == 'b':
                                        print(
                                            "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                        time.sleep(2)
                                        break

                                    if escolha10.lower() == 'c':
                                        print("Você vai atrás de procurar suprimentos e encontra um diário ensopado.")
                                        time.sleep(2)
                                        break

                            elif escolha4.lower() == 'b':
                                print(
                                    "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                time.sleep(2)
                                break

                            if escolha4.lower() == 'c':
                                print("Você vai atrás de procurar suprimentos e encontra um diário ensopado.")
                                time.sleep(2)

                                print("O que prefere fazer, então?\n")
                                time.sleep(1)
                                print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                                time.sleep(2)

                                escolha6 = str(input("Sua decisão: ")).strip()
                                if escolha6 == 'a':
                                    print(
                                        "Você vasculha a praia, mas não encontra nada além de conchas e alga marinha.")
                                    time.sleep(3)

                                    print("O que prefere fazer, então?\n")
                                    time.sleep(1)
                                    print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                                    escolha8 = str(input("Sua decisão: "))
                                    time.sleep(2)

                                    if escolha8.lower() == 'a':
                                        print(
                                            "Você vasculha a praia, mas não encontra nada além de conchas e alga marinha.")
                                        time.sleep(3)
                                        break

                                    elif escolha8.lower() == 'b':
                                        print(
                                            "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                        time.sleep(2)
                                        break

                                    if escolha8.lower() == 'c':
                                        print("Você vai atrás de procurar suprimentos e encontra um diário ensopado.")
                                        time.sleep(2)
                                        break

                                elif escolha6 == 'b':
                                    print(
                                        "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                    time.sleep(2)
                                    break
                                if escolha6 == 'c':
                                    print("Você vai atrás de procurar suprimentos e encontra um diário ensopado.")
                                    time.sleep(2)

                                    print("O que prefere fazer, então?\n")
                                    time.sleep(1)
                                    print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                                    escolha9 = str(input("Sua decisão: "))
                                    time.sleep(2)

                                    if escolha9.lower() == 'a':
                                        print(
                                            "Você vasculha a praia, mas não encontra nada além de conchas e alga marinha.")
                                        time.sleep(3)
                                        break

                                    elif escolha9.lower() == 'b':
                                        print(
                                            "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                        time.sleep(2)
                                        break

                                    if escolha9.lower() == 'c':
                                        print("Você vai atrás de procurar suprimentos e encontra um diário ensopado.")
                                        time.sleep(2)
                                        break
                        break
                    else:
                        print("Opção inválida, por favor insira uma das alternativas mostradas.")


                elif self.escolha2.lower() in ['nao', 'no', 'n', 'na', 'não']:
                    print("O que prefere fazer, então?\n")
                    time.sleep(1)
                    print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                    time.sleep(1)
                    escolha11 = str(input("Sua decisão: ")).strip()
                    time.sleep(1)

                    if escolha11.lower() == 'a':
                        print("Você vasculha a praia, mas não encontra nada além de conchas e alga marinha.")
                        time.sleep(2)

                        print("O que prefere fazer, então?\n")
                        time.sleep(1)
                        print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                        time.sleep(2)

                        escolha12 = str(input("Sua decisão: ")).strip()

                        if escolha12.lower() == 'b':
                            print(
                                "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                            time.sleep(2)
                            break

                        elif escolha12.lower() == 'c':
                            print("Você vai atrás de procurar suprimentos e encontra um diário ensopado.")
                            time.sleep(2)

                            print("O que prefere fazer, então?\n")
                            time.sleep(1)
                            print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                            time.sleep(2)
                            escolha13 = str(input("Sua decisão: ")).strip()

                            if escolha13.lower() == 'b':
                                print(
                                    "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                break
                            elif escolha13.lower() == 'a':
                                print(
                                    "Você vasculha a praia e encontra uma garrafa que você decide guardar para pegar água potável depois.")
                                time.sleep(2)
                                return False
                            if escolha13.lower() == 'c':
                                print(
                                    "Você vai atrás de procurar suprimentos e encontra um coqueiro, você pega alguns para guardar")
                                time.sleep(2)
                                break
                        if escolha12.lower() == 'a':
                            print(
                                "Você vasculha a praia e encontra um coqueiro, você decide pegar alguns para comer depois.")
                            time.sleep(2)
                            print("O que prefere fazer, então?\n")
                            time.sleep(1)
                            print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                            time.sleep(2)

                            escolha14 = str(input("Sua decisão: "))
                            if escolha14.lower() == 'a':
                                print(
                                    "Você vasculha a praia e encontra alguns galhos, você pega alguns para ver se consegue fazer uma fogueira depois.")
                                time.sleep(3)
                                break

                            elif escolha14.lower() == 'b':
                                print(
                                    "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                time.sleep(2)
                                break

                            if escolha14.lower() == 'c':
                                print("Você vai atrás de procurar suprimentos e encontra um diário ensopado.")
                                time.sleep(2)
                                break

                    elif escolha11.lower() == 'b':
                        print("Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                        time.sleep(2)
                        break

                    if escolha11.lower() == 'c':
                        print("Você vai atrás de procurar suprimentos e encontra um diário ensopado.")
                        time.sleep(2)

                        print("O que prefere fazer, então?\n")
                        time.sleep(1)
                        print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                        time.sleep(2)

                        escolha15 = str(input("Sua decisão: "))
                        if escolha15 == 'a':
                            print(
                                "Você vasculha a praia e encontra uma garrafa, você a pega para futuramente colocar água potável.")
                            time.sleep(3)

                            print("O que prefere fazer, então?\n")
                            time.sleep(1)
                            print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
------------------------------ \n""")
                            escolha16 = str(input("Sua decisão: "))
                            time.sleep(2)

                            if escolha16.lower() == 'a':
                                print("Você vasculha a praia e encontra alguns galhos.")
                                time.sleep(3)
                                break

                            elif escolha16.lower() == 'b':
                                print(
                                    "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                time.sleep(2)
                                break

                            if escolha16.lower() == 'c':
                                print(
                                    "Você vai atrás de procurar suprimentos e encontra um coqueiro, você pega alguns para comer mais tarde.")
                                time.sleep(2)
                                break

                        elif escolha15 == 'b':
                            print(
                                "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                            time.sleep(2)
                            break
                        if escolha15 == 'c':
                            print(
                                "Você vai atrás de procurar suprimentos e encontra um coqueiro, você pega alguns para poder comer depois.")
                            time.sleep(2)

                            print("O que prefere fazer, então?\n")
                            time.sleep(1)
                            print("""------------------------------
A - Vasculhar a praia
B - Esperar a voz
C - Procurar suprimentos
        ------------------------------ \n""")
                            escolha17 = str(input("Sua decisão: "))
                            time.sleep(2)

                            if escolha17.lower() == 'a':
                                print(
                                    "Você vasculha a praia e encontra alguns galhos, você os pega pensando que talvez dê para fazer uma fogueira com eles.")
                                time.sleep(3)
                                break

                            elif escolha17.lower() == 'b':
                                print(
                                    "Você espera pacientemente a voz ficar pronta para lhe falar o que estava acontecendo.")
                                time.sleep(2)
                                break

                            if escolha17.lower() == 'c':
                                print(
                                    "Você vai atrás de procurar suprimento e encontra uma garrafa, você a pega para colocar água potável quando achar.")
                                time.sleep(2)
                                break
                break
            else:
                print("Opção inválida. Por favor, insira uma das alternativas mostradas.")

