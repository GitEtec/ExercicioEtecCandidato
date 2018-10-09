from random import choice
'''
1) Existe 3 vagas para o senado.Serão computados 50 votos, sendo:
a - Candidato 1
b - Candidato 2
c - Candidato 3
d - Candidato 4
e - Voto Branco
f - Voto Nulo
Exiba
a- os canditados vencedores e seus numeros de votos
b- numeros de voto em branco
c- numer de voto nulos
d- a porcentagem de votos para cada candidato
'''

print('a - BolsoGato ')
print('b - Hajade    ')
print('c - Celso RussoMano ')
print('d - Ciro Comes ')
print('e - Voto Branco')
print('f - Voto Nulo')
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
for i in range(1,50+1):
    cad = ['a','b','c','d','e','f']
    if choice(cad) == 'a':
        a +=1
    elif choice(cad) == 'b':
        b +=1
    elif choice(cad) == 'c':
        c +=1
    elif choice(cad) == 'd':
        d +=1
    elif choice(cad) == 'e':
        e +=1
    else:
        f +=1

pa = (a / 50)*100
pb = (b / 50)*100
pc = (c / 50)*100
pd = (d / 50)*100

if a == b == c:
    print('Empatou')
elif a > b and a > c and a > d:
    print(f'BolsoGato Mais votado! ')
elif b > a and b > c and b >d:
    print(f'Hajade Mais votado!')
elif c > a and c > b and c > d:
    print('Celso RussoMano Mais votado!')
elif d > a and d > b and d >c:
    print('Ciro Comes Mais votado!')



print(f'Porcentagem BolsoGato ({pa:.0f}%)')
print(f'Porcentagem Hajade ({pb:.0f}%)')
print(f'Porcentagem Celso RussoMano ({pc:.0f}%)')
print(f'Porcentagem Ciro Comes ({pd:.0f}%)')
print(f'Branco {e}')
print(f'Nulos {f}')



