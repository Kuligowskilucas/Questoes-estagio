def verificar_fibonacci(numero):
    primeiro_valor = 0
    segundo_valor = 1

    while segundo_valor < numero:
        primeiro_valor, segundo_valor = segundo_valor, primeiro_valor + segundo_valor
    return segundo_valor == numero

def sequencia_fibonacci(numero):
    sequencia = []
    primeiro_valor = 0
    segundo_valor = 1

    while segundo_valor <= numero:
        sequencia.append(segundo_valor)
        primeiro_valor, segundo_valor = segundo_valor, primeiro_valor + segundo_valor
    return sequencia
    
    

valor_usuario = int(input('Digite o valor: '))

sequencia = sequencia_fibonacci(valor_usuario)
if valor_usuario in sequencia:
      print(f'O número {valor_usuario} pertence à sequência de Fibonacci.')
else:
    print(f'O número {valor_usuario} não pertence à sequência de Fibonacci.')