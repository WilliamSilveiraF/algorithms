tipo = input()
classe = input()
alimentacao = input()

if tipo == 'vertebrado' and classe == 'ave' and alimentacao == 'carnivoro':
    animal = 'aguia'
if tipo == 'vertebrado' and classe == 'ave' and alimentacao == 'onivoro':
    animal = 'pomba'

if tipo == 'vertebrado' and classe == 'mamifero' and alimentacao == 'onivoro':
    animal = 'homem'
if tipo == 'vertebrado' and classe == 'mamifero' and alimentacao == 'herbivoro':
    animal = 'vaca'


if tipo == 'invertebrado' and classe == 'inseto' and alimentacao == 'hematofago':
    animal = 'pulga'
if tipo == 'invertebrado' and classe == 'inseto' and alimentacao == 'herbivoro':
    animal = 'lagarta'

if tipo == 'invertebrado' and classe == 'anelideo' and alimentacao == 'hematofago':
    animal = 'sanguessuga'
if tipo == 'invertebrado' and classe == 'anelideo' and alimentacao == 'onivoro':
    animal = 'minhoca'
print('{}'.format(animal))