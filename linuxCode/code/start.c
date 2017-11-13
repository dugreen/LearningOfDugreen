#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(void) {

    int i;
    pid_t  pid;

    for ( i = 0; i < 3; i++) {
    pid = fork();

    // printf("%d\n",pid );
    if (pid == -1) {
      perror("fork error!");
      exit(1);
    }else if (pid == 0) {
      break;
    }
    }

    if (i == 0) {
    execl("/usr/bin/netease-cloud-music","music",NULL);
    }else if (i == 1) {
    execl("/usr/bin/cairo-dock","cairo",NULL);
    }else if (i == 2) {
    execlp("back","back",NULL);
    }
    return 0;
}
