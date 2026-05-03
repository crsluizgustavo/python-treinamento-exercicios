"""
Verifica se todas as dependências do treinamento estão instaladas corretamente.
Execute: python verificar_instalacao.py
"""
import sys
import shutil

OK   = "  [OK]"
FAIL = "  [ERRO]"

erros = 0


def checar(label, fn):
    global erros
    try:
        resultado = fn()
        print(f"{OK}  {label}{' — ' + resultado if resultado else ''}")
    except Exception as e:
        print(f"{FAIL} {label} — {e}")
        erros += 1


print("\n=== Verificação do Ambiente — Treinamento Python ===\n")

# Python
checar(
    f"Python {sys.version.split()[0]}",
    lambda: "OK" if sys.version_info >= (3, 10) else (_ for _ in ()).throw(
        RuntimeError("Python 3.10+ necessário")
    ),
)

# Biblioteca padrão
for modulo in ["csv", "json", "logging", "pathlib", "dataclasses",
               "functools", "contextlib", "abc", "collections"]:
    checar(f"stdlib: {modulo}", lambda m=modulo: __import__(m) and None)

# Dependências externas
def checar_pandas():
    import pandas as pd
    return f"v{pd.__version__}"

def checar_numpy():
    import numpy as np
    return f"v{np.__version__}"

def checar_ipykernel():
    import ipykernel
    return f"v{ipykernel.__version__}"

checar("pandas",    checar_pandas)
checar("numpy",     checar_numpy)
checar("ipykernel", checar_ipykernel)

# VS Code
def checar_vscode():
    if shutil.which("code"):
        return "encontrado no PATH"
    raise RuntimeError(
        "VS Code não encontrado no PATH — instale em https://code.visualstudio.com\n"
        "         No Windows/macOS, marque 'Add to PATH' durante a instalação"
    )

checar("VS Code (code)", checar_vscode)

# Resumo
print()
if erros == 0:
    print("Tudo certo! Abra o projeto com: code .")
    print("Selecione o kernel 'Python (Treinamento)' ao abrir um notebook.\n")
else:
    print(f"{erros} problema(s) encontrado(s).")
    print("Siga o README.md para resolver.\n")

sys.exit(erros)
