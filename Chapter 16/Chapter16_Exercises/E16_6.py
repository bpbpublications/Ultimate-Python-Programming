class CustomString(str):
    def __init__(self, value):
        str.__init__(value)

    def spacify(self):
        if not self:  # empty string
            return self

        s = ''
        for i in range(0, len(self) - 1):
            s += self[i] + ' '
        s += self[len(self) - 1]  # no blank after last character

        return s

    def space_to_underscore(self):
        return self.replace(' ', '_')

    def reverse(self):
        return self[::-1]

    def count_vowels(self):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in self if char in vowels)

    def is_palindrome(self):
        s = ''.join(char for char in self if char.isalnum()).lower()
        return s == s[::-1]


my_string = CustomString('Madam I am Adam')
print('Reversed:', my_string.reverse())
print('Number of vowels:', my_string.count_vowels())
print('Is Palindrome:', my_string.is_palindrome())
print(my_string.spacify())
print(my_string.space_to_underscore())
