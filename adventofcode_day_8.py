# -*- coding: utf-8 -*-
"""adventofcode_day_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cc_yErAgJjsYDW0BTLrt1HhwKOOq0Lbc
"""
f = open("data/day_8_part_1.txt")
test_data_part_1 = "".join(f.readlines())

# print(test_data_part_1)

boot_code = test_data_part_1.split("\n")


lines_executed = []
total_possible_lines = len(boot_code)


def execute_line(accumulator, line_number):

    instruction = boot_code[line_number]
    print("Executing line:", line_number, "| accumulator:", accumulator)

    if line_number in lines_executed:
        print("Duplicate line attempted:", line_number, lines_executed)
        print("\nAccumulator:", accumulator)
        return
    lines_executed.append(line_number)

    if "acc" in instruction:
        increment_value = int(instruction.split(" ")[1][1:])
        if "+" in instruction:
            accumulator += increment_value
        else:
            accumulator -= increment_value
        line_number += 1

    elif "jmp" in instruction:
        jump_value = int(instruction.split(" ")[1][1:])
        if "+" in instruction:
            line_number += jump_value
        else:
            line_number -= jump_value

    else:
        line_number += 1

    if len(lines_executed) == total_possible_lines:
        print("\nAccumulator:", accumulator)
        return
    else:
        execute_line(accumulator, line_number)


# execute_line(0, 0)


def execute_line2(modded_boot_code, accumulator, line_number, lines_executed_check=[]):

    instruction = modded_boot_code[line_number]
    # print(
    #     "Executing line:",
    #     line_number,
    #     "| accumulator:",
    #     accumulator,
    #     "| instruction:",
    #     instruction,
    # )

    if line_number in lines_executed_check:
        # print("Duplicate line attempted:", line_number, lines_executed_check)
        return

    else:
        lines_executed_check.append(line_number)

    if "acc" in instruction:
        increment_value = int(instruction.split(" ")[1][1:])
        if "+" in instruction:
            accumulator += increment_value
        else:
            accumulator -= increment_value
        line_number += 1
    elif "jmp" in instruction:
        jump_value = int(instruction.split(" ")[1][1:])
        if "+" in instruction:
            line_number += jump_value
        else:
            line_number -= jump_value
    else:
        line_number += 1

    if line_number == len(modded_boot_code):
        print("\nAccumulator:", accumulator)
        return


    execute_line2(modded_boot_code, accumulator, line_number, lines_executed_check)

f = open("data/day_8_part_2.txt")
test_data_part_2 = "".join(f.readlines())

# print(test_data_part_1)

boot_code = test_data_part_2.split("\n")


to_check = [i for i, x in enumerate(boot_code) if "jmp" in x or "nop" in x]

print(to_check)
for swap_index in to_check:
    # print("swapping:", swap_index)
    modded_boot_code = boot_code[:]

    line_to_mod = modded_boot_code[swap_index]
    if "jmp" in line_to_mod:
        modded_boot_code[swap_index] = line_to_mod.replace("jmp", "nop")
    else:
        modded_boot_code[swap_index] = line_to_mod.replace("nop", "jmp")

    # print(modded_boot_code)
    # print(modded_boot_code[swap_index])
    execute_line2(modded_boot_code, 0, 0, [])
