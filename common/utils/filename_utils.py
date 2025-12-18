import re
import unicodedata
from typing import Dict


def strip_diacritics(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def slug(text: str) -> str:
    """Convert text into an ASCII, filesystem-safe slug (no diacritics)."""
    if not text:
        return "unknown"

    text = strip_diacritics(text).lower()

    text = re.sub(r"[^a-z0-9]+", "-", text)

    return text.strip("-") or "unknown"


def build_pdf_filename(record_dict: Dict, pid_value: str) -> str:
    """Create PDF filename: <method>_<pid>_<creator>_<title>.pdf"""

    md = record_dict.get("metadata", {})
    gp = md.get("general_parameters", {})

    raw_method = gp.get("method", "") or "unknown-method"
    method = slug(raw_method)

    method_prefix_map = {
        "microscale-thermophoresis-temperature-related-intensity-change-mst-tric": "mst",
        "bio-layer-interferometry-bli": "bli",
        "surface-plasmon-resonance-spr": "spr",
        "isothermal-titration-calorimetry-itc": "itc",
        "mass-phonometry-mp": "mp",
    }
    prefix = method_prefix_map.get(method, method)

    record_info = gp.get("record_information", {})
    raw_title = record_info.get("title", "") or "untitled"
    title = slug(raw_title)

    depositors = gp.get("depositors", {})
    depositor = depositors.get("depositor", {})

    raw_depositor = f"{depositor.get('given_name', '')} {depositor.get('family_name', '')}".strip() or "unknown"
    depositor_slug = slug(raw_depositor)

    return f"{prefix}_{pid_value}_{depositor_slug}_{title}.pdf"
