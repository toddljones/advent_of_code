def test_extract_instructions():
    from y2024.d3.d3 import extract_instructions
    from y2024.d3.data import sample

    expected_instructions = [
        "mul(2,4)",
        "mul(5,5)",
        "mul(11,8)",
        "mul(8,5)",
    ]

    instructions = extract_instructions(sample)

    assert instructions == expected_instructions


def test_eval_instruction():
    from y2024.d3.d3 import eval_instruction

    input = "mul(2,4)"

    expected_result = 8

    result = eval_instruction(input)

    assert result == expected_result


def test_process_memory():
    from y2024.d3.d3 import process_memory
    from y2024.d3.data import sample

    expected_result = 161

    result = process_memory(sample)

    assert result == expected_result


def test_extract_instructions_do_dont():
    from y2024.d3.d3 import extract_instructions_do_dont
    from y2024.d3.data import sample2

    expected_instructions = [
        "mul(2,4)",
        "mul(8,5)",
    ]

    instructions = extract_instructions_do_dont(sample2)

    assert instructions == expected_instructions
