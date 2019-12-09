from index import getResult

OUTPUT = 19690720
for noun in range(100):
    for verb in range(100):
        if(getResult(noun, verb) == OUTPUT):
            print(100 * noun + verb)
            break
