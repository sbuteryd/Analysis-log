
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
 create view log_fist
    as select substring(path,10),status from
    log where status = '200 OK';
    """)
```

view的内容如下：
 View "public.log_fist"
 
 | Column   | Type | Modifiers 
 |----------|:----------:|:-----------:|
 |substring | text | ||


 
 
 
view: authors_second 找出作者的名字

```
    create view authors_second as
    select slug,name from articles join
    authors on articles.author = authors.id;
    """
```



|slug       |  name       
|---------- |:----------:|
bad-things-gone|Anonymous Contributor|



view: calculate_third 统计 log的行数

    news=> select count(*) from log;
    count  
    ---------
    1677735
    (1 row)
 
view: error_third 找出404失败的链接:



date    |    status     
--------|------------
2016-07-01 | 404 NOT FOUND
2016-07-01 | 404 NOT FOUND

     
 
