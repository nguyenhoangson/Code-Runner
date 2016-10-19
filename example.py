'''
Example of how to use C.Compiler packages 
'''

from CodeRunner.C.Compiler import Compiler 
 
c = Compiler()

print(c.compile("./test.c", "./test")["error_message"])

print(c.run("./test"))

