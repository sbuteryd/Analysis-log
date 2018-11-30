## udacity teacher

    Oops! You forgot to include the shebang line!
    Shebang line is essential so the interpreter knows 
    which version of Python it has to use to run your script. 
    The shebang line can be #!/usr/bin/env python (when using Python2) 
    or #!/usr/bin/env python3 (when using Python3).
    
    In computing, a shebang (also called a hashbang, hashpling, pound bang, or crunchbang)
     refers to the characters "#!" when they are the first two characters in an interpreter 
     directive as the first line of a text file. In a Unix-like operating system, the program loader 
     takes the presence of these two characters as an indication that the file is a script, 
     and tries to execute that script using the interpreter specified by the rest of the first line in the file.
    
    
second    
    
    You forgot to include some informations here :(
    Think that someone who isn't an Udacity's student is trying to execute your project and you have to let him/her know every single step! :)

    For example, include:

    If using Vagrant/VirtualBox, how to set it up.
    How to access the database in order to create the views.
    The CREATE VIEW statements
    A link to the newsdata.sql file so the user can import it into the database
    How to import the data into the database.
    
third

    The code conforms to the PEP8 style recommendations.
    You can install the pycodestyle tool to test this, with pip install 
    pycodestyle or pip3 install pycodestyle (Python 3).

    In order for this requirement to pass, running the 
    pycodestyle tool on your code should produce zero warnings.

    (pycodestyle was formerly known as pep8. These are the same thing.)
    
# NOTE: 安装autopep8 
$ pip install autopep8  

# NOTE: 对文件进行格式化
$ autopep8 --in-place --aggressive --aggressive <filename>