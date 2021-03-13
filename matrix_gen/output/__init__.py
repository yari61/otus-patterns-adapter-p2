from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from .format import MatrixPairJsonFormatFactory
from matrix_sum.output.dump import MatrixDump
from matrix_sum.output.write import FileWriteFactory


class DumpContainer(DeclarativeContainer):
    config = Configuration()
    write_factory = Factory(FileWriteFactory, path=config.path)
    format_factory = Factory(MatrixPairJsonFormatFactory, matrix1=config.matrix1, matrix2=config.matrix2)
    dumper = Factory(MatrixDump, write_factory=write_factory, format_factory=format_factory)

__all__ = ["DumpContainer"]
