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

O Git é necessário para baixar (clonar) este repositório.

#### Linux (Ubuntu / Debian / Mint)
```bash
sudo apt update
sudo apt install -y git
```

#### macOS
```bash
# Instale o Homebrew se ainda não tiver: https://brew.sh
brew install git
```

#### Windows
1. Acesse [git-scm.com/download/win](https://git-scm.com/download/win)
2. Baixe e execute o instalador
3. Mantenha todas as opções padrão e clique em **Next** até concluir

Verifique a instalação:
```bash
git --version
# Esperado: git version 2.x.x
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
2. Baixe o instalador da versão **3.11 ou superior**
3. Execute o instalador e marque a opção **"Add Python to PATH"** antes de instalar
4. Clique em **Install Now**

Verifique a instalação:
```bash
python --version
# Esperado: Python 3.11.x ou superior
```

---

### Passo 4 — Criar um Ambiente Virtual

Ambiente virtual isola as dependências do projeto sem afetar o sistema.

```bash
# Dentro da pasta clonada
python3 -m venv .venv

# Ative o ambiente virtual
# Linux / macOS:
source .venv/bin/activate

# Windows (Prompt de Comando):
.venv\Scripts\activate.bat

# Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

Quando ativado, o terminal mostrará `(.venv)` no início da linha.

> **Importante:** ative o ambiente virtual toda vez que for trabalhar no treinamento.

---

### Passo 5 — Instalar as Dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

---

### Passo 6 — Registrar o Ambiente no Jupyter

```bash
python -m ipykernel install --user --name=treinamento --display-name "Python (Treinamento)"
```

---

### Passo 7 — Abrir o Jupyter Lab

```bash
jupyter lab
```

O navegador abrirá automaticamente em `http://localhost:8888`.
Navegue até a pasta `python/` e abra o notebook desejado começando pelo `nivel_1.ipynb`.

> Se o navegador não abrir automaticamente, copie o link com o token que aparece no terminal.

---

## Verificação da Instalação

Execute o script abaixo para confirmar que tudo está funcionando:

```bash
python verificar_instalacao.py
```

---

## Solução de Problemas Comuns

### `python` não reconhecido no Windows
Use `python` em vez de `python3`. Se ainda não funcionar, reinstale o Python marcando **"Add Python to PATH"**.

### `git` não reconhecido no Windows
Feche e reabra o terminal após instalar o Git.

### Erro de permissão no Linux ao instalar pacotes
Não use `sudo pip install`. Sempre use o ambiente virtual conforme o Passo 4.

### PowerShell bloqueia o `.ps1` no Windows
Execute no PowerShell como administrador:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Porta 8888 já em uso
```bash
jupyter lab --port=8889
```

### Kernel não aparece no Jupyter
Repita o Passo 6 com o ambiente virtual ativado.

---

## VS Code (alternativa ao Jupyter Lab)

1. Instale o [VS Code](https://code.visualstudio.com/)
2. Instale a extensão **Python** (Microsoft)
3. Instale a extensão **Jupyter** (Microsoft)
4. Abra qualquer arquivo `.ipynb` — o VS Code abre nativamente como notebook
5. Selecione o kernel **"Python (Treinamento)"** no canto superior direito

---

## Desinstalar / Limpar

```bash
# Desative o ambiente virtual
deactivate

# Remova o ambiente virtual
rm -rf .venv          # Linux / macOS
rmdir /s /q .venv     # Windows
```
