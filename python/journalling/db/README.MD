# export database

mysqldump -uroot -proot naa > naa_dump.sql    


# import database 

mysql -uroot -proot naa < naa_dump.sql