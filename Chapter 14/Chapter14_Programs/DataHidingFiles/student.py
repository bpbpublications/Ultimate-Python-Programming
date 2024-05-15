class Student:
    def __init__(self, name, phone, marks):
        self.name = name
        self.phone = phone
        self._marks = marks

    def _calculate_total(self):
        return sum(self._marks)

    def _calculate_percentage(self):
        return self._calculate_total() / 4

    def display(self):
        print(self.name, self.phone)

    def show_result(self):
        self.display()
        percentage = self._calculate_percentage()
        print(f'Percentage : {percentage : .1f}')
        print('Pass' if percentage > 40 else 'Fail')


# class Student:
#     def __init__(self, name, phone, marks):
#         self.name = name
#         self.phone = phone
#         self._marks = marks
#
#     def _calculate_total(self):
#         total_best3 = sum(sorted(self._marks)[1:])
#         return total_best3
#
#     def _calculate_percentage(self):
#         return self._calculate_total() / 3
#
#     def display(self):
#         print(self.name, self.phone)
#
#     def show_result(self):
#         self.display()
#         percentage = self._calculate_percentage()
#         print(f'Percentage : {percentage : .1f}')
#         print('Pass' if percentage > 40 else 'Fail')
#
#
# class Student:
#     def __init__(self, name, phone, marks):
#         self.name = name
#         self.phone = phone
#         self._marks = marks
#
#     def _calculate_cgpa(self):
#         credit_hours = [3, 3, 4, 2]
#         total_grade_points = 0
#         for i, score in enumerate(self._marks):
#             if score > 90:
#                 grade_points = 10
#             elif score > 70:
#                 grade_points = 8
#             elif score > 50:
#                 grade_points = 6
#             elif score > 30:
#                 grade_points = 4
#             else:
#                 grade_points = 0
#             total_grade_points += grade_points * credit_hours[i]
#         cgpa = total_grade_points / sum(credit_hours)
#         return cgpa
#
#     def display(self):
#         print(self.name, self.phone)
#
#     def show_result(self):
#         self.display()
#         cgpa = self._calculate_cgpa()
#         print(f'cgpa : {cgpa : .1f}')
#         print('Pass' if cgpa > 4 else 'Fail')
