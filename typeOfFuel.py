valorVerdade = True
alcool = 0
gasolina = 0
diesel = 0
while valorVerdade:
    choice = int(input())
    if choice == 1:
        alcool += 1
    elif choice == 2:
        gasolina += 1
    elif choice == 3:
        diesel += 1
    elif choice == 4:
        valorVerdade = False
print('MUITO OBRIGADO\n'
      'Alcool: {}\n'
      'Gasolina: {}\n'
      'Diesel: {}'.format(alcool, gasolina, diesel))