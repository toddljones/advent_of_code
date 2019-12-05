
idx = 0
codes = [int(x) for x in open("2019/2/input.a").read().strip().split(",")]
codes[1] = 12
codes[2] = 2
print(f"len(codes) {len(codes)}")
while idx < len(codes)-1:
    opcode = int(codes[idx])

    if opcode not in [1,2,99]:
        raise Exception(f"unknown opcode {opcode}")

    input_pos_1 = codes[idx + 1]
    input_pos_2 = codes[idx + 2]
    output_pos = codes[idx + 3]

    if opcode == 99:
        break
    elif opcode == 1:
        codes[output_pos] = codes[input_pos_1] + codes[input_pos_2]
    elif opcode == 2:
        codes[output_pos] = codes[input_pos_1] * codes[input_pos_2]

    idx += 4
    print(f"new idx={idx}")
    print(f"codes = {codes}")

print(f"codes = {codes}")
print(f"final code = {codes[0]}")

