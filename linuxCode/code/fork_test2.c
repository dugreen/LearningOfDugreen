#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(void) {

  int i;
  pid_t pid;

  printf("xxxxxxxxxxxxxxx\n");

  for ( i = 0; i < 5; i++) {
    pid = fork();

    // printf("%d\n",pid );
    if (pid == -1) {
      perror("fork error!");
      exit(1);
    }else if (pid == 0) {
      break;
    }
  }

  if (i < 5) {
    sleep(i);
    printf("i am %d child!,pid = %u,ppid= %u\n",i+1,getpid(),getppid() );
  }else{
    sleep(i);
    printf("i am parent!\n");
  }
  printf("hello\n");

  return 0;
}
