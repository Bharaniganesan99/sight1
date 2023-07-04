##import threading
##import time
##
##
##def seq():
##    print("thread1")  
##    print("thread2")
##    multi()
##
##def multi():
##    print("thread3")  
##    print("thread4")
##    time.sleep(3)
##
####print("sequencial")
##
##
####start_time = time.time()
######print(start_time)
####seq()
####multi()
####end_time = time.time()
######print(end_time)
####exe_time=end_time-start_time
######print(exe_time)
##
##
####print("multithreading")
##
##
##thread1=threading.Thread(target=multi)
##thread2=threading.Thread(target=seq)
##
####start_time = time.time()
####print(start_time)
##
##thread1.start()
##thread2.start()
##
##thread1.join()
##thread2.join()
##
##seq()
##multi()
##end_time=time.time()
##print(end_time)

##exe_time=end_time-start_time
##print(exe_time)






##import threading
##import time
##
##
##def seq():
##    print("thread1")  
##    print("thread2")
##    print("thread3")
##
##def multi():
##    print("thread4")  
##    print("thread5")
##    print("thread6")
##    time.sleep(3)
##    
##print("sequencial")
##
##seq()
##multi()
##
##print("multithreading")
##
##
##thread1=threading.Thread(target=multi)
##thread2=threading.Thread(target=seq)
##
##thread1.start()
##thread2.start()
##
##thread1.join()
##thread2.join()
##
##






##
##import threading
##import time
##
##
##def seq():
##    print("thread1")  
##    print("thread2")
##    print("thread3")
##
##def multi():
##    print("thread4")  
##    print("thread5")
##    print("thread6")
##    time.sleep(3)
##    
##print("sequencial")
##
####seq()
##multi()
##
##print("multithreading")
##
##
####thread1=threading.Thread(target=multi)
##thread2=threading.Thread(target=seq)
##
####thread1.start()
##thread2.start()
##
####thread1.join()
##thread2.join()




##import threading
##import time
##def one(name,delay):
##    new()
##    print(name,token)
##
##token = 0
##def new():
##    global token
##    token = token + 1
##t1 = threading.Thread(target = one,args =["dhoni",2])
##t2 = threading.Thread(target = one ,args = ["virat",4])
##t3 = threading.Thread(target = one,args=["bharani",3])
##
##t1.start()
##t2.start()
##t3.start()
##
##t1.join()
##t2.join()
##t3.join()
##
##






































