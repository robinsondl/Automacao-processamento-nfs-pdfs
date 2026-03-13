# Arquitetura do Projeto

## Objetivo
Automatizar a leitura de notas fiscais em PDF, extrair itens válidos e registrar essas informações em uma planilha Excel, evitando duplicidade e organizando os arquivos processados.

### Domain
Contém as entidades e regras centrais do negócio, como `NfItem`, `NfDocument` e `NfParserService`.

### Application
Contém os casos de uso da aplicação, como o processamento completo das NFs.

### Infrastructure
Contém as implementações técnicas, como leitura de PDF com `pdfplumber`, escrita em Excel com `openpyxl` e manipulação de arquivos locais.

### Presentation
Camada responsável por iniciar a aplicação via terminal.

## Benefícios da Estrutura
- Separação de responsabilidades
- Reutilização de componentes
- Facilidade de manutenção
- Facilidade para testes
- Possibilidade de suportar novos layouts de documentos no futuro

## Impacto Operacional

A automação do processamento de notas fiscais em PDF reduziu o tempo de execução da atividade em aproximadamente 3 horas, eliminando etapas manuais de leitura, validação e lançamento em planilha.

### Ganhos observados
- Redução do tempo de processamento em cerca de 3 horas
- Menor esforço operacional manual
- Redução de risco de erro humano no preenchimento da planilha
- Maior padronização no tratamento das notas fiscais