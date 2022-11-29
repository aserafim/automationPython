#!/bin/bash
# chapter1 - Primeiro capítulo com exercícios do curso de Python/Shell
# Autor: Alefe Serafim

# Pede uma confirmação do usuário para prosseguir com a chamada 
# dos comandos do sistema
printf "Vou buscar os dados do sistema.\nPara prosseguir digite s.
Para encerrar a execução digite n: \n"
read RESPOSTA

# Testa a resposta do usuário. Se for n ele encerra o script
test "$RESPOSTA" = "n" && exit

# Exibe a data e hora do sistema
printf "Data e horário:\n "
date

# Exibe o uso do disco
printf "\nUso do disco: \n"
df -khPT

# Exibe os usuários conectados
printf "\nUsuários conectados: \n"
w
