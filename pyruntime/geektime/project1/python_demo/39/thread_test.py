import  threading
import  time
from threading import current_thread

def myThread(arg1, arg2):
    print(current_thread().getName(),'start')
    print('%s %s'%(arg1, arg2))
    time.sleep(1)
    print(current_thread().getName(),'stop')


for i in range(1,6,1):
    # t1 = myThread(i, i+1)
    t1 = threading.Thread(target=myThread,args=(i, i+1))
    t1.start()

#t1.join()

print(current_thread().getName(),'end')

#运行的效果是，主线程先结束，thead线程依次结束

#如果我们期望thead线程先结束，主线程最后结束，需要用t1.join()方法
