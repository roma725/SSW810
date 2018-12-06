'''Roma Shah
HW 9
create 3 classes and file generator etc'''

import collections from defaultdict

def generator(path, numOfValues): #reads the file
while True:
    try:
        fp=open (file_name, "r")
    except FileNotFoundError:
        print("Can't open", file_name)
    except ValueError:
        print("'foo.txt' has 3 fields on line 26 but expected 4")
    else:
        with fp:
            lines= fp. readlines()
            rows=[] #loop thru it
            for line in lines:
                values=line.split(",")
                if len(value)!== numOfValues:
                    throw ValueError#not sure if t
                else:
                yield object(line.split(","))

class Repository: #holds all your info in one place
    def __init__(self,name, major):
        self.name=name
        self.major=major
    
    def grades(self):
        return self.name 
    
    def __str__(self):
        return()


class Student:
    #including a defaultdict(str) to store the classes taken 
    #and the grade where the course is the key and the grade is the value
    dd=defaultdict(str)

class Instructor:
    #hold all of the details of an instructor, 
    #including a defaultdict(int) to store the names of the courses taught along with the number of students
    dd=defaultdict(int)
    

def main():


if __name__ == '__main__':
    main(
   # for cwid, name, major in file_reader(path, 3, sep='|', header=True):
    #    print("name: {} cwid: {} major: {}".format(name, cwid, major))