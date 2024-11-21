# x-hec-agent

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
```

Install requirements.txt

```bash
pip install -r requirements.txt
```

Create a .env file with the following content:

```bash
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

## Run

```bash
fastapi dev main.py
```
