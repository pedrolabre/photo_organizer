# Photo Organizer

Organizador de fotos simples — scanner, cálculo de hashes, extração de metadata e organização em pastas. Este repositório contém o código-fonte, scripts de geração de relatórios e uma pequena interface web (Flask) para inspeção.

Status: trabalho em progresso. Documentação principal em `docs/`.

## Requisitos

- Python 3.10+ (testado com 3.14)
- Dependências listadas em `requirements.txt`

## Instalação (Windows - PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Uso

- Rodar a interface web (dashboard):

```powershell
# ativa o venv se necessário
.\venv\Scripts\Activate.ps1
python app.py
```

- Executar a ferramenta/CLI (gera banco e arquivos de saída):

```powershell
.\venv\Scripts\Activate.ps1
python main.py
```

- Gerar relatórios via script (offline):

```powershell
.\venv\Scripts\Activate.ps1
python scripts/generate_reports.py
```

Observação: os scripts gravam arquivos em `output/reports/` e movem/quarentenam duplicatas em `output/quarantine/`.

## Estrutura relevante

- `src/` — código fonte principal
- `app.py` — app Flask para dashboard
- `main.py` — runner/CLI que cria/usa `data/database/photo_organizer.db`
- `scripts/` — scripts utilitários (geração de relatórios, empacotamento)
- `output/` — diretório de saída gerado (relatórios, organizados, quarantine)
- `data/database/photo_organizer.db` — banco de dados SQLite usado pelo projeto
- `docs/` — documentação (manter)

## O que NÃO commitar

Arquivos gerados e caches que não pertencem ao código-fonte devem ser ignorados antes do commit. Sugestão mínima de `.gitignore`:

```
# Virtual environment
venv/

# Output and data
output/
data/logs/

# Python cache
__pycache__/
*.pyc

# Reports / generated artifacts
output/reports/
```

## Notas finais

- Já removi temporariamente logs e relatórios gerados do workspace local (conforme pedido). O banco `data/database/photo_organizer.db` foi mantido porque é usado pelo projeto.
- Se quiser, posso inicializar um repositório `git` local e criar o primeiro commit com o código e `docs/` limpos.
