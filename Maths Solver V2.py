# Answers any question by adding the numbers in the question (works for words and ASCII characters)

questions_list = [
    'What is the sum of seven and seven?',
    'What is the sum of 3 and 3?',
    'Add 5 and 7',
    'What is 7 plus seven?',
    'What is 8 add 3?'
    ]

questions_list.append(input('Ask a question adding numbers up to 10: '))

numbers_word = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

numbers_range = range(10)

for line in questions_list:
    line = str(line).split()
    print(line)
    answer = 0
    integer = 0
    for text in numbers_word:
        for word in line:
            if str(text) in word:
                answer += integer
        integer += 1
    answer2 = 0
    integer2 = 0
    for word in line:
        for integer2 in numbers_range:
           if str(integer2) in word:
               answer2 += integer2
        integer2 += 1
    print(answer + answer2)
