# Rodar os seguintes comandos:

npstudy=NP001_all_reads_combined_assembly
nanopore_run_directory=~/nanopore_assembly/NP001_all_reads_combined
barcode_numbers=({01..15})
barcodes=( "${barcode_numbers[@]/#/barcode}")
outdir=~/nanopore_assembly/$npstudy

conda activate assembly 

mkdir $outdir
for i in ${barcodes[@]}
  do 
  mkdir $outdir/flye_out/$i -p 
  cat $nanopore_run_directory/$i/*.fastq.gz > $outdir/$i.fastq.gz
  flye --nano-raw $outdir/$i.fastq.gz --out-dir $outdir/flye_out/$i --threads 20 
done 

conda deactivate
conda activate ambienteMedaka

export TF_FORCE_GPU_ALLOW_GROWTH=true
for i in ${barcodes[@]}
  do 
  mkdir  $outdir/flye_out/$i/medaka_consensus/
  medaka_consensus -i $outdir/$i.fastq.gz -d $outdir/flye_out/$i/assembly.fasta -o $outdir/flye_out/$i/medaka_consensus/ -t 20 -m r1041_e82_260bps_hac_g632 -b 70
done

for i in ${barcodes[@]}
  do 
  sed "s/>/>$i\//I" $outdir/flye_out/$i/medaka_consensus/consensus.fasta > $outdir/flye_out/$i/medaka_consensus/consensus.named.fasta
done

# Anotação Prokka (precisa ser mais desenvolvida)
# conda deactivate
# conda activate ambienteProkka
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
#conda activate ambienteSeqkit
#for i in ${codigos_barras[@]} 
#  do 
#  seqkit fx2tab -nl $diretorio_saida/$i.fastq.gz > $diretorio_saida/$i.comprimento_leituras.txt
#done

quarto render ~/nanopore_assembly/nanopore_report_template.qmd -P $npstudy
mv ~nanopore_assembly/nanopore_report_template.html $outdir/nanopore_report_template.html
