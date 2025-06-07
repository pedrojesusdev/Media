print('*'*30)
print("""Vamos verificar seu Boletim!
Digite abaixo suas notas para 
calcularmos a média e saber se 
você está aprovado ou não.""")
print('*'*30)
n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
if (n1 + n2) / 2 >= 7:
    print('Parabéns!! Você está aprovado!')
elif (n1 + n2) / 2 >= 5 and (n1 + n2) / 2 <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('REPROVADO')
