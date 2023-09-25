# O jogo madlib, consiste em estimular a criatividade através da gramática.

def barra():
    print('-' * 30)
barra()
print(f"{'Bem vindos ao MADLIBS':^30}\n{'Meu amigo famoso!':^30}")
barra()

dia_da_semana = input('Dia da semana: ')
sentimento = input('Sentimento: ')
data_especial = input('Data especial: ')
verbo1 = input('Verbo: ')
verbo2 = input('Verbo: ')
adj_diminutivo = input('Adjetivo no diminutivo: ')
local = input('Local: ')
verbo3 = input('Verbo: ')
substantivo = input('Substantivo: ')

madlib = f'Hoje é {dia_da_semana} e eu estou muito {sentimento}. Na verdade eu gostaria que fosse {data_especial} para que eu pudesse {verbo1} e {verbo2}\nTenho um amigo famoso, o {adj_diminutivo} e nós sempre vamos ao {local}. Quando estamos lá, nós gostamos de {verbo3} no {substantivo}'

print(madlib)



