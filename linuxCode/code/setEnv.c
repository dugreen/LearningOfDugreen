#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(void) {
  /* code */
  char *val;

  const char *name = "ABD";

  val = getenv(name);//获取制指定名称的环境变量 null
  printf("%s = %s\n",name,val);

  setenv(name,"good-good-study",1);//设置新的环境变量 name存在,第三个参数不为0时表示修改

  val = getenv(name);
  printf("%s = %s\n",name,val);

  /*
  int ret = unsetenv("ABCDEF");
  printf("ret = %d\n",ret );//0

  int ret = unsetenv("ABC=");
  printf("ret = %d\n",ret );//-1
  */
  int ret = unsetenv("ABD");
  printf("ret = %d\n",ret );//0
  
  val = getenv(name);
  printf("%s = %s\n",name,val);//ABD = good-good-study

  return 0;
}
