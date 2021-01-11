"""
15/11/2020
O programa vai receber, nome e inserir numa lista.
Será essa lista, que ira validar se a pessoa já votou ou não, para só assim contar votos únicos.
No programa terá 3 partidos diferentes: Partido1, Partido2, Partido3.
Após o inserção do nome, o programa terá que validar se há ou não o nome da lista, e caso já houver,
Exibir a mensagem, ja votou.
Em seguida, solicitará um novo nome, e fará a mesma verificação.
Sendo negativo o o nome na lista, o programa permitirá o voto para 1 partido.

A cada 2 votos, eu quero que conte +1 para o partido3.
Mostre no final a quantidade de votos unicos, a quatidade de votos para cada um dos partidos.

O programa não terá limite de pessoas. Questionando se há mais eleitor. Sendo positivo, o loop recomeça.
Lembrar de citar que a constituição fala que o voto é secreto.

* IMPORTANTE RODRIGO! Verificar a lei do voto secreto, e verificar também o que é necessário para mudar
a constituição.

Segundo site: https://www.camara.leg.br/noticias/21921-como-se-altera-a-constituicao-federal/

Tentaram invadir o sistema em são paulo, em noticia em 21:24h na band.
"""
print('-'*100)
print('{:^100}'.format('PROGRAMA VOTO EM CASA'))
print('-'*100)
listacpf = []
voto_branco = voto_nulo = candidato1 = candidato2 = total_votos = 0
candidato3 = 1
while True:
    cpf = str(input('Nome do Eleitor: '))
    if cpf not in listacpf:
        listacpf.append(cpf)
        print('-=' * 20)
        print('{:^40}'.format('LISTA DE CANDITADO'))
        print('[1]: Para Candidato 1!\n[2]: Para Candidato 2!\n[3]: Para Candidato 3!\nOU\n'
              '[0] Para Anular\n[00] Voto em Branco!')
        print('{:^40}'.format('SEU VOTO'))
        voto = int(input('Informe seu Cadidadto-> '))
        total_votos += 1
        if total_votos % 2 == 0:
            candidato3 += 1
        if voto == 0:
            voto_nulo += 1
        elif voto == 00:
            voto_branco += 1
        elif voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        print('VOTO COMPUTADO COM SUECESSO')
        print('-=' * 20)
    else:
        print('FRAUDE! VOCÊ JA VOTOU!')
    r = str(input('Novo Eleitor? [S/N]: '))
    print()
    if r in 'Ss':
        print('{:^40}'.format('NOVO ELEITOR'))
        print('-=' * 20)
    else:
        break
print(f'Qtd de votos computados: {total_votos}')
print(f'Qtd de votos Candidato 1: {candidato1}')
print(f'Qtd de votos Candidato 2: {candidato2}')
print(f'Qtd de votos Candidato 3: {candidato3}')
