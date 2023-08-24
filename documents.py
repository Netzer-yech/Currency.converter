class LIST:

    def create_file(self):
        list_file = open('C:\\automation course\\Currency_Results.txt', 'w')
        list_file.write("Here are the last conversions you made: \n \n")
        list_file.close()



class Result:
    def __init__(self, result, conversion):
        self.result = result
        self.conversion = conversion

# this constructor defined the Result object with 2 properties
# the result itself and the conversion
