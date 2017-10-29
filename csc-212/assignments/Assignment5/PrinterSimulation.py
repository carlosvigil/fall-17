"""
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
"""

import random
from Queue import Queue


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.page_rate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


class Simulation:
    """Constructor for simulation class."""
    def __init__(self, cfg):
        self.duration_sim = cfg['duration_sim']
        self.min_task = cfg['min_task']
        self.max_task = cfg['max_task']
        self.num_devices = cfg['num_devices']
        self.page_rate_one = cfg['page_rate_one']
        self.page_rate_two = cfg['page_rate_two']

        if self.num_devices == 1:
            self.device = Printer(self.page_rate_one)
        else:
            self.device = [Printer(self.page_rate_one), Printer(self.page_rate_two)]

        self.print_queue = Queue()
        self.wait_times = []

    def start(self):
        """Use the Boolean attribute to start simulation."""
        self.single_device_sim() if self.num_devices == 1 else self.dual_device_sim()

    def single_device_sim(self):
        """A simulation with a single printing device."""
        for current_sec in range(self.duration_sim):
            if self.new_print_task():
                task = Task(current_sec)
                self.print_queue.enqueue(task)

            if (not self.device.busy()) and (not self.print_queue.is_empty()):
                next_task = self.print_queue.dequeue()
                self.wait_times.append(next_task.wait_time(current_sec))
                self.device.start_next(next_task)

            self.device.tick()
        self.avg_wait()

    def dual_device_sim(self):
        """A simulation with two printing devices."""
        for current_sec in range(self.duration_sim):
            if self.new_print_task():
                task = Task(current_sec)
                self.print_queue.enqueue(task)

            if (not self.device[0].busy()) and (not self.print_queue.is_empty()):
                next_task = self.print_queue.dequeue()
                self.wait_times.append(next_task.wait_time(current_sec))
                self.device[0].start_next(next_task)

            elif (not self.device[1].busy()) and (not self.print_queue.is_empty()):
                next_task = self.print_queue.dequeue()
                self.wait_times.append(next_task.wait_time(current_sec))
                self.device[1].start_next(next_task)

            self.device[0].tick()
            self.device[1].tick()
        self.avg_wait()

    def avg_wait(self):
        wait = sum(self.wait_times)/len(self.wait_times)
        print("Average Wait {:>6.2f} secs {:>3} tasks remaining."
              .format(wait, self.print_queue.size()))

    def new_print_task(self):
        num = random.randrange(1, 181)
        if num == 180:
            return True
        else:
            return False


def read_config():
    """Reads the configuration for the printer simulation from a text file."""
    cfg = {}
    with open('sim_config.txt') as cfg_file:
        cfg['duration_sim'] = int(cfg_file.readline())
        cfg['num_sims'] = int(cfg_file.readline())
        cfg['min_task'] = int(cfg_file.readline())
        cfg['max_task'] = int(cfg_file.readline())
        cfg['num_devices'] = int(cfg_file.readline())
        cfg['page_rate_one'] = int(cfg_file.readline())
        cfg['page_rate_two'] = cfg_file.readline()
    # Check values
    # config line 1
    if 3600 < cfg['duration_sim'] > 36000:
        raise ValueError('Line 1 of config is out of the range 3600-36000')
    # 2
    if 1 < cfg['num_sims'] > 100:
        raise ValueError('Line 2 of config is out of the range 1-100')
    # 3
    if 1 < cfg['min_task'] > 100:
        raise ValueError('Line 3 of config is out of the range 1-100')
    # 4
    if 1 < cfg['max_task'] > 100 or cfg['max_task'] < cfg['min_task']:
        raise ValueError(
            'Line 4 of config is out of the range 1-100 and the minimum')
    # 5
    if 1 < cfg['num_devices'] > 2:
        raise ValueError('Line 5 of config is out of the range 1-2')
    # 6
    if 1 < cfg['page_rate_one'] > 50:
        raise ValueError('Line 6 of config is out of the range 1-50')
    # 7
    if cfg['page_rate_two'] != '':
        cfg['page_rate_two'] = int(cfg['page_rate_two'])
        if 1 < int(cfg['page_rate_two']) > 50:
            raise ValueError('Line 7 of config is out of the range 1-50')
    return cfg


def main():
    cfg = read_config()
    for sim in range(cfg['num_sims']):
        Simulation(cfg).start()


if __name__ == "__main__":
    main()
