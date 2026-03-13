# Automação de Processamento de NFs em PDF

Projeto desenvolvido em Python para automatizar a leitura, extração e processamento de dados de notas fiscais em PDF, com registro estruturado em planilha Excel.

## Objetivo

O objetivo desta automação é reduzir o trabalho manual envolvido no tratamento de notas fiscais, realizando de forma automática:

- leitura dos arquivos PDF;
- identificação do número da nota fiscal;
- extração dos itens da NF;
- validação dos dados extraídos;
- inserção das informações em planilha Excel;
- controle de notas já processadas;
- organização dos arquivos processados.

## Impacto Operacional

A automação proporcionou um **ganho operacional de aproximadamente 3 horas** no processo, reduzindo etapas manuais repetitivas e aumentando a eficiência da rotina.

### Ganhos observados

- Redução do tempo de processamento em cerca de 3 horas
- Menor esforço operacional manual
- Redução do risco de erro humano no preenchimento da planilha
- Maior padronização no tratamento das notas fiscais
- Estrutura preparada para evolução e reutilização em outros modelos de documento

## Arquitetura do Projeto

O projeto foi estruturado com foco em organização, separação de responsabilidades e possibilidade de evolução futura, seguindo uma abordagem modular inspirada em princípios como:

- SOLID
- Clean Architecture
- Separation of Concerns

### Estrutura de pastas

```bash
AUTOMACAO-PROCESSAMENTO-NFS-PDFS/
├── app/
│   ├── application/
│   ├── domain/
│   ├── infrastructure/
│   └── presentation/
├── config/
├── data/
├── docs/
├── tests/
├── main.py
├── requirements.txt
└── README.md
