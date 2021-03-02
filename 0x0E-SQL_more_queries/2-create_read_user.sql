--  creates the MySQL server user user_0d_1
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
