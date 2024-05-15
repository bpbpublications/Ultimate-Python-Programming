class Question:

    def __init__(self):
        self.text = ''
        self.options = []
        self.answer = 0

    def enter_details(self):
        self.text = input('Enter the text of the question : ')

        n = int(input('How many options do you want to give for the answer : '))
        for i in range(n):
            option = input(f'Enter option {i + 1} : ')
            self.options.append(option)

        self.answer = int(input('Enter the option number of the correct answer : '))

    def ask(self):
        print(self.text)
        for i in range(len(self.options)):
            print(f'{i + 1}. {self.options[i]}')
        response = int(input('Enter your option : '))
        return self._check(response)

    def _check(self, response):
        if response == self.answer:
            print('Your answer is correct\n')
            return True
        else:
            print('Sorry, wrong answer.', end=' ')
            print(f'Option {self.answer} is the correct answer\n')
            return False


if __name__ == '__main__':
    question = Question()
    question.enter_details()
    question.ask()
