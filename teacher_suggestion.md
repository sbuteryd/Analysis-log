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
    
## NOTE: 安装autopep8 
$ pip install autopep8  

## NOTE: 对文件进行格式化
$ autopep8 --in-place --aggressive --aggressive <filename>


## sql format
 For multi-line query statements, using the triple quotation (""") mark,
makes it easy to understand the code and also more readable.
To improve readability, capitalize all keywords and separate each new clause by a new line.
e.g.:

query = """
SELECT SUBSTRING,
       count(SUBSTRING) AS num
FROM log_fist
JOIN articles ON log_fist.substring = articles.slug
GROUP BY log_fist.substring
ORDER BY num DESC
LIMIT 3 ;
"""
Use sql format to get a nice formatting statement.
SQLFormat is a free online formatter for SQL statements.

## REATE OR REPLACE VIEW' commands in the database.
:warning: The documentation (README) should contain the 'CREATE OR REPLACE VIEW' commands in the database.
The VIEWs should not be part of the application code.
The VIEWs should be available in the database prior to running the application.


## hardcoded
The code connects to and queries an SQL database. It does not use answers hardcoded into the application code.

From last reviewer:
"Third query is using hardcoded answer."

More about the third question:
The third question uses two queries for answering the question.
:warning: This is a project requirement:
"When the application fetches data from multiple tables, it uses a single query with a JOIN,
rather than multiple queries.
Each of the questions must be answered using only one SQL query."

It is OK to add views (CREATE VIEW) to the database, but don't modify or rename the existing table



1、
:bulb: If you are interested, here’s another way to get a solution.
CTEs, also know as Common Table Expressions, are a way of refactoring a query.
They let you give the result of a subquery a name and reuse the result multiple times.
The general syntax of a CTE looks like the following:

WITH <name1> AS (<subquery1>),
     <name2> AS (<subquery2>),
     ...
     <nameN> AS (<subqueryN>)
  query
This will first evaluate each of the subqueries and assign the results of each query to the corresponding name.
Then within the final query, you can use each name to refer to the results of the corresponding query.

:bulb: The suggested query above may be a subquery here
![Postgres CTE - 通用表格表达式](https://malisper.me/postgres-ctes/?subscribe=success#blog_subscription-3)


2、
You should put the following code within this if statement:

if __name__ == '__main__':
    # code goes here
else:
    print 'Importing ...'
This code makes sure that this file was run directly, not imported.
And will avoid executing the code when importing the file.

![Read this to see why](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

![If __name__](https://www.quora.com/Why-would-you-use-if-__name__-__main__)
Doing this, users import your code into their code and run only the functions they need.