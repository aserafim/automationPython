#!/bin/bash
#Capítulo 2 do livro de automação
#Autor:aserafim

#9 - Escreva um código que exiba Hello se 1 estiver armazenado em spam, Howdy
#se 2 estiver armazenado em spam e Greetings! se outro valor estiver
#armazenado em spam.
SPAM=2

if [ $SPAM = 1 ]; then
    printf "Hello\n"
elif [ $SPAM = 2 ]; then 
    printf "Howdy \n\n"
else
    printf "Greetings!\n"
fi


#13 - Crie um pequeno programa que mostre os números de 1 a 10 usando um
#loop for. Em seguida, crie um programa equivalente que mostre os números
#de 1 a 10 usando um loop while
for i in {1..10..1}
do
    printf "$i\n"
done
printf "\n"

#Forma alternativa
for ((j=1; j<=10; j+=1))
do
    printf "$j\n"
done
printf "\n"

#Forma alternativa 2
for k in $(seq 1 1 10)
do
    printf "$k\n"
done

#Usando while
l=1;
while [ $l -le 10 ]; do
    printf "$l\n";
    l+=1;
done


