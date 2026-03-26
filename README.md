# Boilerplate of Python Project

Python 專案樣板，內建 `src` 結構、`pytest` 測試設定與 Docker 打包流程。

## Quick Start

### 1) Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 3) Environment variables

此專案提供範本檔：`config/.env.template`。  
測試時會由 `pytest.ini` 自動載入此檔案（`--envfile config/.env.template`）。

若你要本機直接執行程式，可先複製一份：

```bash
cp config/.env.template .env
```

## Run Application

此專案 Docker 預設啟動指令為：

```bash
python -m proj.main
```

若在本機直接執行：

```bash
PYTHONPATH=src python -m proj.main
```

## Run Tests

執行全部測試：

```bash
pytest
```

只跑單元測試：

```bash
pytest -m unit
```

只跑整合測試：

```bash
pytest -m integration
```

## Docker Usage

### Build and run locally

```bash
bash ./scripts/build-and-run.bash
```

> 使用前請先依需求修改 `scripts/build-and-run.bash` 內的 `repo_name`。

### Build and push image

```bash
bash ./scripts/build_and_push.bash
```

> 使用前請先依需求修改 `scripts/build_and_push.bash` 內的 `tag`、`repo_name`、`registry_host`。

## Folder Structure

- `src/`: application source code
- `tests/`: test cases
- `docs/`: project documents
- `scripts/`: helper scripts for Docker build/run/push
- `config/`: environment variable templates

## Basic Requirements

Core packages:

- `pydantic`
- `pydantic[email]`
- `python-dotenv`
- `loguru`

Development packages:

- `pytest`
- `pytest-cov`
- `pytest-sugar`
- `pytest-html`
- `pytest-dotenv`
- `pytest-xdist`