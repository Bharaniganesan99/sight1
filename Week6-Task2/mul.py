
import threading
count=0

def count_up():
    global count
    while count<10:
        count+=1
        print(count)

thread1 = threading.Thread(target=count_up)
thread2 = threading.Thread(target=count_up)

thread1.start()

thread1.join()
thread2.start()
thread.join()

for i in range(1,5):
    print(i)
        
thread.join()
