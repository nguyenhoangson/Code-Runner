from C.Compiler import Compiler

c = Compiler()

# Test 1: .c file exists as stated in sourcePath and all its syntax is correct 
def test_the_case_when_the_file_exists_and_all_syntax_are_correct():

    # compile the file 
    compiling_result = c.compile("./test.c", "test")

    assert compiling_result["is_successful"] is True
    assert compiling_result["error_message"] is None 


    # Test content of the result
    
# Test 2: .c file is listed properly and syntax is incorrect
def test_it_should_return_executable_file_when_the_file_exists_and_all_syntax_are_correct():
    #compile the file
    # c.compile("./test_2.c", "./test_2") 
    assert os.path.isfile("./test_2") is True # assert the file exists 
    
    

    
