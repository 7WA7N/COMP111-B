# Muhammad Ali Awan 
# 231522965
# COMP111 - B 
# Lab 5


class Classroom():
    total_students = 0
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.roll_call = []

    def add_student(self, name):
        self.capacity += 1
        total_students = self.capacity
        self.roll_call.append(name)
        print(f'{name} has been added to the classroom.')

    def student_count(self):
        print(f'Capacity: {self.capacity}')

    def display_students(self):
        print(f'Students in the classroom: {self.roll_call}')
    
    def get_total_students(self):
        total_students = self.capacity
        print(f'Total students: {total_students}')

def main():
    # Classroom 1 
        classroom1 = Classroom(1111, 5)
        classroom1.add_student('John')
        classroom1.add_student('Mary')
        classroom1.add_student('Bob')
        classroom1.add_student('Jane')
        classroom1.add_student('Jack')
        classroom1.student_count()
        classroom1.display_students()
        classroom1.get_total_students()
        # Classroom 2
        classroom2 = Classroom(2222, 4)
        classroom2.add_student('Ali')
        classroom2.add_student('Haze')
        classroom2.add_student('Khan')
        classroom2.add_student('Sara')
        classroom2.student_count()
        classroom2.display_students()
        classroom2.get_total_students()
        # Classroom 3
        classroom3 = Classroom(3333, 3)
        classroom3.add_student('Faiza')
        classroom3.add_student('Noor')
        classroom3.add_student('Rizwan')
        classroom3.student_count()
        classroom3.display_students()
        classroom3.get_total_students()
main()
