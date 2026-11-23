import pytest
from src.a1_triage import (
    results_to_csv, 
    build_report, 
    CSV_COLUMNS,
    decision_counts, 
    gene_summary, 
    impact_counts, 
    rank_variants, 
    classify_variant
)

# --- YOUR TESTS (Outputs & Integration) ---

SAMPLE_RESULT = [
    {
        "variant": "v1", "gene": "BRCA1", "chrom": "1", "pos": "100", 
        "ref": "A", "alt": "T", "depth": "10", "quality": "80", 
        "impact": "high", "decision": "prioritize", "reason": "priority gene BRCA1 with high impact"
    },
    {
        "variant": "v2", "gene": "MYC", "chrom": "2", "pos": "200", 
        "ref": "C", "alt": "G", "depth": "5", "quality": "50", 
        "impact": "low", "decision": "exclude", "reason": "low depth: observed 5 is below 10"
    }
]

def test_results_to_csv_header():
    """Test that the CSV string starts with the correct header and has no spaces after commas."""
    csv_text = results_to_csv(SAMPLE_RESULT)
    lines = csv_text.splitlines()
    assert lines[0] == ",".join(CSV_COLUMNS)

def test_results_to_csv_newlines():
    """Test that every line ends with a newline."""
    csv_text = results_to_csv(SAMPLE_RESULT)
    assert csv_text.endswith("\n")
    assert len(csv_text.splitlines()) == 3 # Header + 2 rows

def test_build_report_contains_thresholds():
    """Test that the report contains the thresholds from params."""
    params = {"min_depth": 10, "min_quality": 75, "priority_genes": ["BRCA1", "TP53"], "top_k": 2}
    report = build_report(SAMPLE_RESULT, params)
    assert "Thresholds: min_depth=10 min_quality=75" in report
    assert "Priority genes: BRCA1, TP53" in report

def test_build_report_invalid_empty():
    """Test that the report handles an empty list of variants gracefully."""
    params = {"min_depth": 10, "min_quality": 75, "priority_genes": ["BRCA1"], "top_k": 5}
    report = build_report([], params)
    assert "Variants: 0" in report
    assert "prioritize: 0" in report
    assert "Top 5 variants" in report


# --- AINUR'S TESTS (Summaries & Ranking) - Fixed function names ---

PARAMS = {"min_depth": 20, "min_quality": 30, "priority_genes": ["BRCA1"], "top_k": 3}

def test_decision_and_impact_counts():
    rows = [
        {"decision": "prioritize", "impact": "high"},
        {"decision": "review", "impact": "moderate"},
        {"decision": "exclude", "impact": "high"},
    ]
    assert decision_counts(rows) == {"prioritize": 1, "review": 1, "exclude": 1}
    assert impact_counts(rows) == {"high": 1, "moderate": 1, "low": 0, "modifier": 0}

def test_gene_summary_normal():
    rows = [
        {"gene": "TP53", "decision": "prioritize", "depth": 30},
        {"gene": "BRCA1", "decision": "review", "depth": 20},
        {"gene": "BRCA1", "decision": "exclude", "depth": 25},
    ]
    res = gene_summary(rows)
    assert list(res.keys()) == ["BRCA1", "TP53"]
    assert res["BRCA1"]["mean_depth"] == 22.5

def test_boundary_below_threshold():
    v = {"gene": "BRCA1", "depth": "19", "quality": "50", "impact": "high"}
    assert classify_variant(v, PARAMS)[0] == "exclude"

def test_boundary_at_and_above_threshold():
    v_at = {"gene": "BRCA1", "depth": "20", "quality": "30", "impact": "high"}
    v_above = {"gene": "BRCA1", "depth": "21", "quality": "31", "impact": "high"}
    assert classify_variant(v_at, PARAMS)[0] == "prioritize"
    assert classify_variant(v_above, PARAMS)[0] == "prioritize"

def test_awkward_messy_text():
    rows = [{"decision": "review", "impact": "  HIGH  "}]
    assert impact_counts(rows)["high"] == 1

def test_awkward_empty_list():
    assert decision_counts([]) == {"prioritize": 0, "review": 0, "exclude": 0}
    assert gene_summary([]) == {}

def test_awkward_k_larger_than_data():
    rows = [{"gene": "BRCA1", "decision": "prioritize", "quality": "90", "depth": "50", "pos": "100", "impact": "high"}]
    assert len(rank_variants(rows, 10)) == 1

def test_invalid_negative_k():
    """At least one invalid-input test with pytest.raises."""
    with pytest.raises(ValueError):
        rank_variants([], -1)