'''
Example os how to use C.Compiler packages 
'''

from CodeRunner.C.Compiler import Compiler 
 
c = Compiler()

compiling_result = c.compile("/home/livetolove128/Projects/NTU EdX/packages/CodeRunner/test.c", "/home/livetolove128/Projects/NTU EdX/packages/CodeRunner/test")

result = c.run("/home/livetolove128/Projects/NTU EdX/packages/CodeRunner/test")

print(result)
print(compiling_result)

