from multiprocessing import Process
import os


def child_process(name):
    """创建一个子进程要执行的代码的函数"""
    print("it is a child process name is %s : pid = %d"%(name,os.getpid()))


if __name__ == "__main__":
    print("father process")
    # 创建一个进程对象第一个参数target = 进程实例所调用对象
    # 第二个参数args=传入一个元组作为子进程函数的参数
    p = Process(target=child_process,args=("text",))
    # 调用子进程执行方法
    p.start()
    # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
