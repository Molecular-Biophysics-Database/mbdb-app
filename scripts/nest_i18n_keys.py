"""Convert flat i18n keys in model YAML files to the nested form oarepo-model 6 reads.

    label.en: Entities of interest        label:
    help.en: List of the entities   ->      en: Entities of interest
      that are ...                        help:
                                            en: List of the entities
                                              that are ...

oarepo-model 6 reads only `label: {en: ...}` (and `help`, `hint`). With the flat
`label.en:` keys the ui_model falls back to `{"und": "<field name>"}`.

The conversion is line based, so comments and formatting are kept. Every file is
checked afterwards: the converted file must parse to the original data with the
flat keys nested. On a mismatch the file is not written.

Usage: python scripts/nest_i18n_keys.py FILE.yaml [FILE.yaml ...]
"""

import re
import sys

import yaml

KEY = re.compile(r"^(?P<indent>\s*)(?P<name>label|help|hint)\.(?P<lang>[a-z]{2}):(?P<rest>.*)$")


def indent_of(line):
    return len(line) - len(line.lstrip(" "))


def convert_text(text):
    lines = text.splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        match = KEY.match(lines[i])
        if not match:
            out.append(lines[i])
            i += 1
            continue

        indent = match["indent"]
        # Siblings with the same prefix (label.en, label.cs) go under one key.
        name = match["name"]
        out.append(f"{indent}{name}:\n")
        while i < len(lines) and (match := KEY.match(lines[i])) and match["indent"] == indent and match["name"] == name:
            out.append(f"{indent}  {match['lang']}:{match['rest']}\n")
            i += 1
            # Continuation lines of a multi-line scalar are indented deeper
            # than the key; shift them along with it.
            while i < len(lines) and (not lines[i].strip() or indent_of(lines[i]) > len(indent)):
                if not lines[i].strip() and not _continues(lines, i, len(indent)):
                    break
                out.append("  " + lines[i] if lines[i].strip() else lines[i])
                i += 1
    return "".join(out)


def _continues(lines, i, indent):
    """A blank line belongs to the scalar only if a deeper-indented line follows."""
    for line in lines[i:]:
        if line.strip():
            return indent_of(line) > indent
    return False


def nest_expected(data):
    if isinstance(data, list):
        return [nest_expected(x) for x in data]
    if not isinstance(data, dict):
        return data
    result = {}
    for key, value in data.items():
        match = KEY.match(f"{key}:") if isinstance(key, str) else None
        if match:
            result.setdefault(match["name"], {})[match["lang"]] = value
        else:
            result[key] = nest_expected(value)
    return result


def main(paths):
    failed = False
    for path in paths:
        with open(path, encoding="utf-8") as f:
            original = f.read()
        converted = convert_text(original)
        if converted == original:
            print(f"{path}: nothing to convert")
            continue
        if yaml.safe_load(converted) != nest_expected(yaml.safe_load(original)):
            print(f"{path}: MISMATCH after conversion, file not written")
            failed = True
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(converted)
        count = sum(1 for line in original.splitlines() if KEY.match(line))
        print(f"{path}: converted {count} keys")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
