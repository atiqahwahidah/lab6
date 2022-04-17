#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void)
{
char name[5];
for (int i=1;i<5;i++)
{
  printf("Enter name: ");
  scanf("%s",name);
  printf("Name:%s\n ",name);
  pid_t pid=fork();
  if (pid==0)
   {
     printf("Child process => PPID=%d,PID=%d\n",getpid(),getpid());
     exit(0);
   }
else
   {
     printf("Parent process => PID=%d\n",getpid());
     printf("Waiting for child processes to finish...\n");
     wait(NULL);
     printf("Job is done.\n");
   }
}
return EXIT_SUCCESS;
}
