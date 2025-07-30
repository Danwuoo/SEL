"""Configuration models for the orchestrator."""

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel


class ModuleConfig(BaseModel):
    """Configuration for a single module."""

    enabled: bool = True
    params: Dict[str, Any] = {}


class PipelineConfig(BaseModel):
    """Top-level pipeline configuration."""

    batch_size: int = 1
    phases: List[str] = ["main"]
    modules: Dict[str, ModuleConfig] = {}
