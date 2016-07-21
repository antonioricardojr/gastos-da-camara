
#!/usr/bin/python
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

'''O Script abaixo faz o merge entre duas tabelas levando o nome do deputado em consideração'''

import unicodedata

def remove_accents(data):
    return unicodedata.normalize('NFD', unicode(data)).encode('ascii','ignore')

f1 = open("siconv_emenda.csv","r") #Tabela que tem os dados do deputado sem o ID
f2 = open("deputados_id.csv","r") #Tabela com o ID do deputado

readlines1 = f1.readlines()
readlines2 = f2.readlines()


for lines in readlines1:
    if "NOME_PARLAMENTAR" not in lines:
        nome_urna = remove_accents(lines.split(";")[4].lower().replace('\"',"")).lower()
        if len(nome_urna) == 0:
            continue
        for lines2 in readlines2:
            if "txNomeParlamentar" not in lines2:
                nome_dpt = remove_accents(lines2.split(",")[0].lower().replace('\"',"")).lower()
                id_dpt = remove_accents(lines2.split(",")[1].lower().replace('\"',"")).lower()
                if  nome_urna in nome_dpt:
                        print lines.strip() +";" + id_dpt


# for lines in readlines1:
#     if "nome_cand" not in lines:
#         nome_urna = remove_accents(lines.split(",")[7].lower().replace('\"',"")).lower()
#         nome_cand = remove_accents(lines.split(",")[6].lower().replace('\"',"")).lower()
#         uf = remove_accents(lines.split(",")[1].lower().replace('\"',"")).lower()
#         pt = remove_accents(lines.split(",")[8].lower().replace('\"',"")).lower()
#         for lines2 in readlines2:

#             if "txNomeParlamentar" not in lines2:
#                 nome_dpt = remove_accents(lines2.split(",")[0].lower().replace('\"',"")).lower()
#                 id_dpt = remove_accents(lines2.split(",")[1].lower().replace('\"',"")).lower()
#                 sgPT = remove_accents(lines2.split(",")[2].lower().replace('\"',"")).lower()
#                 sgUF = remove_accents(lines2.split(",")[3].lower().replace('\"',"")).lower()
#                 # print sgUF, uf
#                 # print sgUF.strip() == uf.strip()

#                 if  nome_urna in nome_dpt and sgPT == pt and  sgUF.strip() == uf.strip():
#                     # if pt == sgPT and uf == sgUF:
#                         print lines.strip() + "," + id_dpt
#                 elif nome_urna.strip() == nome_dpt.strip():
#                 		print lines.strip() + "," + id_dpt
        #         try:
        #             nome2 = remove_accents(lines2.split(",")[7].lower().replace('\"',"")).lower()
        #             nome3 = remove_accents(lines2.split(",")[6].lower().replace('\"',"")).lower()
        #             # print nome1,nome2
        #             # print nome1 in nome2
        #             if  nome1 in nome2 or nome1 in nome3:
        #                 print lines.strip() + "," + lines2
        #         except IndexError:
        #             continue
        # f2.seek(0)

# for line1 in f1.readlines():
#     if "txNomeParlamentar" not in line1:
#         nome_urna = line1.split(",")[4]
#         f2.seek(0)
#         for line2 in f2.readlines():
#             if "nome_urna_cand" not in line2:
#                 nome_parlamentar = line2.split(",")[7]
#                 print remove_accents(nome_parlamentar).lower(), nome_urna.lower()
#                 if  remove_accents(nome_urna).lower() in remove_accents(nome_parlamentar).lower():
#                     print line1 + "," + line2


    

