from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import Mock
from json import loads

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from matrix_gen.output.format import MatrixPairJsonFormat
from matrix_sum.matrix import ABCMinimalMatrix
from matrix_sum.matrix.extensions import ToList


class Container(DeclarativeContainer):
    config = Configuration()
    json_format = Factory(MatrixPairJsonFormat, matrix1=config.matrix1, matrix2=config.matrix2)


class Call(TestCase):
    def test_formatted_correctly(self):
        container = Container()
        shape = (5, 5)
        value = 0.0
        container.config.set("matrix1", Mock(ABCMinimalMatrix, get_shape=Mock(return_value=shape), get_cell=Mock(return_value=value)))
        container.config.set("matrix2", Mock(ABCMinimalMatrix, get_shape=Mock(return_value=shape), get_cell=Mock(return_value=value)))
        expected_result = {"a": ToList(matrix=container.config.matrix1()).__call__(), "b": ToList(matrix=container.config.matrix2()).__call__()}
        json_format = container.json_format()

        formatted = json_format()

        self.assertEqual(expected_result, loads(formatted))

if __name__ == "__main__":
    main()
