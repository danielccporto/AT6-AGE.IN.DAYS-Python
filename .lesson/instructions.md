<p align="center">
    <img src="assets/logo_infnet.png" width="70" height="70" />
</p>

# *Assessment*

## Exercício 6

**Atenção:**
- É importante que você desenvolva o programa totalmente, do início ao fim, na IDE do Replit (**AQUI MESMO!!**⚠️**NÃO crie um repl no seu perfil do Replit para fazer o Assessment**⚠️). Você **NÃO** deve escrever o código em outra IDE e depois copiá-lo para cá.
- **NÃO** é permitido usar nenhum recurso que não faça parte do conteúdo desta disciplina, a menos que explicitamente autorizado no enunciado.
- Use comentários para explicar o que cada parte do código faz.
- Após concluir as tarefas, submeta suas soluções aqui e no Moodle (postando lá os links para seus projetos do Replit).

Neste exercício, você deverá criar uma nova versão do programa do Exercício 1, alterando a funcionalidade "Listar todos os cadastros" de um sistema de cadastro de dados pessoais conforme a descrição a seguir.

## Descrição das funcionalidades

### Listar todos os cadastros

Além dos dados contidos no cadastro (ID, nome, CPF e data de nascimento), deve ser apresentada uma nova informação: a idade **em dias** da pessoa correspondente.

A idade em dias calculada deve ser a real, ou seja, o nº exato de dias decorridos entre a data de nascimento da pessoa e a data em que o programa estiver sendo executado. Portanto, além de levar em consideração o nº de dias de cada mês do ano, o programa deverá levar em consideração a ocorrência de **anos bissextos**. 😉

*Observações:*

- O arquivo main.py já contém a definição de uma variável chamada `hoje` (armazenando a data em que o programa é executado) e instruções sobre como usá-la.
- **NÃO** é permitido usar nenhum recurso do módulo datetime além do que está indicado nas instruções de uso.
- As regras para determinar se um ano é bissexto podem ser encontradas em https://pt.wikipedia.org/wiki/Ano_bissexto#Calend%C3%A1rio_Gregoriano (se olharem bem esse artigo da Wikipédia, pode ser que encontrem mais coisa útil #ficaadica 🤐).
- Você pode verificar se seu programa está calculando corretamente a idade em dias, comparando o resultado com o desse site: https://www.contadordedias.com.br/contador-de-dias/calcular-idade
- As máquinas virtuais do Replit estão no fuso-horário UTC (pois estão no Reino Unido). Por isso, se você estiver no Brasil, o programa estará algumas horas adiantado, podendo ocasionar uma diferença de 1 dia em relação ao valor esperado da idade, dependendo da hora de execução.