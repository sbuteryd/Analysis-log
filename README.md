
## how to use 

```git clone https://github.com/sbuteryd/Analysis-log.git```


1、需要把文件Analysis-log.git 放入虚拟你运行(vagrant)

2、 在执行文件前需要安装 psycopg2 模块

```pip  install psycopg2```


3、view:log_fist 如下内容，找出路径，和成功访问的,以及如何创建 view。

```
 create view log_fist
    as select substring(path,10),status from
    log where status = '200 OK';
    """)
```
 
 | Column   | Type | Modifiers 
 |----------|:----------:|:-----------:|
 |substring | text | ||


4、view:authors_second 找出作者的名字

```
    create view authors_second as
    select slug,name from articles join
    authors on articles.author = authors.id;
    """
```
|slug       |  name       
|---------- |:----------:|
bad-things-gone|Anonymous Contributor|


5 On which days did more than 1% of requests lead to errors?"
```
    """
     create view error_connect as SELECT time::date AS day, count(*)
    FROM log WHERE status != '200 OK' GROUP BY day;
    """
    
```
