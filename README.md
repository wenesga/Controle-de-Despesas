# Controle-de-Despesas
Aplicativo em Python de Controle de Despesa Pessoal.

## Como executar

### 1) Pré-requisitos
- Python 3.10+
- `tkinter` instalado no sistema operacional

### 2) Criar ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Instalar dependências
```bash
pip install -r requirements.txt
```

### 4) Iniciar o app
```bash
python main.py
```

> O app já cria as tabelas automaticamente caso o banco não exista.

### 5) (Opcional) Criar banco manualmente
```bash
python criardb.py
```

## Observações
- O arquivo `dados.db` é o banco SQLite local usado pelo app.
- Se o banco já existir, **não** execute `criardb.py` novamente para evitar erro de tabela já existente.

## Capturas de tela

![ScreenShot_20230926103331](https://github.com/wenesga/Controle-de-Despesas/assets/13321239/816312c3-069c-4a90-b030-d990c370c1a9)

![ScreenShot_20230928110114](https://github.com/wenesga/Controle-de-Despesas/assets/13321239/1e33ed33-9e98-4eb2-964e-2ef83d181775)

![ScreenShot_20230929193832](https://github.com/wenesga/Controle-de-Despesas/assets/13321239/3d405741-5a31-4eb5-b176-f1dafdc82299)
