# Rodar os seguintes comandos:

estudo_np=NP001_todas_leituras_combinadas_montagem
diretorio_execucao_nanopore=~/montagem_nanopore/NP001_todas_leituras_combinadas
numeros_codigos_barras=({01..15})
codigos_barras=( "${numeros_codigos_barras[@]/#/codigo_barra}")
diretorio_saida=~/montagem_nanopore/$estudo_np

conda activate montagem 

mkdir $diretorio_saida
for i in ${codigos_barras[@]}
  do 
  mkdir -p $diretorio_saida/flye_out/$i 
  cat $diretorio_execucao_nanopore/$i/*.fastq.gz > $diretorio_saida/$i.fastq.gz
  flye --nano-raw $diretorio_saida/$i.fastq.gz --out-dir $diretorio_saida/flye_out/$i --threads 20 
done 

conda deactivate
conda activate medaka

export TF_FORCE_GPU_ALLOW_GROWTH=true

for i in ${codigos_barras[@]}
  do 
  mkdir $diretorio_saida/flye_out/$i/medaka_consenso/
  medaka_consensus -i $diretorio_saida/$i.fastq.gz -d $diretorio_saida/flye_out/$i/assembly.fasta -o $diretorio_saida/flye_out/$i/medaka_consenso/ -t 20 -m r1041_e82_260bps_hac_g632 -b 70
done

for i in ${codigos_barras[@]}
  do 
  sed "s/>/>$i\//I" $diretorio_saida/flye_out/$i/medaka_consenso/consensus.fasta > $diretorio_saida/flye_out/$i/medaka_consenso/consensus.nomeado.fasta
done

# Anotação Prokka (precisa ser mais desenvolvida)
# conda deactivate
# conda activate prokka
# for i in ${codigos_barras[@]}
#   do 
#   prokka $diretorio_saida/flye_out/$i/medaka_consenso/consensus.fasta --outdir $diretorio_saida/flye_out/$i/medaka_consenso/prokka
# done

conda deactivate

# Incluir esses comandos após a implementação do Prokka
# for i in ${codigos_barras[@]}
#  do 
#  ~/Desktop/Bandage image $diretorio_saida/flye_out/$i/assembly_graph.gfa $diretorio_saida/flye_out/$i/assembly_graph.jpg 
#done
#conda activate estatisticas_nanopore
#for i in ${codigos_barras[@]} 
#  do 
#  seqkit fx2tab -nl $diretorio_saida/$i.fastq.gz > $diretorio_saida/$i.comprimento_leituras.txt
#done

quarto render ~/montagem_nanopore/modelo_relatorio_nanopore.qmd -P $estudo_np
mv ~/montagem_nanopore/modelo_relatorio_nanopore.html $diretorio_saida/modelo_relatorio_nanopore.html
