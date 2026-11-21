# Design - Variant Triage Service

Write this BEFORE you write the code, then keep it up to date. It is marked by the lecturer.
Use your own words, your own thresholds and your own data. Delete the guidance in italics.

Group ID: <G01>      Thresholds from data/params.json: min_depth = <...>, min_quality = <...>, top_k = <...>

## 1. Decomposition

| Question | Our answer |
|---|---|
| Input |1. A list of variant dictionaries (`rows`) loaded from `data/variants.csv`, where each dictionary holds string values for `variant`, `gene`, `chrom`, `pos`, `ref`, `alt`, `depth`, `quality`, and `impact`.<br>2. A configuration dictionary (`params`) loaded from `data/params.json` containing `min_depth` (int), `min_quality` (int), `priority_genes` (list of gene symbol strings), and `top_k` (int).|

| Output |1. Classified variant records (`triage`) as a new list of new dictionaries containing all original fields plus `decision` and `reason` (without commas).<br>2. Summary dictionaries for `decision_counts`, `impact_counts` (excluding `exclude` variants), and alphabetical `gene_summary` (including `mean_depth` rounded to 1 decimal place).<br>3. A ranked list of top-k non-excluded variants (`rank_variants`).<br>4. Formatted CSV string (`results/triage.csv`) and plain-text summary report (`results/report.txt`). |

| Constraints (named thresholds, what happens at exactly the threshold) | |
| Rule order and why the order matters | |
| Out of scope | |

## 2. Pseudocode or flowchart of classify_variant

*Give either structured pseudocode (indentation, IF / ELSE, RETURN) or a flowchart (a picture file
committed in docs/ and linked here, or a Mermaid block). Show all six rules.*

depth <- CONVERT_TO_INT(row["depth"])
quality <- CONVERT_TO_INT(row["quality"])
gene_clean <- STRIP(row["gene"])
gene_norm <- CASEFOLD(gene_clean)
impact_norm <- CASEFOLD(STRIP(row["impact"]))

min_depth <- params["min_depth"]
min_quality <- params["min_quality"]
priority_set <- SET of CASEFOLD(STRIP(g)) FOR EACH g IN params["priority_gene"]
is_priority <- (gene_norm IN priority_set)

IF depth <- min_depth THEN
     RETURN("exclude", "Rule 1: low depth("+ depth + " <" + min_depth +")")
ELSE IF quality < min_quality THEN
     RETURN("exclude", "Rule 2: low quality(" + quality + " < " + min_quality + ")")
ELSE IF is_priority AND impact_norm IN {"low", "modifier"} THEN
     RETURN("prioritize","Rule 3: priority gene" + gene_clean + "with" + impact_norm + "impact")
ELSE IF is_priority AND impact_norm IN {"low", "modifier"} THEN
        RETURN ("review", "Rule 4: priority gene " + gene_clean + " with " + impact_norm + " impact")
ELSE IF (NOT is_priority) AND impact_norm IN {"high", "moderate"} THEN
        RETURN ("review", "Rule 5: non-priority gene " + gene_clean + " with " + impact_norm + " impact")
    ELSE
        RETURN ("exclude", "Rule 6: non-priority gene " + gene_clean + " with " + impact_norm + " impact")
    END IF
END FUNCTION

## 3. Hand trace

*Trace the first six rows of YOUR data/variants.csv (v1 to v6) with YOUR thresholds, then two more rows of
your choice that reach rules 3 to 6. Do it by hand BEFORE you run your code, then compare with your code.*

| Variant | Gene | Depth | Quality | Impact | Rule that fires | Decision |         Reason                                   |
|V1       |MYC   |9      |90       |Moderate|      rule1      |  exclude | Rule 1:low depth(9<10)                           | 
|V2       |MYC   |10     |90       |low     |      rule6      |  exclude | Rule 6:non-priority gene MYC with low impact     |
|V3       |ATM   |11     |90       |modifier|      rule4      |  review  | Rule 4:priority gene ATM with modifier impact    |
|V4       |APC   |30     |79       |moderate|      rule5      |  review  | Rule 5:non-priority gene APC with moderate impact|
|V5       |KRAS  |30     |80       |moderate|      rule5      |  review  | Rule 5:non-pririty gene KRAS with moderate impact|
|V6       |MYC   |30     |81       |modifier|      rule6      |  exclude | Rule 6:non-priority gene MYC with modifierimpact |
|V7       |PTEN  |33     |72       |low     |      rule2      |  exclude | Rule 2:low quality(72<75)                        |
|V8       |ATM   |78     |78       |moderate|      rule3      |prioritize| Rule 3:priority gene ATM with moderate impact    |


## 4. Test plan

Normal Cases:
-------------

Verify priority gene with high/moderate impact returns prioritize(Rule 3)
Priority gene with low/modifier returns review(Rule 4)
non-priority gene with high/moderate returns review(rule 5)
non-priority gene with low/modifier returns exclude(rule 6)

Boundary Cases(at group thresholds min_depth=10, min_quality=75):
------------------------------------------------------------------
Test depth=9 (rule1 exclude),depth=10 (passes depth QC),
depth=11(passes depth QC);test quality=74(Rule 2 exclude),
quality=75(passes quality QC), 
Quality=76(passes quality QC).

Rule precedence case:
---------------------
Test a priority gene variant with high impact where both depth=5 <10 and quality=50 < 75 to confirm rule 1(depth) fires first.

Immutability / pure function check: 
-----------------------------------
Confirm triage() and rank_variants() do not mutate the input list or inner dictionaries. 

Summary functions: 
-------------------
Verify decision_counts() and impact_counts() maintain exact key order including zero counts, and impact_counts() ignores exclude rows; verify gene_summary() sorts genes alphabetically and rounds mean_depth over all rows of a gene to 1 decimal place (returning {} on empty input).

Ranking & tie-breaking (rank_variants): 
---------------------------------------
Verify exclude variants are omitted, tie-breaking follows decision -> impact -> -quality -> -depth -> +pos, k=0 returns [], and k > len(candidates) returns all available candidates.

Awkward & invalid inputs:
--------------------------
 Test messy text (" brca1 ", " HIGH "), empty input lists [], and verify rank_variants(results, -1) raises ValueError using pytest.raises(ValueError).

## 5. Work plan

*Who builds which function, in which order, and how you will review each other's code.*
