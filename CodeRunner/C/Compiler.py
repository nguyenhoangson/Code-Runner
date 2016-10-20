# Dependencies 
import subprocess32
import os.path as path
import hashlib
from datetime import datetime 
from random import randint

# Execute 
class Compiler:

    ''' 
        Compiler uses Docker as a sandboxing environment to 
        actually run the code
        By default, it will execute Docker container in local computer
        The environment can be set by docker-machine
    '''
    
    def __call__(self, executable_file_path):
        return self.run(executable_file_path)
    
    def compile(self, path_to_source_code, executable_file_path):

        ''' 
           Return a dictionary with the following format 
           {'is_successful': Boolean, 'error_message': 
           String or None, 'executable_name': String or None}
        '''
        try:
            
            compiling_result = dict([("is_successful", True), ("error_message", None), ("executable_file_path", executable_file_path)])
            
            compiling_result["error_message"] = subprocess32.Popen(["gcc", "-g", "-Wall", path_to_source_code, "-o", executable_file_path], stdout=subprocess32.PIPE, stderr=subprocess32.PIPE).communicate()[1]
                        
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
            random_string = hashlib.sha256(str(randint(0, 1000))).hexdigest()
            docker_unique = hashlib.sha256(str(datetime.now())).hexdigest() + random_string 

            # Create a docker volume
            subprocess32.call(["docker", "run", "--name", docker_unique, "-v", "/executable", "gcc:latest"])
            
            # Copy executable file from host to docker volume 
            subprocess32.call(["docker", "cp", executable_file_path, docker_unique + ":executable"])

            # Run executable file inside Docker container
            executable_result = subprocess32.Popen(["docker", "run", "--volumes-from", docker_unique, "-m", "5M", "--kernel-memory" , "50M" ,"gcc:latest", "/executable/" + filename_executable], stdout=subprocess32.PIPE, stderr=subprocess32.PIPE).communicate()[0]

            # Remove executable file from volume of docker 
            subprocess32.call(["docker", "rm", "--volumes=true", docker_unique])
            
            return executable_result

        except Exception as e:
            print("Exception: " + str(e))
 
            
