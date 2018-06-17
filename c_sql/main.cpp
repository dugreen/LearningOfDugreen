/*************************************************************************
    > File Name: main.cpp
    > Author: SongLee
    > E-mail: lisong.shine@qq.com
    > Created Time: 2014年05月05日 星期一 00时30分45秒
    > Personal Blog: http://songlee24.github.io
 ************************************************************************/
#include<iostream>
#include "MyDB.h"
using namespace std;

int main()
{
	MyDB db;
	db.initDB("localhost", "root", "970904", "polls");
	db.exeSQL("select * from polls_choice");
	return 0;
}
