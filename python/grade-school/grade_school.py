import pandas as pd

class School(object):
    def __init__(self):
        self.school = pd.DataFrame(columns = ['Name', 'Grade'])

    def add_student(self, name, grade):
        new_student = pd.DataFrame({'Name': [name],'Grade': [grade]})
        self.school = self.school.append(new_student)

    def roster(self):
        student = self.school.sort_values(by = ['Grade', 'Name'])['Name'].to_list()
        return student

    def grade(self, grade_number):
        out = self.school[self.school['Grade'] == grade_number].sort_values(by = ['Name'])['Name'].to_list()
        return out