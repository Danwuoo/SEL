"""Utilities for writing log traces to disk."""

from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List

from .trace_schema import TaskTrace


def write_jsonl(trace: TaskTrace, path: str) -> None:
    """Append a trace as one JSON line to the given file."""
    file = Path(path)
    file.parent.mkdir(parents=True, exist_ok=True)
    with file.open("a", encoding="utf-8") as f:
        json.dump(asdict(trace), f)
        f.write("\n")


def write_csv(summary_list: List[Dict], path: str) -> None:
    """Write a CSV summary of traces."""
    if not summary_list:
        return
    file = Path(path)
    file.parent.mkdir(parents=True, exist_ok=True)
    with file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=summary_list[0].keys())
        writer.writeheader()
        writer.writerows(summary_list)


def rotate_logs(path: str, max_versions: int) -> None:
    """Rotate log files, keeping up to ``max_versions`` previous versions."""
    file = Path(path)
    if not file.exists():
        return
    for i in range(max_versions, 0, -1):
        src = file.with_suffix(f".v{i}") if i > 1 else file
        dst = file.with_suffix(f".v{i+1}")
        if src.exists():
            src.rename(dst)
