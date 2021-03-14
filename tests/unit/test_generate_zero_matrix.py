from __future__ import annotations
from unittest import TestCase, main

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from matrix_gen.generate.generate import GenerateZeroMatrix
from matrix_sum.matrix import MinimalMatrixFactory


class Container(DeclarativeContainer):
    config = Configuration()
    matrix_factory = Factory(MinimalMatrixFactory)
    generate = Factory(GenerateZeroMatrix, shape=config.shape, matrix_factory=matrix_factory)


class Call(TestCase):
    def test_generated_matrix_with_correct_shape(self):
        container = Container()
        shape = (5, 5)
        container.config.set("shape", shape)
        generate = container.generate()

        generated_matrix = generate()

        self.assertEqual(shape, generated_matrix.get_shape())

    def test_generated_zero_matrix(self):
        container = Container()
        shape = (5, 5)
        container.config.set("shape", shape)
        matrix_factory = container.matrix_factory()
        generate = container.generate(matrix_factory=matrix_factory)

        generated_matrix = generate()

        for i in range(0, shape[0]):
            for j in range(0, shape[0]):
                self.assertEqual(0.0, generated_matrix.get_cell(i, j))

if __name__ == "__main__":
    main()
