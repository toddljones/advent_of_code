
codes = [int(x) for x in open("2019/5/input.a").read().strip().split(",")]
og_codes = list(codes)
codes = list(og_codes)

idx = 0
while idx < len(codes)-1:
    opcode = int(codes[idx])

    if len(str(opcode)) == 2:
        pass
    if len(str(opcode)) == 4:
        opcode = str(opcode)[2:]
        param_1

    if opcode not in [1,2,3,4,99]:
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
    elif opcode == 3:
        output_pos = idx + 1
        codes[output_pos] = int(input("integer: "))
    elif opcode == 4
        input_pos = idx + 1
        print(f"output {idx}: {codes[input_pos]}")

    idx += 4
