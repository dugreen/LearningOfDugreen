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
        "localhost",   //要访问数据库的IP地址
        "root",         //用户名
        "970904",         //密码
        "polls",         //要访问的数据库
        3306,           //该数据库的端口
        NULL,           //一般为NULL
        0           //一般为0
    );
  
    //插入
    string sql = "select * from polls_choice";
  
    //删除
    // string sql = "delete from polls_choice where id = 2";
  
    //执行sql语句
    //mysql_query( &mysql, sql.c_str() );

    //sql查询
    MYSQL_RES *temp;
    temp = mysql_store_result(&mysql);
    
    //cout<<sql<<endl;
    
    int fields =  mysql_num_fields(temp);
    cout<<temp<<endl;
    //关闭数据库连接
    mysql_free_result(temp);	
    mysql_close( &mysql );
 
    return 0;
}
