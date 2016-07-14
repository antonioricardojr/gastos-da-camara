#!/usr/bin/env Rscript
# Os argumentos esperados são uma lista de arquivos .json
# A saída estará no arquivo resultado.csv
library(jsonlite)

args = commandArgs(trailingOnly = TRUE)
resultado = NULL
for (arquivo in args) {
  message("processando ", arquivo)
  anoAtualdf = fromJSON(arquivo, simplifyDataFrame = TRUE)
  d = anoAtualdf$orgao$DESPESAS$DESPESA
  if(is.null(resultado)){
    resultado = d
  } else {
    resultado = rbind(resultado, d)
  }
}

write.csv(resultado, "resultado.csv", row.names = FALSE)
