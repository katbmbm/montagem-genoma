#rodar os seguintes comandos:
npstudy=NP001_all_reads_combined_assembly
nanopore_run_directory=~/nanopore_assembly/NP001_all_reads_combined
barcode_numbers=({01..13})
barcodes=( "${barcode_numbers[@]/#/barcode}")
# Entrar o caminho do diretório de saida desejada para o genoma montado
outdir=~/nanopore_assembly/$npstudy
# Usar um genoma de referência de acordo com a espécie de bactéria que será montada:
reference_fasta=~/nanopore_analysis/NP001_strep/Streptococcus_pneumoniae_ATCC_BAA_334.fasta

conda activate ambienteMedaka   
for i in ${barcodes[@]}
  do 
  medaka_haploid_variant -i $outdir/$i.fastq.gz -r $reference_fasta -o $outdir/flye_out/$i/medaka_variant/
done 
