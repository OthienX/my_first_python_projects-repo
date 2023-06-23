import sched
import time
def job():
    print("its reading time>>>>>>>>>>>>")
    def coding():
        print("its coding time>>>>>>>>>>>>>>")
   #time
        sched.every(10).seconds.do(job)
           sched.every(20).seconds.do(coding)

   while true:
       sched.run.pending()
       time.sleep(1)