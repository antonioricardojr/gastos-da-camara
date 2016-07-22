#!/usr/bin/python
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

import unicodedata

'''O script abaixo faz o merge entre duas tabelas levando em conta o nome do deputado.
Rode esse script logo após ter criado o dataset de deputados_id.csv'''

def remove_accents(data):
    return unicodedata.normalize('NFD', unicode(data)).encode('ascii','ignore')

f1 = open("B.EPP4-Observatory-Elites.xlsx.csv","r")
f2 = open("deputados_id.csv","r")

readlines1 = f1.readlines()
readlines2 = f2.readlines()

print "ano_eleicao,sigla_uf,estado,regiao,cargo_disput,tipo_cargo,nome_cand,nome_urna_cand,sig_part,nome_part,partidos_leg,nome_leg,ocupacao_declarada,ano_nasc,n_tit_eleitoral,id_data_eleicao,sexo,grau_instrucao,curso_super_dummy,est_civil,situacao_conjug,nacionalidade,sig_uf_nasc,mun_nasc,eleito_sim_ou_nao,tipo_eleito,cor,ideologia_simplificada,ideologia_partido,ideol_tamanho_part,indio_sim_nao,pardo_sim_nao,branco_sim_nao,preto_sim_nao,amarelo_sim_nao,id"

for lines in readlines1:
    if "nome_cand" not in lines:
        nome_urna = remove_accents(lines.split(",")[7].lower().replace('\"',"")).lower()
        nome_cand = remove_accents(lines.split(",")[6].lower().replace('\"',"")).lower()
        uf = remove_accents(lines.split(",")[1].lower().replace('\"',"")).lower()
        pt = remove_accents(lines.split(",")[8].lower().replace('\"',"")).lower()
        for lines2 in readlines2:

            if "txNomeParlamentar" not in lines2:
                nome_dpt = remove_accents(lines2.split(",")[0].lower().replace('\"',"")).lower()
                id_dpt = remove_accents(lines2.split(",")[1].lower().replace('\"',"")).lower()
                sgPT = remove_accents(lines2.split(",")[2].lower().replace('\"',"")).lower()
                sgUF = remove_accents(lines2.split(",")[3].lower().replace('\"',"")).lower()
                if nome_urna == nome_dpt :
                    print lines.strip() + "," + id_dpt
                elif  nome_urna in nome_dpt and sgPT == pt and sgUF.strip() == uf.strip():
                    print lines.strip() + "," + id_dpt
