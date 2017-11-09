#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

int main(void) {
  /* code */
  pid_t pid;

  printf("xxxxxxxxxxxxxxx\n");

  pid = fork();

  if (pid == -1) {
    /* code */
    perror("fork error!");
    exit(1);
  }else if (pid == 0) {
    /* code */
    printf("i am child!pid = %u,ppid = %u\n",getpid(),getppid() );
  }else{
    /* code */
    printf("i am parent!pid = %u,ppid = %u\n",getpid(),getppid() );
  }

  printf("xxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyyyy\n");
  return 0;
}
