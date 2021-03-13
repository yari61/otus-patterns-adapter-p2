from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from .generate import GenerateZeroMatrix
from matrix_sum.matrix import MinimalMatrixFactory


class GenerateContainer(DeclarativeContainer):
    config = Configuration()
    matrix_factory = Factory(MinimalMatrixFactory)
    generate_matrix = Factory(GenerateZeroMatrix, shape=config.shape, matrix_factory=matrix_factory)

__all__ = ["GenerateContainer"]
