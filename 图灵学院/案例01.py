import time
import threading as thread

def loop1():
    print("My world!", time.ctime())
    time.sleep(2)
    print("我是参数")
    time.sleep(4)
    print("You world!", time.ctime())

def loop2():
    print("You world!", time.ctime())
    time.sleep(1)
    print("我出来了")
    time.sleep(3)
    print("My world!", time.ctime())

def main():
    print("startling at:", time.ctime())
    thread._start_new_thread(loop1,())
    thread._start_new_thread(loop2,())
    print("All done:", time.ctime())

if __name__ == '__main__':
    main()

    while True:
        time.sleep(1)