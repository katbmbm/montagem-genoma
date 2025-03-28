# Rodar os seguintes comandos no terminal (WSL, se estiver no Windows):

create -n assembly python=3.9 flye -y
conda activate assembly
flye --version

# Instalar Medaka
conda install medaka -y
medaka --version
conda deactivate
conda create -n ambienteMedaka python=3.8 -y
conda activate ambienteMedaka
conda config --add channels defaults conda config --add channels bioconda conda config --add channels conda-forge conda install medaka INSTALAR MEDAKA
medaka --version

# Instalar Prokka
conda deactivate
conda create -n ambienteProkka python=3.9 -y
conda activate ambienteProkka
conda install -c bioconda prokka
prokka --version
conda deactivate
python --version
pip install --upgrade pip

# Instalar Seqkit
conda create -n ambienteSeqkit python=3.9 -y
conda activate ambienteSeqkit
git clone https://github.com/autor-do-projeto/seqkit.git
cd seqkit
pip install seqkit --help
conda deactivate

# Instalar Quarto
conda create -n ambienteQuarto python=3.9 -y
conda activate ambienteQuarto
conda install -c conda-forge quarto
quarto --version
conda deactivate
