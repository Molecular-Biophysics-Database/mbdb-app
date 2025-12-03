from typing import Dict


def slug(text: str) -> str:
    """Convert text into a filesystem-safe slug."""
    if not text:
        return "unknown"

    t = "".join(c.lower() if c.isalnum() else "-" for c in text)
    while "--" in t:
        t = t.replace("--", "-")
    return t.strip("-")


def build_pdf_filename(record_dict: Dict, pid_value: str) -> str:
    """Create PDF filename: <method>_<pid>_<creator>_<title>.pdf"""

    md = record_dict.get("metadata", {})
    gp = md.get("general_parameters", {})

    # Method
    # extract and slugify method string
    raw_method = gp.get("method", "") or "unknown-method"
    method = slug(raw_method)

    method_prefix_map = {
        "microscale-thermophoresis-temperature-related-intensity-change-mst-tric": "mst",
        "bio-layer-interferometry-bli": "bli",
        "surface-plasmon-resonance-spr": "spr",
        "isothermal-titration-calorimetry-itc": "itc",
        "mass-phonometry-mp": "mp"

    }
    prefix = method_prefix_map.get(method, method)

    # --- TITLE ---
    record_info = gp.get("record_information", {})
    raw_title = record_info.get("title", "") or "untitled"
    title = slug(raw_title)

    # Depositor
    depositors = gp.get("depositors", {})
    depositor = depositors.get("depositor", {})

    raw_depositor = f"{depositor.get('given_name', '')} {depositor.get('family_name', '')}".strip()
    if not raw_depositor:
        raw_depositor = "unknown"

    depositor = slug(raw_depositor)

    # Assemble filename
    return f"{prefix}_{pid_value}_{depositor}_{title}.pdf"
