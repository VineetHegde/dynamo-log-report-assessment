import json
from pathlib import Path

def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"

def test_report_schema_and_values():
    """The report file contains the correct keys and values."""
    data = json.loads(Path("/app/report.json").read_text())
    
    assert data.get("total_requests") == 6, "Incorrect total_requests"
    assert data.get("unique_ips") == 3, "Incorrect unique_ips"
    assert data.get("top_path") == "/index.html", "Incorrect top_path"