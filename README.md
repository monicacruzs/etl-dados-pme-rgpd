
# 🚀 Desafio de Projeto DIO: Reimaginação de Pipeline ETL com Python

  ## 🎯 Objetivo do Projeto
  Este projeto tem como objetivo principal **reimaginar** a estrutura de um pipeline ETL (Extração, Transformação, Carga), conforme proposto no desafio, aplicando conceitos de Python e Pandas em um novo domínio de aplicação: o processamento de dados tabulares (como faturas ou documentos fiscais). O foco é demonstrar a capacidade de limpeza, padronização e estruturação de dados.

## ⚙️ Arquitetura do Pipeline

A solução foi desenvolvida seguindo o fluxo ETL tradicional, utilizando ferramentas open-source:

| Fase | Ferramenta Principal | Função no Projeto |
| :--- | :--- | :--- |
| **E - Extração** | **JSON** (Simulado) | Simula a ingestão de dados brutos (e sujos) extraídos de documentos por um serviço de OCR (como o AWS Textract ou Azure Document Intelligence). |
| **T - Transformação** | **Pandas** | Realiza a limpeza dos dados, tratando valores nulos, padronizando formatos de texto e convertendo tipos de dados (e.g., texto para float). |
| **L - Carga (Load)** | **CSV** | Carrega os dados transformados para um arquivo final (`output.csv`), simulando o carregamento em um Data Mart ou Data Warehouse para análise. |

## 🛠️ Tecnologias Utilizadas
* **Python:** Linguagem principal para desenvolvimento.
* **Pandas:** Biblioteca fundamental para a manipulação e limpeza de dados na fase de **Transformação**.
* **Luigi (Opcional - Futuro):** Framework de orquestração para gerenciar a dependência entre as etapas E, T e L
* 
## 💡 Como Executar
1.  Clone este repositório.
2.  Instale o Pandas (`pip install pandas`).
3.  Execute o script principal (`python etl_pipeline.py`).
4.  O resultado será salvo no arquivo `data/output.csv`.
