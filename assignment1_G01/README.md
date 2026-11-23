# Variant Triage Service (SECB3203 Assignment 1)

All data are synthetic teaching data, not clinical data

## Group

- Group ID: G01
- Members: MUHAMMAD LUQMAN BIN MOHD AZMI (A24CS0138), ABDUL RASYID BIN ABD GHANI (A24CS0030), AINURRULNAJWA BINTI SAHLAN (A24CS0223)


## What this project does

This project implements a transparent, deterministic variant triage module for a clinical genomics teaching scenario. It reads synthetic variant calls from a CSV file alongside named quality-control thresholds and priority gene lists from a JSON parameter file, applying strict ordered rules to classify variants.

## Set up

```bash
python -m venv .venv
# Windows (PowerShell): .venv\Scripts\Activate.ps1
# Windows (Command Prompt): .venv\Scripts\activate.bat
# macOS / Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run

To run the program, use the following command from the root folder:

```
python src/a1_triage.py data/variants.csv data/params.json results
```

This will create a results/ folder containing two files: triage.csv and report.txt

## Test and lint

```
python -m pytest
ruff check src
```

## Our parameters

Our thresholds, priority genes and top_k are in data/params.json (min_depth = 10, min_quality = 75, top_k = 8).
They are read at run time and passed to the functions; they are not typed into the rules.

## Design

See docs/design.md for our decomposition table, pseudocode flowchart, and hand trace. It contains our logical plan for the triage rules before coding.

## Limitations

1. The rules only use depth, quality, impact, and the priority gene list; they do not consider actual genomic sequence context, inheritance patterns, or structural variants
2. The data is synthetic teaching data, so the triage results are not clinically actionable

## Who did what

| Member | Main contributions | Commits |
|---|---|---|
| Luqman | `results_to_csv, build_report, Git integration, README` | 12 |
| Rasyid | `classify_variant`,`triage`, boundary tests | 5 |
| Ainur | `decision_counts`, `impact_counts`, `gene_summary`, `rank_variants`, awkward tests | 9 |

## AI use

See AI_USE_LOG.md for full details. The group used AI (Level 1: Tutor) to help format the report strings, generate the Mermaid flowchart, and debug Git terminal errors.

