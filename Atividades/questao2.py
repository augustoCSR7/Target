def fibonacci(n):
    fibonacci_seq = [0, 1]
    
    # calcula até o número n
    while fibonacci_seq[-1] < n:
        next_fibonacci = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_fibonacci)
    
    # verifica se o número pertence à sequência
    if n in fibonacci_seq:
        return True
    else:
        return False

# função para verificar se um número pertence à Fibonacci e imprimir uma mensagem informando
def verificar_pertencimento(numero):
    if fibonacci(numero):
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."


numero_informado = int(input("Digite o número: "))
print(verificar_pertencimento(numero_informado))
