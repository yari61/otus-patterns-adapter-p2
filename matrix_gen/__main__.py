from __future__ import annotations

from .cli import parser
from .generate import GenerateContainer
from .output import DumpContainer
from .operations import SummarizeContainer


if __name__ == "__main__":
    generate_container = GenerateContainer()
    dump_container = DumpContainer()
    summarize_container = SummarizeContainer()

    args = parser.parse_args()
    generate_container.config.set("shape", (5, 5))
    generate_matrix = generate_container.generate_matrix()
    matrix1 = generate_matrix()
    matrix2 = generate_matrix()

    dump_container.config.set("path", args.output)
    dump_container.config.set("matrix1", matrix1)
    dump_container.config.set("matrix2", matrix2)
    dumper = dump_container.dumper()
    dumper()

    summarize_container.config.set("input_path", args.output)
    summarize_container.config.set("output_path", "f1.json")
    summarize_adapter = summarize_container.summarize_adapter()
    summarize_adapter()
