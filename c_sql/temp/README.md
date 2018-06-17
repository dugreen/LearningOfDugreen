
```
#include <iostream>
#include <mysql/mysql.h>
 
using namespace std;
 
int main(int argc, char* argv[])
{
    //准备mysql的访问结构
    MYSQL mysql;
    mysql_init( &mysql );
  
    mysql_real_connect(
        &mysql,
        "192.168.16.114",   //要访问数据库的IP地址
        "root",         //用户名
        "root",         //密码
        "test",         //要访问的数据库
        3306,           //该数据库的端口
        NULL,           //一般为NULL
        0           //一般为0
    );
  
    //插入
    string sql = "insert into student value(1, 'jp', 24, 'gzjd')";
  
    //删除
    //string sql = "delete from student where id = 33";
  
    //执行sql语句
    mysql_query( &mysql, sql.c_str() );
 
    //关闭数据库连接
    mysql_close( &mysql );
 
    return 0;
}
```
//编译
g++ file.cpp -o target -lmysqlclient
 
//执行
./target
