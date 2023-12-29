#must link (import) def from seperate file to the file the function will be used in
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}") 
    
    #another way to import a function is: 
# import functions(file with def)

#for i in range(10):
    #print(f"The square of {i} is {functions.square(i)}") 