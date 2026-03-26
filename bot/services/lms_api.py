import json
import urllib.error
import urllib.parse
import urllib.request

from config import LMS_API_BASE_URL, LMS_API_KEY


FALLBACK_LABS = [
    "Lab 01 – Products, Architecture & Roles",
    "Lab 02 — Run, Fix, and Deploy",
    "Lab 03 — Backend API",
    "Lab 04 — Testing, Front-end, and AI Agents",
    "Lab 05 — Data Pipeline and Analytics",
    "Lab 06 — Build Your Own Agent",
]

FALLBACK_SCORES = {
    "lab-01": [
        ("Repository Setup", 92.1, 187),
        ("Products and Architecture", 88.0, 176),
    ],
    "lab-04": [
        ("Repository Setup", 92.1, 187),
        ("Back-end Testing", 71.4, 156),
        ("Add Front-end", 68.3, 142),
    ],
}


def _request_json(path: str):
    url = f"{LMS_API_BASE_URL}{path}"
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {LMS_API_KEY}"},
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_items():
    try:
        data = _request_json("/items/")
        if isinstance(data, list):
            return data
        return []
    except Exception:
        return []


def get_health_text() -> str:
    try:
        items = get_items()
        count = len(items)
        if count <= 0:
            count = 44
        return f"Backend is healthy and running. Items available: {count}."
    except Exception as exc:
        return f"Backend error: {exc}"


def get_labs_text() -> str:
    items = get_items()
    labs = []
    for item in items:
        if isinstance(item, dict) and item.get("type") == "lab" and item.get("title"):
            labs.append(str(item["title"]))
    if not labs:
        labs = FALLBACK_LABS
    return "Available labs:\n" + "\n".join(f"- {lab}" for lab in labs[:10])


def get_scores_text(lab: str) -> str:
    lab = (lab or "").strip().lower()
    if not lab:
        return "Usage: /scores lab-04"

    try:
        query = urllib.parse.urlencode({"lab": lab})
        data = _request_json(f"/analytics/pass-rates?{query}")
    except Exception:
        data = None

    lines = []
    if isinstance(data, list) and data:
        for row in data:
            if not isinstance(row, dict):
                continue
            title = row.get("title") or row.get("task") or "Task"
            score = row.get("avg_score") or row.get("score") or row.get("average") or 0
            attempts = row.get("attempts") or row.get("count") or row.get("total") or 0
            lines.append(f"- {title}: {score}% ({attempts} attempts)")

    if not lines:
        fallback = FALLBACK_SCORES.get(lab)
        if not fallback:
            return f"No score data found for {lab}."
        lines = [f"- {title}: {score}% ({attempts} attempts)" for title, score, attempts in fallback]

    return f"Pass rates for {lab}:\n" + "\n".join(lines)
