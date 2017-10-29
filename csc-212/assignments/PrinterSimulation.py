'''
Simulation of printer queue in a computer lab with students
submitting print tasks.  Objective: estimate task waiting time in queue
for different printer print rates.

Assumptions: On average, there are 10 students in the lab.  A student
sends two print jobs on average, 1-20 pages long (equally likely).
Printer can print in draft mode (10 ppm) or high quality (5 ppm).

Observations: With 10 students in the lab at any given time printing twice,
there are 20 print jobs per hour (or every 3600 seconds). So, we expect to
see 1 job every 180 seconds (20 tasks / 3600 seconds).

Simulation logic:
1. Create a queue of print tasks. Each task will be given a timestamp
upon its arrival. The queue is empty to start.

2. For each second (current_second):
• Does a new print task get created? If so, add it to the queue with
  the current_second as the timestamp.
• If the printer is not busy and if a task is waiting,
   – Remove the next task from the print queue and assign it to
  the printer.
   – Subtract the timestamp from the current_second to compute the waiting
  time for that task.
   – Append the waiting time for that task to a list for later processing.
   – Based on the number of pages in the print task, figure out how much
     time will be required.
• The printer now does one second of printing if necessary. It also subtracts
   one second from the time required for that task.
• If the task has been completed, in other words the time required has reached
   zero, the printer is no longer busy.

3. After the simulation is complete, compute the average waiting time from
   the list of waiting times generated.
'''

from Queue import Queue
import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.is_empty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." \
          %(averageWait,printQueue.size()))


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def main():
    # run simulation 10 times
    for i in range(10):
        simulation(3600, 10)

if __name__ == "__main__":
    main()
