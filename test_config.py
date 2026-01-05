"""
Teste do módulo de configuração `src/utils/config.py`.

Execute este script (com o `venv` ativado) para validar o carregamento
e a validação das configurações.
"""

import sys
from pathlib import Path
from pprint import pprint

# Garantir que o projeto root está no path
sys.path.insert(0, str(Path(__file__).parent))

from src.utils.config import get_config


def main():
    print("TESTE DE CONFIGURAÇÃO")
    print("=" * 40)

    # Inicializar (carrega config.yaml)
    cfg = get_config("config.yaml")

    # Quantidade de pastas de entrada
    print(f"➡️  Pastas de entrada configuradas: {len(cfg.input_folders)}")
    for p in cfg.input_folders:
        print(f"   - {p} -> exists={p.exists()}")

    # Mostrar pastas de saída
    print(f"➡️  Pasta de saída: {cfg.output_folder} (exists={cfg.output_folder.exists()})")
    print(f"➡️  Pasta de quarentena: {cfg.quarantine_folder} (exists={cfg.quarantine_folder.exists()})")

    # Mostrar algumas configurações carregadas
    print("\nConfigurações principais:")
    print(f"  - Organização: {cfg.organization}")
    print(f"  - Duplicatas: {cfg.duplicates}")
    print(f"  - Segurança: {cfg.safety}")
    print(f"  - Performance: {cfg.performance}")
    print(f"  - Logging: {cfg.logging}")

    # Validação
    print("\nExecutando validação...")
    errors = cfg.validate()
    if not errors:
        print("✅ Validação OK — nenhuma inconsistência encontrada.")
    else:
        print("⚠️  Validação retornou avisos/erros:")
        for e in errors:
            print(f"   - {e}")

    # Exibir caminho do banco
    print(f"\nCaminho do banco de dados: {cfg.get_database_path()}")


if __name__ == "__main__":
    main()
"""
Teste do módulo config.py

Execute este arquivo para verificar se as configurações estão sendo carregadas corretamente.
"""

import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent))

from src.utils.config import get_config


def test_config():
    """Testa o carregamento de configurações."""
    
    print("=" * 60)
    print("TESTE DO SISTEMA DE CONFIGURAÇÃO")
    print("=" * 60)
    print()
    
    try:
        # Carregar configuração
        config = get_config()
        
        print("✅ Configuração carregada com sucesso!")
        print()
        
        # Exibir informações principais
        print("📋 INFORMAÇÕES DA CONFIGURAÇÃO:")
        print("-" * 60)
        print(f"📁 Pastas de entrada: {len(config.input_folders)}")
        for i, folder in enumerate(config.input_folders, 1):
            exists = "✅" if folder.exists() else "⚠️  (não existe)"
            print(f"   {i}. {folder} {exists}")
        
        print()
        print(f"📤 Pasta de saída: {config.output_folder}")
        print(f"🗑️  Quarentena: {config.quarantine_folder}")
        print()
        
        print(f"🖼️  Extensões suportadas: {len(config.supported_extensions)}")
        print(f"   {', '.join(config.supported_extensions[:10])}")
        if len(config.supported_extensions) > 10:
            print(f"   ... e mais {len(config.supported_extensions) - 10}")
        print()
        
        print(f"📂 Estrutura de organização: {config.organization.structure}")
        print(f"🔍 Detectar duplicatas exatas: {config.duplicates.detect_exact}")
        print(f"🔍 Detectar duplicatas similares: {config.duplicates.detect_similar}")
        print(f"🔒 Operação de arquivo: {config.safety.file_operation}")
        print(f"📊 Nível de log: {config.logging.level}")
        print()
        
        # Validar configuração
        print("-" * 60)
        print("🔍 VALIDANDO CONFIGURAÇÃO:")
        print("-" * 60)
        
        errors = config.validate()
        
        if errors:
            print("⚠️  Avisos encontrados:")
            for error in errors:
                print(f"   • {error}")
        else:
            print("✅ Todas as configurações são válidas!")
        
        print()
        print("-" * 60)
        print("✅ Teste concluído!")
        print()
        
        # Dicas
        if errors:
            print("💡 DICA: Edite o arquivo config.yaml para corrigir os avisos.")
            print()
        
    except FileNotFoundError as e:
        print("❌ ERRO:", e)
        print()
        print("💡 Certifique-se de que o arquivo config.yaml está na raiz do projeto.")
        print()
    except Exception as e:
        print("❌ ERRO inesperado:", e)
        print()


if __name__ == "__main__":
    test_config()
