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

## Como usar esse repositório:
- É necessário **clonar** esse repositório e abrir ele em uma ferramenta de desenvolvedor como o Visual Studio
- No terminal do **Linux** ou no **WSL**, instalar **miniconda** com o seguinte código:
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh bash Miniconda3-latest-Linux-x86_64.sh
```
- Ativar o **miniconda**:
```
source ~/miniconda3/bin/activate
```
- Configurar os canais:
```
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge 
```
- Verifique-se de que o **pip** está instalado no seu terminal rodando o comando:
```
pip --version
```
- Em seguida, pode iniciar a **instalação** e **inicialização** dos **programas** necessários para a montagem. Para isso, segue o passo a passo do arquivo ```instalacao.sh```
- O próximo passo é rodar os comandos nos arquivos ```montagem.sh``` e ```var_medaka.sh``` da mesma maneira como feito anteriormente. Em ```montagem.sh```, há aluns códigos em comentários, isso é porque a parte de anotação utlilizando Prokka ainda não foi desenvolvida. O programa ainda funciona normalmente para realizar a montagem em si. *Não se esqueça de alterar os primeiros comandos em ```var_medaka.sh``` de acordo com o seu organismo* 
- Como isso feito, 

## Contato:
katherine.b@aluno.ifsp.edu.br

luiza.souza@aluno.ifsp.edu.br
