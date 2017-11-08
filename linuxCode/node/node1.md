### 程序与进程

* 程序：二进制文件，不占用系统资源。
* 进程：活跃的程序。

---

### 并发
* 并行运行

---

### 单道程序设计模型　
例：ＤＯＳ模型
### 多道程序设计模型　
例：安卓系统

---

### 中央处理器 CPU
- 存储介质
###### 寄存器
##### cache
#### 内存 (G)
###　硬盘 (T)
##　网络 (large)
- 预取器 (预取指令)
- 译码器　(译码)
- ALU (算数逻辑单元)
- 寄存器堆　

---

### MMU
虚拟地址：可用的地址空间４g
*实现虚拟地址与实际物理地址的对应*
*修改内存的访问级别*

---

### 进程控制块　PCB
*linux内核的进程控制块是task_struct结构体*
进程id
进程的状态 运行 就绪 挂起(阻塞 等待) 停止
描述虚拟地址的信息
描述控制终端的信息
当前工作目录
umask掩码
文件描述符表
和信号相关的信息
用户id和组id
会话和进程组
进程可以使用的资源上线

---

### 环境变量
字符串
有统一格式 名=值
- dugeen@du:~$ echo $SHELL
/bin/bash
- dugeen@du:~$ echo $HOME
/home/dugeen
- dugeen@du:~$ echo $LANG
zh_CN.UTF-8
- dugeen@du:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
