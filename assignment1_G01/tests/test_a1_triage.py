import pytest
from src.a1_triage import results_to_csv, build_report, CSV_COLUMNS

# sample row
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