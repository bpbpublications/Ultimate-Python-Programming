class VideoCourse:
    def __init__(self, title, instructor, duration):
        self.title = title
        self.instructor = instructor
        self.duration = duration

    def __len__(self):
        return self.duration


course1 = VideoCourse('Learn Piano', 'Jack', 10)
course2 = VideoCourse('Learn Python', 'John', 15)

print(len(course1), len(course2))
