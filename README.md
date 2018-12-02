
how to use 
```git clone https://github.com/sbuteryd/Analysis-log.git```


需要把文件Analysis-log.git 放入虚拟你运行(vagrant)

 在执行文件前需要安装 psycopg2 模块
```pip  install psycopg2```
 
use python 2.7.6

``` python log_analysis.py```

log_fist view 如下内容，找出路径，和成功访问的。
表格内容：

```
cursor.execute("""
    create view log_fist
    as select substring(path,10),status from
    log where status = '200 OK';
    """
```
news=> \d log_fist
    Column   | Type | Modifiers 
    -----------+------+-----------
    substring | text | 
    status    | text | 
 
substring       | status 
----------------------+--------
    candidate-is-jerk    | 200 OK
    goats-eat-googles    | 200 OK

 
 
view: authors_second 找出作者的名字

```
    create view authors_second as
    select slug,name from articles join
    authors on articles.author = authors.id;
    """
```
 slug            |          name          
 ---------------------------+------------------------
     bad-things-gone           | Anonymous Contributor
     balloon-goons-doomed      | Markoff Chaney
     bears-love-berries        | Ursula La Multa
     candidate-is-jerk         | Rudolf von Treppenwitz
     goats-eat-googles         | Ursula La Multa
     media-obsessed-with-bears | Ursula La Multa
     trouble-for-troubled      | Rudolf von Treppenwitz
     so-many-bears             | Ursula La Multa


view: calculate_third 统计 log的行数

    news=> select count(*) from log;
    count  
    ---------
    1677735
    (1 row)
 
view: error_third 找出404失败的链接:

        date    |    status     
    ------------+---------------
     2016-07-01 | 404 NOT FOUND
     2016-07-01 | 404 NOT FOUND
     2016-07-01 | 404 NOT FOUND
     2016-07-01 | 404 NOT FOUND
     2016-07-01 | 404 NOT FOUND
     
 