def calculo(tempo, valor, juros):
    investimento = valor
    for i in range(tempo):
        investimento += investimento*juros
    return investimento

#-------------------------------------------
def lci(tempo, valor, juros):
    investimento= valor
    if tempo >= 6:
        investimento= calculo(tempo, valor, juros)
    return investimento
#--------------------------------------------
def cdb_deduzido(tempo,valor, juros):
    investimento = calculo(tempo, valor, juros)
    rentabilidade = investimento - valor
    if tempo <= 6:
        valor= investimento - (0.225* rentabilidade)
    elif tempo > 6 and tempo <= 12:
        valor = investimento - (0.2 * rentabilidade)
    elif tempo > 12 and tempo <= 24:
        valor = investimento - (0.175 * rentabilidade)    
    elif tempo > 24:
        valor = investimento - (0.15 * rentabilidade)
    return valor    
#---------------------------------------------
def comparacao(valor1, valor2, valor3):
    resp = ''
    if valor1 > valor2 and valor1 > valor3:
        resp = 'P'
    elif valor2 > valor1 and valor2 > valor3:
        resp = 'L'
    else:
        resp = 'C'
    return resp

#----------------------------------------------
info = [int(i) for i in input().split()]
valor = info[0]
tempo = info[1]
melhor = 0
investimento = ''
totalP= 0
totalL = 0
totalC = 0
juros_pop = 0.0059
juros_lci =0.0086
juros_cdb = 0.01032

totalP = calculo(tempo, valor, juros_pop)
totalL = lci(tempo, valor, juros_lci)
totalC = cdb_deduzido(tempo, valor, juros_cdb)
investimento = comparacao(totalP, totalL, totalC)

print('{:.2f}'.format(totalP))
print('{:.2f}'.format(totalL))
print('{:.2f}'.format(totalC))
print(investimento)
