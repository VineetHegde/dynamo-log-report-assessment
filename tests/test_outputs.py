import json
from pathlib import Path

def test_criterion_1():
    """1. The report must be saved to `/app/report.json`."""
    assert Path("/app/report.json").exists(), "no report.json found"

def test_criterion_2():
    """2. The JSON report must contain the key `total_requests` matching the total number of requests."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("total_requests") == 6, "Incorrect total_requests"

def test_criterion_3():
    """3. The JSON report must contain the key `unique_ips` matching the count of unique IP addresses."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("unique_ips") == 3, "Incorrect unique_ips"

def test_criterion_4():
    """4. The JSON report must contain the key `top_path` matching the most frequently requested path."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("top_path") == "/index.html", "Incorrect top_path"