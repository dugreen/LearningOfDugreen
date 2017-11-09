#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(void) {

  pid_t  pid;
  pid = fork();

  if (pid == -1) {
    /* code */
    perror("fork error!!");
    exit(1);
  }else if (pid > 0) {
    /* code */
    sleep(1);
    printf("parent\n" );
  } else{
    /* code */
    execlp("ls","ls","-l","-a","-h",NULL);
  }
  return 0;
}
