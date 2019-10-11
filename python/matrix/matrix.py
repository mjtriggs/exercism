class Matrix(object):
    def __init__(self, matrix_string):
        
        # Get the number of rows and columns for the matrix 
        # (and other stuff we'll use later)
        self.rows = matrix_string.split("\n")
        self.elements = matrix_string.split()
        self.num_rows = len(self.rows)
        self.num_cols = len(self.elements)/self.num_rows

    def row(self, index):
        # Output the row chosen by the index
        # Class object self.rows is a list of rows in the matrix, so relatively
        # straight forward to get the one we want.

        # Pretty simple error checking?
        if index <= 0 or index > self.num_rows:
            raise Exception('Index out of bounds')

        # We use index - 1 as the 1st row is actually the 0th row in python.    
        output = self.rows[index - 1]

        # Split the row into individual characters then turn this into an integer
        output = output.split()
        output = list(map(int, output))
        return output

    def column(self, index):
         # Input validation
         if index <= 0 or index > self.num_cols:
             raise Exception('Index out of bounds')

         # Set up the output vector
         output = []
         # For each of the rows, convert to a list and take index element
         for i in range(self.num_rows):
             r = self.rows[i]
             output.append(r.split()[index - 1])
         # map the list of characters to integers
         output = list(map(int, output))
         return output