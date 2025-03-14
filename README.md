# Montagem de Genoma Bacteriano
## Introdução:

A seguir está um _pipeline_ computacional usado para realizar a montagem automática de genomas bacterianos, criado por Katherine Bilsland Marchesan e Luiza Rodrigues de Souza no Instituto Federal de São Paulo (IFSP), Campus Campinas.

Para desenvolver o projeto, usamos como base os códigos disponíveis no seguinte repositório:
**https://github.com/baynec2/nanopore_pipelines**

## Indicações:
- Para melhores resultados, recomendamos realizar a quantificação do DNA para assegurar a concentração ideal
- Além de utilizar o _Ligation Sequencing Kit_ da Oxford Nanopre para a geração de dados brutos de alta quantidade
- Recomendamos executar a montagem em um computador com **no mínimo 32GB** de memória **RAM**
- O _pipeline_ foi desenvolvido para ser executado no **Linux** ou no Windows. Se usar o Windows, é necessário instalar e ativar o **WSL** (Windows Subsistema para Linux)

## Instruções:
- No terminal do **Linux** ou no **WSL**, instalar **miniconda**, copiando e colando o seguinte código:
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh bash Miniconda3-latest-Linux-x86_64.sh
```
- Roda o seguinte comando para ativar o **miniconda**:
```
source ~/miniconda3/bin/activate
```
- Depois, utilize esses comandos para configurar os canais:
```
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge 
```
- Verifique-se de que o **pip** está instalado no seu terminal rodando o comando:
```
pip --version
```
### Determinando a qualidade dos _reads_ com fastp:
Recomenda-se fazer a avaliação da qualidade dos seus dados brutos antes da montagem, para verificar se há a quantidade de bases o suficiente para prosseguir.
- Primeiramente, instale o fastp apertando [aqui](https://github.com/OpenGene/fastp), seguindo as instruções no repositório
- Com o fastp instalado, roda o seguinte comando no seu terminal, realizando as devidas substituições:
```
fastp -i diretório1 -h diretório2 -j /dev/null -w 16
```
> Subistitua ```diretório1``` pelo local dos reads (dados brutos a testar) na sua máquina\
> Subistitua ```diretório2``` pelo local onde deseja salvar o arquivo output (.html)\
> Caso necessário, subistitua ```16``` pelos nucleos de processamento da sua maquina
- Abra o aquivo output .html para obter os resultadados da avaliação

### A montagem:
- Para a montagem, usamos o Canu. Para realizar sua instalação, aperta [aqui](https://github.com/marbl/canu)
- Com o Canu devidamente instalado, roda o seguinte comando no mesmo terminal, realizando novamente, as substituições:
```
canu maxThreads=16 useGrid=false -p nome -d diretório1 genomeSize=11m maxInputCoverage=100 -nanopore diretório2
```
> Caso necessário, subistitua ```16``` pelos nucleos de processamento da sua maquina\
> Subistitua ```nome``` pelo nome desejada da sua amostra. Ele será o output\
> Subistitua ```diretório1``` pelo local onde deseja salvar o output\
> Opcionalmente, subistitua ```11m``` pelo tamanho do genoma de referência (NCBI)\
> Subistitua ```diretório2``` pelo local dos reads (.FASTQ) na sua máquina

### Avaliando a qualidade da montagem:
- Por último, podemos avaliar a qualidade da montagem usando o QUAST. Aperte [aqui](https://github.com/ablab/quast) para realizar sua instalação.
- Após sua instalação, roda o seguinte comando no seu terminal:
```
quast.py diretório1 -r diretório2 -o diretório3
```
> Subistitua ```diretório1```   pelo local do arquivo .contigs.fasta da montagem do genoma\
> Subistitua ```diretório2``` pelo genoma de referência do ncbi\
> Subistitua ```diretório3``` pelo local onde deseja salvar o arquivo output
- Abra o aquivo output para obter os resultados da avaliação da qualidade

## Observações:
- Para a montagem de uma bactéria, o tempo de execução esperado é de 7 a 12 horas. **Não** é recomendado usar a maquina para realizar outras tarefas durante esse tempo.
- O aquivo de saída será **.config.fasta**

## Contato:
katherine.b@aluno.ifsp.edu.br

luiza.souza@aluno.ifsp.edu.br
