print("Olá recrutadores!")
question = int(input("Qual questão você quer ver?\n(1) Fibonacci\n(2) Verificador de Letra A\n"
                     "(3) Questão de Soma\n(4) Questão de Lógica\n(5) Interruptores\n"))

if question == 1:
    def num_fibo(n):
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n or n == 0


    numero = int(input("Informe um número para conferir se ele pertence à sequência de Fibonacci: "))

    if num_fibo(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

elif question == 2:
    quantidade_a = input("Escreva uma palavra qualquer: ")
    letra_a = quantidade_a.lower().count('a')
    if letra_a == 0:
        print(f"A sua palavra '{quantidade_a}' não possui letra 'a'.")
    elif letra_a == 1:
        print(f"A sua palavra '{quantidade_a}' possui {letra_a} letra 'a'.")
    else:
        print(f"A sua palavra '{quantidade_a}' possui {letra_a} letras 'a'.")

elif question == 3:
    INDICE = 12
    SOMA = 0
    K = 1
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    print(f"Logo, o valor requerido da soma é {SOMA}")

elif question == 4:
    print("a) 1, 3, 5, 7, x \nR: A resposta é x = 9, acrescentando 2 em cada termo.\n"
          "b) 2, 4, 8, 16, 32, 64, y\nR: A resposta é y = 128, multiplicando os termos seguintes por 2.\n"
          "c) 0, 1, 4, 9, 16, 25, 36, z\nR: A resposta é z = 49, trata-se do quadrado dos valores em ordem 1,2,3...\n"
          "d) 4, 16, 36, 64, a\nR: A resposta é a = 100, sendo 4*n*n, com n seguindo a ordem 1,2,3...\n"
          "e) 1, 1, 2, 3, 5, 8, b\nR: Sequência de Fibonacci.\n"
          "f) 2, 10, 12, 16, 17, 18, 19, c\nR: A resposta é c = 200, porque são números que começam com a letra 'd'.")

elif question == 5:
    print("Descrevendo a solução:")
    print(
        "Supondo que os interruptores são A, B e C, há 3! (6) possíveis combinações para associar os interruptores às lâmpadas.")
    print(
        "Dessa forma, com apenas duas idas para verificar, a probabilidade de acerto por tentativa aleatória é baixa.")
    print("Para resolver o problema de forma sistemática, siga estas etapas:")

    input("Pressione Enter para continuar...")

    print("1. Ligue o Interruptor A e deixe-o ligado por cerca de 10 minutos.")
    print("2. Após 10 minutos, desligue o Interruptor A e ligue o Interruptor B.")
    print("3. Vá até as salas para verificar as lâmpadas:")

    input("Pressione Enter para continuar...")

    print("   a) Se uma lâmpada estiver acesa, ela é controlada pelo Interruptor B.")
    print("   b) Se uma lâmpada estiver apagada, mas quente ao toque, ela é controlada pelo Interruptor A.")
    print("   c) A lâmpada que está apagada e fria ao toque é controlada pelo Interruptor C.")
    print("Com essas informações, você conseguirá identificar qual interruptor controla cada lâmpada.")

    input("Pressione Enter para finalizar.")
    input()
    print("Se você for até a sala 1 e estiver ligada, você sabe que é a A ou B")
    input()
    print("Volta, e desliga a A, e deixa a B ligada por um tempo. ")


else:
    print("Opção inválida.")