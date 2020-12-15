import logging
from argparse import ArgumentParser, Namespace

from read_input_data import get_input_data

parser: ArgumentParser = ArgumentParser()

parser.add_argument("--log", default="info")

options: Namespace = parser.parse_args()

level: int = logging.INFO

if options.log.lower() == "debug":
    level = logging.DEBUG

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    level=level)

logger: logging.Logger = logging.getLogger(__name__)


def solution(file_name: str, steps: int) -> int:
    numbers: list[int] = list(get_input_data(file_name))
    last_index_dict: dict[int, int] = {}
    last_num: int = numbers[-1]
    index: int
    for i, n in enumerate(numbers[:-1]):
        last_index_dict[n] = i
    for n in range(len(numbers) - 1, steps - 1):
        index = last_index_dict.get(last_num, n)
        last_index_dict[last_num] = n
        last_num = n - index
        logger.debug(last_num)
    return last_num


if __name__ == '__main__':
    logger.info(solution("inputData.txt", 2020))
    logger.info(solution("inputData.txt", 30000000))
