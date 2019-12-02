def intcode(memory: list):
    instruction_pointer = 0
    opcode = memory[instruction_pointer]

    while opcode != 99:

        address_par1 = memory[instruction_pointer + 1]
        address_par2 = memory[instruction_pointer + 2]
        address_par3 = memory[instruction_pointer + 3]

        par1 = memory[address_par1]
        par2 = memory[address_par2]

        if opcode == 1:
            memory[address_par3] = par1 + par2
        elif opcode == 2:
            memory[address_par3] = par1 * par2
        else:
            raise Exception

        instruction_pointer += 4

        opcode = memory[instruction_pointer]

    return memory[0]


def replace_input(memory, noun=12, verb=2):
    memory[1] = noun
    memory[2] = verb
    word = int(100 * noun + verb)
    return memory, word


def read_intcode(file):
    with open(file, "r") as f:
        memory = [int(n) for n in f.read().split(",")]

    memory, word = replace_input(memory)

    return intcode(memory)


def find_word(file):

    for noun in range(100):
        for verb in range(100):
            with open(file, "r") as f:
                memory = [int(n) for n in f.read().split(",")]
            mem, word = replace_input(memory, noun=noun, verb=verb)
            try:
                output = intcode(mem)
            except Exception:
                pass
            if output == 19690720:
                return word
