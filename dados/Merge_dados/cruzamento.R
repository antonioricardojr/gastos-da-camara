#!/usr/bin/env Rscript
library(dplyr)


ano.atual <- read.csv("~/Documentos/Didatica/ano-atual.csv")

#Criando um ID para cada deputado
deputados <- transform( ano.atual,id=as.numeric(factor(txNomeParlamentar)))

#Criando uma tabela com o deputado e seu ID
deputados_id <- select(deputados,txNomeParlamentar,id,sgPartido,sgUF) %>% group_by(txNomeParlamentar) %>% slice(c(1))

#Salvando a tabela anterior que será usada no script em Python.
write.table(deputados_id,file = "deputados_id.csv", sep = "," ,row.names = F)

#Eu criei um script em python pra atribuir o ID do deputado na mão (make_id.py). 
#Esse script usa deputados_id.csv e B.EPP4-Observatory-Elites.csv  
#No fim, eu salvei a saida do script com o comando abaixo no terminal
#python make_id.py > B.EPP4-Observatory-ElitesID.csv
#Rode o código abaixo apenas se tiver rodado o script em python

B.EPP4.Observatory.ElitesID <- read.csv("B.EPP4-Observatory-ElitesID.csv")

#Alguns deputados diferentes ficaram com ID's iguais porque o nome é muito parecido.
#Eliminando esses deputados vamos ficar com um total de 477 deputados validos, ou seja, que tem um ID em ambas as tabelas

B.EPP4.Observatory.ElitesID <- B.EPP4.Observatory.ElitesID %>% group_by(id) %>% mutate(z = length(unique(nome_urna_cand))) %>% filter(z == 1) %>% select(-z)
B.EPP4.Observatory.ElitesID <- B.EPP4.Observatory.ElitesID %>% group_by(id) %>% mutate(z = length(unique(nome_cand))) %>% filter(z == 1) %>% select(-z)

deputados_ids_temp <-  B.EPP4.Observatory.ElitesID %>% group_by(id) %>% filter(n()==1)

deputados_validos <- (filter(deputados, id %in% deputados_ids_temp$id))

#Escrevendo as tabelas com o ID de cada deputado. 
write.table(deputados_ids_temp, file = "deputados_dados_demograficos_id.csv", sep = ",", row.names = F) 
write.table(deputados_validos, file = "ano.atual_deputados_id.csv", sep = ",", row.names = F)
