# Arquitetura do Photo Organizer

Esta página descreve a estrutura de pastas, o fluxo de dados e as decisões arquiteturais do projeto.

## Estrutura de Pastas

photo_organizer/
├── src/                          # Código-fonte principal
│   ├── __init__.py
│   ├── core/                     # Funcionalidades centrais
│   │   ├── __init__.py
│   │   ├── file_scanner.py       # Busca arquivos de imagem
│   │   ├── metadata_reader.py    # Lê EXIF e metadados
│   │   ├── hash_calculator.py    # Calcula hashes para duplicatas
│   │   └── image_analyzer.py     # Análise visual (futuro)
│   
│   ├── detection/                # Detecção de duplicatas
│   │   ├── __init__.py
│   │   ├── exact_duplicates.py   # Duplicatas idênticas (hash)
│   │   └── similar_detector.py   # Duplicatas suspeitas (futuro)
│   
│   ├── organization/             # Organização de arquivos
│   │   ├── __init__.py
│   │   ├── folder_organizer.py   # Cria estrutura de pastas
│   │   └── file_mover.py         # Move arquivos com segurança
│   
│   ├── database/                 # Persistência de dados
│   │   ├── __init__.py
│   │   ├── db_manager.py         # Gerencia SQLite
│   │   └── models.py             # Estruturas de dados
│   
│   └── utils/                    # Utilitários diversos
│       ├── __init__.py
│       ├── logger.py             # Sistema de logs
│       ├── config.py             # Configurações globais
│       └── validators.py         # Validações de entrada
 
├── data/                         # Dados locais (não versionar)
│   ├── database/                 # Banco de dados SQLite
│   ├── logs/                     # Arquivos de log
│   └── cache/                    # Cache temporário

├── output/                       # Saída organizada
│   ├── organized/                # Fotos organizadas
│   ├── quarantine/               # Duplicatas suspeitas
│   │   └── groups/               # Grupos de duplicatas
│   └── reports/                  # Relatórios JSON

├── tests/                        # Testes unitários
│   ├── __init__.py
│   └── test_*.py                 # Arquivos de teste

├── docs/                         # Documentação
│   ├── setup.md                  # Guia de instalação
│   └── architecture.md           # Arquitetura detalhada

├── requirements.txt              # Dependências Python
├── config.yaml                   # Configuração do usuário
├── .gitignore                    # Arquivos ignorados
└── main.py                       # Ponto de entrada do sistema

## Fluxo de Dados (simplificado)

[Fontes] → [Scanner] → [Metadata Reader] → [Hash Calculator]
                                              ↓
                                    [Database Storage]
                                              ↓
                          [Duplicate Detection] → [Quarantine]
                                              ↓
                          [Organization Logic] → [Organized Folders]
                                              ↓
                                    [Reports & Logs]

## Tecnologias e Bibliotecas

- Python 3.9+ (recomendado 3.11/3.12)
- Pillow (PIL) — processamento de imagens e EXIF básico
- piexif — leitura/escrita EXIF completa (GPS etc.)
- imagehash — hashes perceptuais para duplicatas similares
- PyYAML — leitura de `config.yaml`
- tqdm — barras de progresso
- python-magic-bin (Windows) — detecção segura de tipo de arquivo

## MVP - Funcionalidades Mínimas

O MVP deve implementar:

- Escanear uma pasta e listar todas as imagens
- Ler EXIF básico (data, câmera, resolução)
- Calcular hash MD5 de cada arquivo
- Detectar duplicatas exatas (mesmo hash)
- Salvar metadados no SQLite
- Organizar fotos por ano/mês em pastas
- Mover duplicatas para quarentena com relatório JSON
- Gerar log de todas as operações

## Observações de Projeto

- Começar com duplicatas exatas (hash) e persistência SQLite acelera validação.
- Deixar a detecção de similares e análise visual para v2.
- Testes automatizados e scripts de teste (ex.: `test_metadata_reader.py`) ajudam a validar o pipeline incrementalmente.

---

Arquivo gerado em: 2025-12-16
