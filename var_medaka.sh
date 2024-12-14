#rodar os seguintes comandos:

estudo_np=NP001_todas_leituras_combinadas_montagem
diretorio_execucao_nanopore=~/montagem_nanopore/NP001_todas_leituras_combinadas
numeros_codigos_barras=({01..13})
codigos_barras=( "${numeros_codigos_barras[@]/#/codigo_barra}")
# Entrar o caminho do diretório de saida desejada para o genoma montado
diretorio_saida=~/montagem_nanopore/$estudo_np
# Usar um genoma de referência de acordo com a espécie de bactéria que será montada:
genoma_referencia=~/analise_nanopore/NP001_bacillus/Bacillus_velezensis_CATA_TTA_814.fasta

conda activate medaka   
for i in ${codigos_barras[@]}
  do 
    medaka_haploid_variant -i $diretorio_saida/$i.fastq.gz -r $genoma_referencia -o $diretorio_saida/flye_out/$i/medaka_variant/
done 