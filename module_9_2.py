print('\033[30m\033[47mДомашнее задание по теме "Списковые, словарные сборки"\033[0m')
print('\033[30m\033[47mЦель: закрепить знания о списочных и словарных сборках, решив несколько небольших задач.\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(x) for x in first_strings if len(x) > 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}

# Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)
print()
print(thanks)
