from typing import Iterator, TextIO


def get_input_data(file_name: str) -> Iterator[int]:
    f: TextIO = open(file_name)

    return map(int, f.readline().strip().split(","))