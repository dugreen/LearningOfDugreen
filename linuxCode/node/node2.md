### 进程控制
* fork函数
返回值有两个：一个进程-->两个进程-->各自对fork做返回
返回子进程id （父进程）
返回0 （子进程）

---

### exec函数族
- execlp函数
借助PATH环境变量,执行系统可执行程序
- execcl函数
加载一个进程，通过 路径+程序名 来加载。（执行自定义可执行程序）

---

### 回收子进程
- 僵尸进程
进程终止，父进程尚未回收，子进程残留资源（PCB）存放于内核中，变成僵尸进程
- 孤儿进程
父进程死的早，子进程成为孤儿进程，父进程成为init进程（回收孤儿进程）

wait(status):返回：成功：pid 失败:-1
status:传出参数
1.阻塞等待子进程
2.回收子进程资源
3.获取子进程结束状态

###
###
