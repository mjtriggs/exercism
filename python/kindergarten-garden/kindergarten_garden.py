class Garden(object):
    def __init__(self, diagram, students = None):
        
        # Define the default students in case none are submitted
        default_students = ['Alice', 'Bob', 'Charlie', 'David', \
                            'Eve', 'Fred', 'Ginny', 'Harriet', \
                            'Ileana', 'Joseph', 'Kincaid', 'Larry']


        # If students are input, use that - otherwise default to given list
        if students is None:
            self.student_list = default_students
        else: 
            students.sort()
            self.student_list = students    

        # Get top and bottom rows
        plants = diagram.split()
        self.top_row = plants[0]
        self.bottom_row = plants[1]  

    def plants(self, student):
        
        # Define flora
        flora = {'G': 'Grass', 'C':'Clover', 'R':'Radishes', 'V':'Violets'}

        # Identify student number
        student_index = self.student_list.index(student)
        
        # get the plants
        top_plants = [self.top_row[i] for i in [student_index * 2, 1 + student_index * 2]]
        bottom_plants = [self.bottom_row[i] for i in [student_index * 2, 1 + student_index * 2]]
        student_plants = top_plants + bottom_plants

        # get the plant full names for output using flora list
        out = [flora[i] for i in student_plants]
        return out