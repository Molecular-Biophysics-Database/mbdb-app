def request_title(topic):
    """The deposition's title and pid, shown instead of the request type's name."""
    info = topic.metadata.get("general_parameters", {}).get("record_information", {})
    title = (info.get("title") or "").strip() or "Untitled record"
    return f"{title} ({topic['id']})"
