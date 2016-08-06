# CodeRunner [![Build Status](https://travis-ci.org/nguyenhoangson/CodeRunner.svg?branch=master)](https://travis-ci.org/nguyenhoangson/CodeRunner)


Code Runner uses Docker as sandboxing environment

# Prerequisites
To use CodeRunner package, it requires the following dependencies to be installed: 

```console
Docker: 1.11.2 
```

```console
Docker-machine: 0.7.0
```

```console
python 2.7.11
```

# Set up 
Guide to set up. 

```console
Important: Each of following step is compulsory. Don't miss any to make sure package will work properly  
```

Download the following 2 [scripts](https://github.com/nguyenhoangson/Automation/tree/master/Setup) to your computer:
```console
pre_set_up
set_up_django_server 
```

Change mod for these two scripts:
```console
chmod 755 pre_set_up set_up_django_server 
```
Run them to set up
```console
./pre_set_up
./set_up_django_server
```

Test if setup is done by running example.py file: 
```console
python example.py
```
# User Guide 


