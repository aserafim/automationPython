# Capítulo 2 - Controle de Fluxo
# Autor: aserafim

'''
1 - Quais são os dois valores do tipo de dado booleano? Como eles são escritos?

Os valores permitidos para variáveis booleanas são True e False.


2 - Quais são os três operadores booleanos?

Os operadores booleanos são "and", "or" e "not".


3 - Escreva as tabelas verdade de cada operador booleano (ou seja, todas as 
combinações possíveis de valores booleanos para o operador e como elas são avaliadas).



4 - Para que valores as expressões a seguir são avaliadas?

(5 > 4) and (3 == 5)
A segunda expressão é falsa, portanto a resultante é False

not(5 > 4)
A expressão entre parênteses é verdadeira, quando aplica-se o not
ela resulta em False

(5 > 4) or (3 == 5)
Basta que uma expressão seja verdadeira. Como a primeira expressão
é verdadeira, então a resultante é True

not ((5 > 4) or (3 == 5))
A expressão entre parênteses é True, conforme o exercício anterior.
Ao aplicar o not, ela resulta em False

(True and True) and (True == False)
A primeira expressão é verdadeira e a segunda é falsa,
portanto o resultado é False

(not False) or (not True)
A primeira expressão é verdadeira, a segunda expressão é falsa,
portante o resultado é False



5 - Quais são os seis operadores de comparação?
== : Igual
!= : Diferente
> : Maior que
< : Menor que
>= : Maior ou igual que
<= : Menor ou igual que



6 - Qual é a diferença entre o operador “igual a” e o operador de atribuição?

O operador igual a (==) compara se o valor armazenado na variável a esquerda
é o mesmo armazenado na variável a direita do operador.

O operador de atribuição (=) atribui à variável a esquerda do operador,
o valor que está a direita do operador.



7. Explique o que é uma condição e quando você usaria uma.

Uma condição é um critério que precisa ser cumprido(ou não) a depender
da situação, para que a instrução seguinte seja executadda. 
Por exemplo, podemos pensar no limite de velocidade de uma
rodovia, que é 60Km/h e a regra estabelecida pelo DETRAN é de que,
se um veículo ultrapassar esse limite, deverá ser multado. Nesse cenário
a condição é que a velocidade seja superior a 60Km/h.

Em código a condição acima poderia ser escrita da seguinte forma:

multa = False
velocidade = 50.0

if(velocidade > 60.0):
    multa = True;



8. Identifique os três blocos no código a seguir:

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

Bloco 1:
    if spam > 5:
        print('bacon')

Bloco 2:
    else:
        print('ham')

Bloco 3:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')



9 - Escreva um código que exiba Hello se 1 estiver armazenado em spam, Howdy
se 2 estiver armazenado em spam e Greetings! se outro valor estiver
armazenado em spam.

spam = 1;
if (spam == 1):
    print("Hello!")
elif (spam == 2):
    print("Howdy!")
else:
    print("Greetings!")



10 - Que tecla você deve pressionar se o seu programa estiver preso em um loop infinito?

Pressionando ctrl + c o Python é encerrado.



11 - Qual é a diferença entre break e continue?

O break interrompe a execuçãod e um bloco de código, enquano o continue faz o 
contrário, continua a execução mesmo após uma condição ter ocorrido.



12 - Qual é a diferença entre range(10), range(0, 10) e range(0, 10, 1) em um loop
for?

Em termos de execução de código não há diferença. As três formas da função range
correspondem a mesma instrução.



13 - Crie um pequeno programa que mostre os números de 1 a 10 usando um
loop for. Em seguida, crie um programa equivalente que mostre os números
de 1 a 10 usando um loop while

numero = 1;
for i in range(0,10,1):
    print(numero);
    numero = numero + 1;


numero = 0;
while (numero < 10):
    print(numero + 1);
    numero = numero + 1;



14 - Se você tivesse uma função chamada bacon() em um módulo chamado
spam, como você a chamaria após ter importado spam?

Após realizar o import da função, bastaria chamá-la no código.

from spam import bacon

bacon();

'''



