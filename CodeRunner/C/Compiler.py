# Dependencies 
import subprocess32
import os.path as path
import hashlib
from datetime import datetime 

# Execute 
class Compiler:

    ''' 
        Compiler uses Docker as a sandboxing environment to 
        actually compile and run the code
        By default, it will execute Docker container in local computer
        The environment can be set by docker-machine
    '''
    
    def __init__(self):

        self.root = hashlib.sha256(str(datetime.now())).hexdigest()
        
        # Create a common persistent volume for all containers (processes)
        subprocess32.call(["docker", "run", "--name", self.root, "-v", "/source_code", "-v", "/executable","gcc:latest"])


    '''
       This function if for testing purpose only due to some limitation of parallel
       programming in Python using multiprocessing.Pool() method 
    '''
    def __call__(self, executable_file_path):
        return self.run(executable_file_path)

    
    def compile(self, path_to_source_code, executable_file_path):

        ''' 
           Return a dictionary with the following format {'is_successful': Boolean, 'error_message': String or None, 'executable_name': String or None}
        '''
        try:
            
            compiling_result = dict([("is_successful", True), ("error_message", None), ("executable_file_path", executable_file_path)])
            dirname_source_code = path.dirname(path_to_source_code) # get directory name from path_to_source_code
            dirname_executable = path.dirname(executable_file_path)
            filename_source_code = path.basename(path_to_source_code)
            filename_executable = path.basename(executable_file_path)
            dirname_in_container_source_code = hashlib.sha256(dirname_source_code).hexdigest()
            dirname_in_container_executable = hashlib.sha256(dirname_executable).hexdigest()
            
            # if directories do not exists inside the container, then create them
            if(subprocess32.call(["docker", "run", "--volumes-from", self.root, "gcc:latest", "test", "-e", "/source_code/" + dirname_in_container_source_code]) == 1):
                subprocess32.call(["docker", "run", "--volumes-from", self.root, "gcc:latest", "mkdir", "/source_code/" + dirname_in_container_source_code])

            if(subprocess32.call(["docker", "run", "--volumes-from", self.root, "gcc:latest", "test", "-e", "/executable/" + dirname_in_container_executable]) == 1):
                subprocess32.call(["docker", "run", "--volumes-from", self.root, "gcc:latest", "mkdir", "/executable/" + dirname_in_container_executable])
                
            # copy the file to dirname_in_container_source_code
            subprocess32.call(["docker", "cp", path_to_source_code, self.root + ":/source_code" + "/" + dirname_in_container_source_code])
        
            # Compile the code by running a container 
            compiling_result["error_message"] = subprocess32.Popen(["docker", "run", "--volumes-from", self.root, "gcc:latest", "gcc", "/source_code/" + dirname_in_container_source_code + "/" + filename_source_code, "-o", "/executable/" + dirname_in_container_executable + "/" + filename_executable], stdout=subprocess32.PIPE, stderr=subprocess32.PIPE).communicate()[1]

            # TODO: this code is likely to produce errors. Need to test here carefully
            if(compiling_result["error_message"] != ''):
                compiling_result["is_successful"] = False
                compiling_result["executable_file_path"] = None

            return compiling_result
                
        except Exception as e:
            print("Exception: "+ str(e))

    # Run the executable file after being compiled
    def run(self, executable_file_path):

        try:
            
            filename_executable = path.basename(executable_file_path)
            dirname_executable = path.dirname(executable_file_path)
            dirname_in_container_executable = hashlib.sha256(dirname_executable).hexdigest()

            executable_result = subprocess32.Popen(["docker", "run", "--volumes-from", self.root, "-m", "5M", "--kernel-memory" , "50M" ,"gcc:latest", "/executable/" + dirname_in_container_executable + "/" + filename_executable], stdout=subprocess32.PIPE, stderr=subprocess32.PIPE).communicate()[0]

            return executable_result

        except Exception as e:
            print("Exception: " + str(e))
 
            
