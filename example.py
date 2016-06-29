'''
Example os how to use C.Compiler packages 
'''

from C.Compiler import Compiler 

c = Compiler()

compiling_result = c.compile("/home/livetolove128/Projects/NTU EdX/pythonPackages/CodeExecutor/test.c", "/home/livetolove128/Projects/NTU EdX/pythonPackages/CodeExecutor/test")

result = c.run("/home/livetolove128/Projects/NTU EdX/pythonPackages/CodeExecutor/test")

print(result)
print(compiling_result)
    
