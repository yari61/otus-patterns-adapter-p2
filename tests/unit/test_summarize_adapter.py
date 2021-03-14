from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import Mock, MagicMock, patch

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from matrix_gen.operations.summarize import SummarizeAdapter


class Container(DeclarativeContainer):
    config = Configuration()
    summarize_adapter = Factory(SummarizeAdapter, input_path=config.input_path, output_path=config.output_path)


class Call(TestCase):
    def test_called_correct_module(self):
        container = Container()
        container.config.set("input_path", "f0.json")
        container.config.set("output_path", "f1.json")
        summarize_adapter = container.summarize_adapter()
        with patch("matrix_gen.operations.summarize.run") as subprocess_run:
            summarize_adapter()
            subprocess_run.assert_called_once_with(["python", "-m", "matrix_sum", "-i", container.config.input_path(), "-o", container.config.output_path()])

if __name__ == "__main__":
    main()
