with open('information.txt', 'r') as f:
    while True:
        question = f.readline().strip()
        if question == '':
            break
        options = f.readline().strip()
        answer = f.readline().strip()
        print(question)
        print(options)
        response = input('Enter your answer : ')

        if response.strip().upper() == answer:
            print('Your answer is correct\n')
        else:
            print('Correct answer is ', answer)
        print(f.readline())
