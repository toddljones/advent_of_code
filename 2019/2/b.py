
codes = [int(x) for x in open("2019/2/input.a").read().strip().split(",")]
og_codes = list(codes)
for noun in range(0,100):
    for verb in range(0,100):
        codes = list(og_codes)
        idx = 0
        codes[1] = noun
        codes[2] = verb
        print(f"noun {noun} verb {verb}")
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

            # if codes[output_pos] == 19690720:
            #     print(f"noun {noun} verb {verb}")
            #     print(f"magic number {100 * noun + verb}")
            #     exit()

        print(f"------> {codes[0]} {codes[0] - 19690720}")
        if codes[0] == 19690720:
            print(f"noun {noun} verb {verb}")
            print(f"magic number {100 * noun + verb}")
            exit()
