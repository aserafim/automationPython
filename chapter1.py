# Capítulo 1 - Básico sobre Python
# Autor: aserafim

'''
1 - Quais das opções abaixo são operadores e quais são valores?
# operadores: * - / +
# valores : 'hello' -88.8 5


2 - Qual das opções a seguir é uma variável e qual é uma string?

spam - variável de nome spam
'spam' - valor que pode ser atribuído a qualquer variável do tipo string


3 - Nomeie três tipos de dados.

1 - int
2.0 - float
'texto' - string


4 - De que é composta uma expressão? O que fazem as expressões?

Uma expressão é composta de operadores, variáveis e chamadas de funções.
As expressões são utilizadas para dar instruições ao Python.


5 - Qual a diferença entre uma expressão e uma instrução?

Uma instrução é um comando, por exemplo print, que exibe um
valor na tela. Uma expressão é um conjunto de operadores, variáveis e 
chamadas de funções(instruções) que resultam em um valor.


6 - O que a variável bacon conerá após o código a seguir ser executado?

bacon = 20
bacon + 1

bacon conterá o valor 21



7 - Para que valores as duas expressões a seguir serão avaliadas?

'spam' + 'spamspam'
'spam' * 3

Nos dois casos o resultado será 'spamspamspam'



8 - Por que eggs é um nome válido de variável enqunto 100 é inválido?

O Python não pemite que variáveis sejam noemadas iniciando com um caractere
numérico.



9 - Quais três funções podem ser usadas para obter uma versão inteira de ponto flutuante
ou em string de um valor?

Supondo que numero seja a variável, temos:

int(numero)
float(numero)
str(numero)



10 - Por que a expressão a seguir causa um erro? Como podemos corrigi-la?
'I have eaten' + 99 + 'burritos.'

Ao executar a instrução acima o Python vai tentar realizar uma operação de 
adição com as expressões 'I have eaten' que é uma string e a expressão 99, 
que é um inteiro. Isso não é possível, portanto o Python retornará um erro.
Para corrigir o problema podemos reescrever a instrução como a seguir:

'I have eaten' + '99' + 'burritos.'

Ou ainda,

'I have eaten' + str(99) + 'burritos.'

'''