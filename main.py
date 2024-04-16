from datetime import date

# A variável "hoje" contém a data de hoje.
# Para o dia do mês, use:  hoje.day
# Para o mês, use:         hoje.month
# Para o ano, use:         hoje.year
hoje = date.today()

# Mantenha as linhas acima no início do arquivo

nomes = []
cpfs = []
nascimentos = []
ID = []
dias = []
diasdoano = [31,28,31,30,31,30,31,31,30,31,30,31]
diastotais = 0
data = ""
CP = 0
cadastro = 0
data_ano = 0
data_dia = 0
ano_atual = 2024
mes_atual = 4
dias_ano_atual= 0 
quantidade_dias_total = 0 
diasanonasci = 0
data_mes = 0
diasatual = 12

#Comando para start do programa
nome = input("Digite seu nome ou digite a palavra (terminou) caso queira encerrar o programa: ")

#Loop para cadastro
while nome != "terminou":
  
  data = input("Digite sua data de nascimento (no formato dd/mm/aaaa): ")
  CP = input("Digite seu CPF: ")
  cadastro = input("Digite seu ID: ")

  #Separação de Dados 
  data_ano = data[6:]
  print(f"Dataano: {data_ano}")
  data_dia = data[:2]
  print(f"Datadia: {data_dia}")
  data_mes = data[3:5]
  print(f"Datames: {data_mes}")

  diastotais=0

  #For para período do ano nascido.
  for i in range (int(data_mes),13): 

    #Fevereiro
    if i == 2 : 
      if ano_atual % 4 == 0 or ano_atual % 1000 == 0:

        #Caso de aniversário
        if i == data_mes :
          diasanonasci = 29 - int(data_dia)
          
        else:
          diasanonasci= diasanonasci + 29

      else: 
        if i == data_mes:
          diasanonasci = 28 - int(data_dia)
        else:
          diasanonasci= diasanonasci + 28 
        
    elif i in [1,8]:
      if i % 2 == 0 :
        if i == data_mes:
          diasanonasci = 30 - int(data_dia)
          
        else:
          diasanonasci= diasanonasci + 30
          
      else : 
        if i == data_mes:
          diasanonasci = 31 - int(data_dia)
        
        else:
          diasanonasci = diasanonasci + 31
          
    elif i in [8,13]:
      
      if i % 2 == 0:
        if i == data_mes:
          diasanonasci = 31 - int(data_dia)
        else:                         
          diasanonasci = diasanonasci + 31
      
      else :
        if i == data_mes:
         diasanonasci = 30 - int(data_dia)
        else:
         diasanonasci= diasanonasci + 30
  
  for i in range(int(data_ano) + 1, 2024):
  
    if i % 4 == 0 or i % 1000 == 0: 
    
      diastotais = diastotais + 366
    
    else :
      diastotais = diastotais + 365
  
  for i in range (1,mes_atual): 
      
    if i == 2 : 
      if ano_atual % 4 == 0 or ano_atual % 1000 == 0:
        
        dias_ano_atual= dias_ano_atual + 29
          
      else: 
        dias_ano_atual= dias_ano_atual + 28 
          
    elif i in [1,8]: 
      if i % 2 == 0:
        dias_ano_atual= dias_ano_atual + 30
        
      else :
        dias_ano_atual= dias_ano_atual + 31
        
    elif i in [8,13]: 
      
      if i % 2 == 0:
        dias_ano_atual = dias_ano_atual + 31 
        
      else: 
        dias_ano_atual = dias_ano_atual + 30
      
  
  quantidade_dias_total = int(diastotais) + int(dias_ano_atual) + int(diasanonasci) + int(diasatual)
  
  nomes.append(nome)
  cpfs.append(CP)
  nascimentos.append(data)
  ID.append(cadastro)
  dias.append(quantidade_dias_total)
  
  nome = input("Digite seu nome ou digite a palavra (terminou) caso queira encerrar o programa: ")

for id in range(0, len(ID)):
  print(f"ID: {ID[int(id)]} Nome: {nomes[int(id)]} CPF: {cpfs[int(id)]} Data de nascimento: {nascimentos[int(id)]} Dias: {dias[int(id)]}")  

#print(f"O usuário {nome}, de CPF {CP}, do ID {ID}, nascido em {data}, viveu no total {quantidade_dias_total} dias.")
        
 
  


 