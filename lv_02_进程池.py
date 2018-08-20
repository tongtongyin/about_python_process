from multiprocessing import Pool
import os,time

def worker(name):
    """定义子进程的执行函数"""
    print("this is child process pid = %d" % (os.getpid()))
    start = time.time()
    time.sleep(2)
    end = time.time()
    print("this is child process name = %s; time = %d" %(name, end-start))
    print("")

if __name__ == "__main__":
    # 创建进程池
    p = Pool(3)
    # 每三个进程同时执行
    for x in range(10):
        # 创建进程对象，异步
        p.apply_async(worker,args=("text",))
        # p.apply(worker,args=(x,))     同步
    # 关闭进程池
    p.close()
    p.join()

    print("end")

"""异步：首先申请三个进程，2秒之后，再把这三个进程同时进行 在把这三个进程同时进行"""