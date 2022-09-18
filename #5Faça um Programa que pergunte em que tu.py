#4 Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

periodo = input('Informe qual período você estuda, digite M para matutino, V para Vespertino ou N para Noturno: ')

if periodo == 'M':
    print("Bom dia!")
elif periodo == 'V':
    print('Boa Tarde!') 
elif periodo == 'N':
    print('Boa Noite!')
else:
    print('Valor inválido')

    