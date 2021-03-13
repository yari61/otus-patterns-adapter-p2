from __future__ import annotations
from abc import ABC, abstractmethod
from subprocess import run


class ABCSummarizeAdapter(ABC):
    @abstractmethod
    def __call__(self) -> None:
        pass


class SummarizeAdapter(ABCSummarizeAdapter):
    __slots__ = ["_input_path", "_output_path"]

    def __init__(self, input_path, output_path) -> None:
        self._input_path = input_path
        self._output_path = output_path

    def __call__(self) -> None:
        run(["python", "-m", "matrix_sum", "-i", self._input_path, "-o", self._output_path])
