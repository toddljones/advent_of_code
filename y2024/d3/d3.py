import re
from typing import List

from y2024.d3.data import sample, puzzle


def extract_instructions(memory: str) -> List[str]:
    re_str = r"mul\(\d+,\d+\)"
    instructions = re.findall(re_str, memory)
    return instructions


def extract_instructions_do_dont(memory: str) -> List[str]:
    re_str = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"
    all_instructions = re.findall(re_str, memory)
    instructions = []
    on_off = True
    # filter out instructions between don't() and do()
    for instruction in all_instructions:
        if instruction == "do()":
            on_off = True
        elif instruction == "don't()":
            on_off = False
        elif on_off:
            instructions.append(instruction)
    return instructions


def eval_instruction(instruction: str) -> int:
    nums = re.findall(r"\d+", instruction)
    return int(nums[0]) * int(nums[1])


def process_memory(memory: str, honor_do_dont: bool = False) -> int:
    if honor_do_dont:
        instructions = extract_instructions_do_dont(memory)
    else:
        instructions = extract_instructions(memory)
    result = 0
    for instruction in instructions:
        result += eval_instruction(instruction)
    return result


def p1():
    print(process_memory(puzzle))


def p2():
    print(process_memory(puzzle, honor_do_dont=True))


if __name__ == "__main__":
    p1()
    p2()
