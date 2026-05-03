# Treinamento Python — Data Engineering Track

Treinamento completo de Python do básico ao avançado com foco em Data Engineering.
Desenvolvido para treinees sem experiência prévia em programação.

---

## Estrutura do Treinamento

| Notebook | Conteúdo |
|----------|----------|
| `nivel_1.ipynb` | Variáveis, tipos, operadores, strings, I/O |
| `nivel_2.ipynb` | Condicionais, loops, comprehensions |
| `nivel_3.ipynb` | Listas, tuplas, dicionários, sets |
| `nivel_4.ipynb` | Funções, lambda, recursão |
| `nivel_5.ipynb` | Orientação a Objetos, herança, encapsulamento |
| `nivel_6.ipynb` | Módulos, pathlib, CSV, JSON |
| `nivel_7.ipynb` | Exceções, logging, validação |
| `nivel_8.ipynb` | Decorators, generators, type hints |
| `nivel_9.ipynb` | pandas, numpy, pipeline ETL completo |

---

## Pré-requisitos

- Sistema operacional: **Windows 10/11**, **macOS 12+** ou **Linux (Ubuntu 20.04+)**
- Acesso à internet para baixar os pacotes
- Permissão para instalar programas

---

## Instalação — Passo a Passo

### Passo 1 — Instalar o Git

#### Linux (Ubuntu / Debian / Mint)
```bash
sudo apt update
sudo apt install -y git
```

#### macOS
```bash
brew install git
```

#### Windows
1. Acesse [git-scm.com/download/win](https://git-scm.com/download/win)
2. Baixe e execute o instalador com todas as opções padrão

Verifique:
```bash
git --version
```

---

### Passo 2 — Clonar o Repositório

```bash
git clone https://github.com/crsluizgustavo/python-treinamento-exercicios.git
cd python-treinamento-exercicios
```

---

### Passo 3 — Instalar o Python

#### Linux (Ubuntu / Debian / Mint)
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

#### macOS
```bash
brew install python
```

#### Windows
1. Acesse [python.org/downloads](https://www.python.org/downloads/)
2. Baixe a versão **3.11 ou superior**
3. Marque **"Add Python to PATH"** antes de instalar

Verifique:
```bash
python --version
```

---

### Passo 4 — Instalar o VS Code

1. Acesse [code.visualstudio.com](https://code.visualstudio.com/) e baixe o instalador
2. Execute e siga o instalador padrão
3. Abra o VS Code e instale as duas extensões abaixo:

**Extensão Python**
- Menu: `View → Extensions` (ou `Ctrl+Shift+X`)
- Pesquise: `Python`
- Instale a extensão da **Microsoft**

**Extensão Jupyter**
- Pesquise: `Jupyter`
- Instale a extensão da **Microsoft**

---

### Passo 5 — Criar um Ambiente Virtual

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows (Prompt de Comando)
python -m venv .venv
.venv\Scripts\activate.bat

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Quando ativado, o terminal mostrará `(.venv)` no início da linha.

> **Importante:** ative o ambiente virtual toda vez que for trabalhar no treinamento.

---

### Passo 6 — Instalar as Dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

---

### Passo 7 — Registrar o Ambiente no VS Code

```bash
python -m ipykernel install --user --name=treinamento --display-name "Python (Treinamento)"
```

---

### Passo 8 — Abrir o Projeto no VS Code

```bash
code .
```

Ou abra o VS Code manualmente em `File → Open Folder` e selecione a pasta `python-treinamento-exercicios`.

---

### Passo 9 — Abrir o Primeiro Notebook

1. No painel esquerdo, navegue até a pasta `python/`
2. Clique em `nivel_1.ipynb`
3. No canto superior direito do notebook, clique em **"Select Kernel"**
4. Escolha **"Python (Treinamento)"**
5. Execute a primeira célula com `Shift+Enter`

> **Dica:** no VS Code você pode selecionar parte do código dentro de uma célula e executar só aquela seleção com `Shift+Enter` — igual ao Databricks.

---

## Verificação da Instalação

```bash
python verificar_instalacao.py
```

---

## Solução de Problemas Comuns

### `python` não reconhecido no Windows
Reinstale o Python marcando **"Add Python to PATH"**.

### `git` não reconhecido no Windows
Feche e reabra o terminal após instalar o Git.

### Kernel "Python (Treinamento)" não aparece no VS Code
Repita o Passo 7 com o ambiente virtual ativado e reinicie o VS Code.

### PowerShell bloqueia o `.ps1` no Windows
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Erro de permissão no Linux ao instalar pacotes
Não use `sudo pip install`. Sempre use o ambiente virtual (Passo 5).
