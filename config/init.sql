CREATE USER 'root'@'%' IDENTIFIED BY 'root';
GRANT All privileges ON *.* TO 'root'@'%';
update user set host='%' where user='root' limit 1;
flush privileges;