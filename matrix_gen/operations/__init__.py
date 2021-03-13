from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from .summarize import SummarizeAdapter


class SummarizeContainer(DeclarativeContainer):
    config = Configuration()
    summarize_adapter = Factory(SummarizeAdapter, input_path=config.input_path, output_path=config.output_path)

__all__ = ["SummarizeContainer"]
