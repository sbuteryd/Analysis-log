#### how to use 
```git clone https://github.com/sbuteryd/Analysis-log.git```

```pip  install psycopg2```

#### use python 2.7.6

``` python log_analysis.py```

####  create view remove path and status 200ok
```cursor.execute("create view log_remove_root_path_fist as select substring(path,10),status from log where status = '200 OK';")```