# Variant Triage Service (SECB3203 Assignment 1)

> Replace the text in this template. The README must let a stranger install, run and test the
> project with the exact commands below. All data are synthetic teaching data, not clinical data.

## Group

- Group ID: G01
- Members: MUHAMMAD LUQMAN BIN MOHD AZMI A24CS0138, ABDUL RASYID BIN ABD GHANI A24CS0030, AINURRULNAJWA BINTI SAHLAN  A24CS0223


## What this project does

<This project implements a transparent, deterministic variant triage module for clinical genomics teaching scenario. It reads synthetic variant calls from a CSV file alongside  named quality-control thresholds and priority gene lists from a JSON parameter file>

## Set up

python -m venv .venv
# Windows (PowerShell): .venv\Scripts\Activate.ps1
# Windows (Command Prompt): .venv\Scripts\activate.bat
# macOS / Linux: source .venv/bin/activate
pip install -r requirements.txt

## Run

<Write the exact command. The course command is: python src/a1_triage.py data/variants.csv data/params.json results>
<Say which files appear in results/.>

## Test and lint

```
python -m pytest
ruff check src
```

## Our parameters

Our thresholds, priority genes and top_k are in data/params.json (<write the values here>).
They are read at run time and passed to the functions; they are not typed into the rules.

## Design

<Link to docs/design.md and say in two sentences what it contains.>

## Limitations

<At least two honest limitations, for example: rules use depth, quality and impact only; the data are synthetic.>

## Who did what

| Member | Main contributions | Commits |
|---|---|---|
| <najuwaaaa> | <files or functions> | <number> |

## AI use

<One sentence: see AI_USE_LOG.md. Say whether the group used AI.>
