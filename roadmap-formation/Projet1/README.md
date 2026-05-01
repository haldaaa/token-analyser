# Token Analyzer CLI

Outil CLI Python pour analyser un texte et estimer le coût d'un appel LLM.

## Features

- Compte caractères, mots, et tokens
- Supporte 2 tokenizers : `cl100k_base` (GPT-4) et `o200k_base` (GPT-4o)
- Estime le coût d'appel pour : GPT-4o, GPT-4o-mini, Claude Sonnet, Claude Haiku, ou local (Ollama)
- Lecture depuis `--text` ou `--file`

## Installation

```bash
git clone https://github.com/haldaaa/<nom-de-ton-repo>.git
cd <nom-de-ton-repo>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Analyser un texte direct
python token_analyzer.py --text "Hello world"

# Analyser un fichier
python token_analyzer.py --file mon-document.txt

# Choisir le modèle (pour le calcul de coût)
python token_analyzer.py --text "Hello" --model gpt-4o-mini

# Choisir le tokenizer
python token_analyzer.py --text "Hello" --tokenizer o200k_base
```

## Sortie exemple