# Uma possível solução
```python
from datetime import date

# A variável "hoje" contém a data de hoje.
# Para o dia do mês, use:  hoje.day
# Para o mês, use:         hoje.month
# Para o ano, use:         hoje.year
hoje = date.today()

# Armazenamento dos cadastros
nomes = []
cpfs = []
nascimentos = []

# Lista com nº de dias de cada mês
DIAS_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Se não há nenhum cadastro, imprime mensagem informando
if len(nomes) == 0:
  print('Nenhum cadastro')
else:
  # Para cada cadastro...
  for i in range(len(nomes)):
    # Imprime os dados do cadastro
    print()
    print('ID:', i + 1)
    print('Nome:', nomes[i])
    print('CPF:', cpfs[i])
    print('Data de nascimento:', nascimentos[i])
  
    # Separa e converte os campos da data de nascimento
    dia_nasc = int(nascimentos[i][:2])
    mes_nasc = int(nascimentos[i][3:5])
    ano_nasc = int(nascimentos[i][6:])
  
    # Calcula a idade da pessoa em dias
    # Inicializa a contagem de dias em zero
    dias = 0
  
    # Para cada ano desde o nascimento da pessoa...
    for ano in range(ano_nasc, hoje.year + 1):
      # Define o 1º mês a ser contado no ano
      mes_inicial = 1
  
      # Se for ano de nascimento, começa a contar do mês de nascimento
      if ano == ano_nasc:
        mes_inicial = mes_nasc
        
      # Define o último mês a ser contado no ano
      mes_final = 12
      
      # Se for ano em que estamos, conta até o mês em que estamos
      if ano == hoje.year:
        mes_final = hoje.month
        
      # Para cada mês a ser contado neste ano...
      for mes in range(mes_inicial, mes_final + 1):
        # Se forem o ano e o mês em que estamos, soma o dia de hoje
        if ano == hoje.year and mes == hoje.month:
          dias += hoje.day
        else:
          # Senão, soma o nº de dias do mês
          dias += DIAS_MES[mes - 1]
  
          # Se for fevereiro e o ano for bissexto, soma mais 1 dia
          if (mes == 2 and 
              (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0))):
            dias += 1
        
        # Se forem o ano e o mês de nascimento, subtrai o dia de nascimento
        if ano == ano_nasc and mes == mes_nasc:
          dias -= dia_nasc
          
    # Imprime a idade em dias
    print('Idade em dias:', dias)
```