from __future__ import annotations
from json import dumps

from matrix_sum.matrix import ABCMinimalMatrix
from matrix_sum.matrix.extensions import ToList
from matrix_sum.output.format import ABCFormat, ABCFormatFactory


class MatrixPairJsonFormat(ABCFormat):
    def __init__(self, matrix1: ABCMinimalMatrix, matrix2: ABCMinimalMatrix, indent: int = 2) -> None:
        self._matrix1 = matrix1
        self._matrix2 = matrix2
        self._indend = indent
    
    def __call__(self) -> str:
        to_list1 = ToList(matrix=self._matrix1)
        to_list2 = ToList(matrix=self._matrix2)
        result = {"a": to_list1(), "b": to_list2()}
        return dumps(result, indent=self._indend)


class MatrixPairJsonFormatFactory(ABCFormatFactory):
    def __init__(self, matrix1: ABCMinimalMatrix, matrix2: ABCMinimalMatrix) -> None:
        self._matrix1 = matrix1
        self._matrix2 = matrix2

    def __call__(self) -> ABCFormat:
        return MatrixPairJsonFormat(matrix1=self._matrix1, matrix2=self._matrix2)
