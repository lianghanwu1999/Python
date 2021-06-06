#TODO 定义：
# 进程 ：（就是操作系统中执行的一个程序），操作系统以进程为单位分配存储空间，每个进程都有自己的地址空间、
# 数据栈以及其他用于跟踪进程执行的辅助数据，操作系统管理所有进程的执行，为它们合理的分配资源
# 线程：进程的"子任务", Word（进程），它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）


#TODO 不使用多进程进行下载
#TODO （小结）不使用多进程进行下载，即使执行两个毫不相关的下载任务，也需要先等待一个文件下载完成后才能开始下一个下载任务
# 很显然这并不合理也没有效率
from random import randint
from time import time,sleep

def download_task(filename):
    print('开始下载%s....' %filename)
    time_to_download = randint(5,10)  #下载时间
    sleep(time_to_download)   #程序执行挂起的时间间隔  单位秒。
    print('%s下载完成！耗费了%d秒'%(filename,time_to_download))

def main():
    start = time()  #开始计时
    download_task('python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()    #结束计时
    print('总耗费了%.2f秒。' %(end -start))

if __name__ == '__main__':
    main()

#TODO 应用多线程下载
#Windows系统没有fork()调用，因此要实现跨平台的多进程编程，
# 可以使用multiprocessing模块的Process类来创建子进程
from multiprocessing import Process
# TODO getpid（取得父进程ID 识别码）
from os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
    print('启动下载进程，进程号[%d].'% getpid())
    print('开始下载%s ....' %filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)    #程序执行挂起的时间间隔（模拟文件下载时间。）
    print('%s下载完成！，耗费了%d 秒' %(filename,time_to_download))


def main():
    start = time() #开始计时
    p1 = Process(target=download_task,args=('Python 从入门到入院.pdf',)) #进程1
    p1.start()  #开始进程
    p2 = Process(target=download_task,args=('Peking Hot.avi',)) #进程2
    p2.start()  #开始进程
    p1.join()   #结束进程
    p2.join()   #结束进程
    end = time() #计时结束
    print('总耗费了%.2f秒.'%(end -start))

if __name__ == '__main__':
    main()

#
#TODO 多线程
from random import randint
from threading import Thread
from time import time,sleep

#TODO 直接使用threading模块的Thread类来创建线程,
# 已有的类(系统使用threading 创建的类)创建新类，因此也可以通过继承Thread类的方式来创建自定义的线程类，
# 然后再创建线程对象并启动线程

class DownloadTask(Thread):
    def __init__(self,filename):
        super().__init__() #重写父类，继承父类的功能
        self._filename = filename

    def run(self):
        print('开始下载%s...'%self._filename)
        time_to_download = randint(5,10)
        sleep(time_to_download)
        print('%s下载完成！耗费了%d秒'%(self._filename,time_to_download))

def main():
    start = time()
    t1 = DownloadTask('python 从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒。'%(end -start))

if __name__ == '__main__':
    main()

#TODO 100个线程向同一个银行账户转账（转入1元钱）的场景（模拟资源会处于“混乱”的状态）
from time import sleep
from threading import Thread

class Account(object):
    """账号"""
    def __init__(self):
        self._balance = 0  #余额
    def deposit(self,money):
        #计算存款后的余额
        new_balance = self._balance + money
        #模拟受理存款业务需要0.01秒的时间
        sleep(0.01)
        #修改账号余额
        self._balance = new_balance

    @property
    def balance(self): #获取余额的值（且保护起来）
        return self._balance

class AddMoneyThread(Thread):
    """存钱"""
    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    #创建100 个存储的线程向同一个账号存钱
    for _ in range(100):
        t = AddMoneyThread(account,1) #存钱1块
        threads.append(t)
        t.start()
        #等所有存款的线程都执行完毕
        for t in threads:
            t.join()
        print('账号余额为：￥%d元' %account.balance)


if __name__ == '__main__':
    main()

#TODO 锁住临界资源
# 某个线程要共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，
# 将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源
#TODO (互斥锁保证了每次只有一个线程进入写入操作，从而保证了多线程情况下数据的正确性)
# 只要一上锁，由多任务变为单任务,相当于只有一个线程在运行，所以只有必须加锁的地方才加锁。


from time import sleep
from threading import Thread,Lock

class  Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self,money):
        #先获取锁才能执行后续的代码
        self._lock.acquire()  #TODO 保持数据的正确性，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改
        try:
            new_balance = self._balance +money
            sleep(0.01)
            self._balance = new_balance
        finally:
            #在finally 中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()   # TODO 将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account,1)
        threads.append(t)
        t.start()
        for t in threads:
            t.join()
    print('账户余额为: ￥%d元' % account.balance)

if __name__ == '__main__':
    main()

#TODO IO编程
# 同步（等待）：第一种是CPU等着，也就是程序暂停执行后续代码，等待磁盘完成再继续执行，IO 同步
# 异步（不等待）：CPU 不等待，磁盘慢慢出来，cpu继续执行下面代码。这叫IO 异步
# 效率：异步远高于同步
# 复杂程度 ：同步简单于异步

#TODO 单线程+异步I/O
# 1.单线程+异步I/O的编程模型称为协程，
# 2.高效率：多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能，
# 3.协程优势：不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，节省线程切换时间。

#TODO 将耗时间的任务放到线程中以获得更好的用户体验。
#如果不使用“多线程”，我们会发现，当点击“下载”按钮后整个程序的其他部分都被这个耗时间的任务阻塞而无法执行了

import time
import tkinter
import tkinter.messagebox

def download():
    #模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('提示','下载完成')

def show_about():
    tkinter.messagebox.showinfo('关于','作者：汉武（V1.0）')

def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost',True) #顶置窗口(创建第一个底层窗口)

    panel = tkinter.Frame(top)  #窗口布局框架。
    button1= tkinter.Button(panel,text='下载',command=download)
    button1.pack(side='left')  #显示出来并放置左边
    button2 = tkinter.Button(panel,text='关于',command=show_about)
    button2.pack(side='right') #显示出来并放置右边
    panel.pack(side='bottom')

    tkinter.mainloop() #整个函数循环起来

if __name__ == '__main__':
    main()

#TODO 多线程 把独立耗时间的线程独立出来（就不会阻塞主线程）
import time
import tkinter
import tkinter.messagebox
from threading import Thread  #多线程

def main():
    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示','下载完成！')
            #启动下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        #禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        #通过daemon 参数将线程设置为你守护线程（主程序退出就不再保留执行）
        #在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于','作者：汉武')  # ('标题','内容')

    window = tkinter.Tk()
    window.title('单线程')
    window.geometry('200x150')
    window.wm_attributes('-topmost',1) #创建顶层窗口

    panel = tkinter.Frame(window)
    button1 = tkinter.Button(panel,text='下载',command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text='关于',command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()
if __name__ == '__main__':
    main()

#TODO 单线程密集型任务： 1~100000000求和的计算密集型任务 （运算4秒）
from time import time

def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()

#TODO 将巨大的文件任务分解成8个进程中去执行（运算0.9秒）
from multiprocessing import Process,Queue
from random import randint
from time import time

def task_handler(curr_list,result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1,100000001)]
    result_queue = Queue()
    index = 0
    #启动8个进程将数据切片进行运算
    for _ in range(8):
        #target 目标对象  ， args = 传参
        p = Process(target=task_handler,args=(number_list[index:index+index+12500000],result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    #开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    #合并执行的结果
    total = 0
    while not result_queue.empty():
        total +=result_queue.get()
    print(total)
    end = time()
    print('Execution time:',(end -start),'s' ,sep='')

if __name__ == '__main__':
    main()
