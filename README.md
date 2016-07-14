# Dados de gastos dos deputados em csv

A Câmara dos Deputados publica dados abertos sobre os gastos das Cotas para Exercício da Atividade Parlamentar de nossos deputados. Porém esses dados são xmls enormes e inconvenientes para importar em ferramentas como R, que querem dados tabulares.

## Dependências

https://github.com/knadh/xmlutils.py

`pip install xmlutils` ou `easy_install xmlutils`

R, incluindo o pacote jsonlite.

`R -e 'install.packages("jsonlite", repos = "http://cran.rstudio.com/")'`

## Como obter os dados

Passo a passo semi automatizado para ir dos xml a csvs:

1. Baixe os xml que lhe interessam em <http://www2.camara.leg.br/transparencia/cota-para-exercicio-da-atividade-parlamentar/dados-abertos-cota-parlamentar> . Por exemplo, o ano atual está em <http://www.camara.gov.br/cotas/AnoAtual.zip>.

1. Descompacte

1. Converter de xml para json com xml2json. Por exemplo `xml2json --input AnoAtual.xml --output AnoAtual.json`

1. Use json2csv.R para transformar um ou mais arquivos json para um csv: por exemplo `./json2csv.R AnoAtual.json` ou `./json2csv.R AnoAtual.json AnoAnterior.json`

O resultado estará em `resultado.csv`

## Como entender os dados

Explicações sobre os campos resultantes:
http://www2.camara.leg.br/transparencia/cota-para-exercicio-da-atividade-parlamentar/explicacoes-sobre-o-formato-dos-arquivos-xml

## Alguns já processados

Em `dados`
