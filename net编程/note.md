# 网络编程
- 网络:
- 网络协议: 一套规则
- 网络模型:
    - 七层模型-七层
        - 物理层
        - 数据链路层
        - 网络层
        - 传输层
        - 会话层
        - 表示层
        - 应用层
    - 四层模型-实际应用
        - 链路层
        - 网络层
        - 传输层
        - 应用层
    - 每一层都有相应的协议负责交换信息或者协同工作
    - TCP/IP协议族
    - IP地址:负责在网络上唯一定位一个机器
        - IP地址分ABCDE类
        - 是由四个数字段组成,每个数字的取值是0-255
        - 192.168.xxx.xxx:局域网ip
        - 127.0.0.1:本机
        - IPv4,IPv6
    - 端口
        - 范围: 0-65535
            - 知名端口:0-1023
            - 非知名端口: 1024-
# TCP/UDP协议
- UDP: 非安全的不面向链接的传输
    - 安全性差
    - 大小限制64kb
    - 没有顺序
    - 速度快
- TCP
    - 基于链接的通信
- SOCKET编程
    - socket(套接字): 是一个网络通信的端点，能实现不同主机的进程通信,网络大多基于Socket通信
    - 通过IP+端口定位对方并发送消息的通信机制
    - 分为UDP和TCP
    - 客户端Client: 发起访问的一方  
    - 服务器端Server: 接受访问的一方
- UDP 编程
    - Server端流程
        - 1. 建立socket, socket是负责具体通信的一个实例
        - 2. 绑定,为创建的socket指派固定的端口和ip地址
        - 3. 接受对方发送内容
        - 4. 给对方发送反馈,此步骤为非必须步骤
    - Client端流程
        - 1.建立通信的socket
        - 2. 发送内容到指定服务器
        - 3. 接受服务器给定的反馈内容
        - 服务器案例v01
        - 客服端案例vo2
        - 服务器程序要求永久运行,一般用死循环处理
        - 改造的服务器版本v03
- TCP 编程
    - 面向链接的传输,即每次传输之前需要建立一个链接
    - 客户端和服务器两个程序需要编写
    - Server端的编写流程
        a. 建立socket负责的具体通信, 这个socket起始只负责接受对方的请求,真正通信的是链接后从新建立的socket
        b. 绑定端口和地址
        c. 监听接入的访问socket
        d. 接受访问的socket,可以理解接受访问即建立了一个通讯的链接通路
        e. 接受对方的发送内容, 利用接收到的socket接受内容
        f. 如果有必要,给对方发送反馈信息
        g. 关闭链接通路
    - Client端流程
        a. 建立通信socket
        b. 链接对方,请求跟对方建立通路
        c. 发送内容到对方服务器
        d. 接受对方的反馈
        e. 关闭链接通路
    - 案例 v04, v05
    
# FTP编程
- FTP(FileTransferProtocal)文件传输协议
- 用途: 定制一些特殊的上传下载文件的服务
- 用户分类: 登录FTP服务器必须有一个账号
    - Real账户: 注册账户
    - Guest账户: 可能临时对某一类人的行为进行授权
    - Anonymous账户: 匿名账户,允许任何人
- FTP工作流程
    1. 客户端链接远程主机上的FTP服务器
    2. 客户端输入用户名和密码(或者"anonymous"和电子邮箱地址)
    3. 客户端和服务器进行各种文件传输和信息查询操作
    4. 客户端从远程FTP服务器退出,结束传输
 - FTP文件表示
    - 分三段表示FTP服务器上的文件
    - HOST: 主机地址,类似于ftp.mozilla.org,以ftp开头
    - DIR: 目录,表示文件所在本地的路径, 例如pub/android/focus/1.1 -RC1/
    - File: 文件名称, 例如Klar-1.1-RC1.apk
    - 如果想完整精确表示ftp上某一个文件,需要上述三部分组合在一起
    - 案例v06