from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple, final

from matrix_sum.matrix import ABCMinimalMatrix, ABCMinimalMatrixFactory


class ABCGenerateMatrix(ABC):
    @abstractmethod
    def __call__(self) -> ABCMinimalMatrix:
        pass


@final
class GenerateZeroMatrix(ABCGenerateMatrix):
    def __init__(self, shape: Tuple[int, int], matrix_factory: ABCMinimalMatrixFactory) -> None:
        self._shape = shape
        self._matrix_factory = matrix_factory

    def __call__(self) -> ABCMinimalMatrix:
        matrix_like = list()
        for i in range(0, self._shape[0]):
            row = [0.0 for j in range(0, self._shape[1])]
            matrix_like.append(row)
        return self._matrix_factory(matrix_like=matrix_like)
