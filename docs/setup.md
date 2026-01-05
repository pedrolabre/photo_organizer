# Guia rápido de setup — Photo Organizer

Este guia mostra como criar o ambiente virtual, instalar dependências e executar os testes básicos no Windows (PowerShell) e em sistemas Unix (Linux/macOS).

## Requisitos
- Python 3.9+ (recomendado 3.11/3.12)
- `git` (opcional)

## 1) Criar e ativar o `venv` (Windows PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -V
```

No Windows (CMD):

```cmd
python -m venv venv
venv\Scripts\activate.bat
python -V
```

Em Unix (bash/zsh):

```bash
python3 -m venv venv
source venv/bin/activate
python -V
```

## 2) Atualizar `pip` e instalar dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3) Testes rápidos

- Executar o teste de leitura de EXIF:

```bash
venv\Scripts\python.exe test_metadata_reader.py
```

- Executar o pipeline MVP (`main.py`):

```bash
venv\Scripts\python.exe main.py
```

## 4) Resultado esperado
- `test_metadata_reader.py` imprimirá os metadados das primeiras imagens encontradas em `test_photos/`.
- `main.py` criará o banco em `data/database/photo_organizer.db`, moverá duplicatas para `output/quarantine/groups/` e salvará relatório em `output/reports/`.

## 5) Observações
- Se usar PowerShell e tiver restrições de execução de scripts, execute `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` antes de ativar o venv.
- Para análise em lote maior, ajuste `config.yaml` e execute `main.py` novamente.

---

Arquivo gerado em: 2025-12-16
