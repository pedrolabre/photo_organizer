# Photo Organizer

Organizador e analisador de coleções de fotos: escaneia diretórios, calcula hashes, extrai metadados, detecta duplicatas e fornece ferramentas para organizar e auditar sua biblioteca.

<!-- BADGES -->
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](#license)

Resumo rápido
- Código principal em `src/` — lógica de scanner, detecção e organização.
- Interface web mínima em `app.py` (Flask) para inspeção dos resultados.
- Scripts em `scripts/` geram relatórios em `output/reports/`.

## Sumário

- [Recursos](#recursos)
- [Pré-requisitos](#pré-requisitos)
- [Instalação rápida](#instalação-rápida)
- [Execução](#execução)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Fluxos principais](#fluxos-principais)
- [Desenvolvimento](#desenvolvimento)
- [Boas práticas](#boas-práticas)
- [Licença](#licença)

## Recursos

- Varredura recursiva de diretórios com coleta de metadados EXIF
- Cálculo de hashes e detecção de duplicatas exatas
- Movimentação controlada de arquivos (organização / quarentena)

## Pré-requisitos

- Python 3.10 ou superior
- Recomendado: criar um ambiente virtual

## Instalação rápida

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux / macOS:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Execução

1) Rodar a interface web (dashboard):

```powershell
.\venv\Scripts\Activate.ps1
python app.py
# abra http://localhost:5000 no navegador
```

2) Usar a CLI principal (scaneia e popula o banco):

```powershell
.\venv\Scripts\Activate.ps1
python main.py --path "C:\Fotos" --db data/database/photo_organizer.db
```

## Estrutura do projeto

- `src/` — implementação principal (scanner, detectores, organização)
- `app.py` — pequena aplicação Flask para inspeção
- `main.py` — runner/CLI
- `scripts/` — utilitários de relatórios e empacotamento
- `data/` — banco de dados e caches locais (não versionar)
- `output/` — artefatos gerados (relatórios, organizados, quarantine)
- `docs/` — documentação e guias (conteúdo versionado)

## Fluxos principais

- Scan → coleta de metadados e hashes → persistência no DB
- Detecção de duplicatas → marcação/movimentação para `output/quarantine/`
- Relatórios CSV/JSON/HTML para auditoria e integração

## Desenvolvimento

- Executar testes (quando houver):

```bash
pytest -q
```

- Formatação / lint (opcional):

```bash
pip install -r requirements-dev.txt
black .
flake8
```

## Boas práticas

- Não versionar artefatos gerados localmente: `output/`, `data/logs/`, `__pycache__/`, `venv/`.

## Contribuição

1. Abra uma issue descrevendo a proposta.
2. Crie um branch com prefixo `feature/` ou `fix/`.
3. Envie um Pull Request com descrição clara e testes, se aplicável.

## Licença

MIT — consulte o arquivo `LICENSE` para detalhes.

