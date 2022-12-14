"""

@author: Giovanni Arlotta

"""

"""
System state: number of costumers in the queue, server state

Entities: costumer generator, costumers, queue

Events: costumer arrival, service starting (dependent event), costumer, departure, simultion end

Activities: inter-arrival and service times

Delays: costumer waiting times

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame()

np.random.seed(0)
class Simulation:
    def __init__(self):
        self.queue_len = 0 # total lenght
        
        #SIMULATION VARIABLES

        self.clock = 0.0 # clock for events
        self.time_arrival = self.generate_interarrival() # time arrival
        self.time_depart  = 0 #time depart
        self.time_in_service = self.generate_service()
        self.state = 0 # state of in-service #### 0: FREE !--! 1: BUSY
        
        #STATISTICAL COUNTERS
        
        self.num_arrivals = 0
        self.num_departs = 0
        self.total_wait = 0.0

    def inc_time(self):
        time_event = self.time_in_service # time that passed compute by take the minimum value between the next arrival or next departure
        self.total_wait += self.queue_len*(time_event-self.clock) # update total wait by consider total number customers in a system * the time that passed (which is t_event - clock)
        #t_event-clock give me the step time until the duration from the last time step until the next event that's currently being processed
        self.clock = time_event # update the clock to the current event

        utilization.append(self.total_wait)

        if self.state == 0: # if arrival event happens first (arrival time less than departure time)
            self.handle_arrival_event()
        else:
            self.handle_depart_event()
        wait_t.append(time_event)
        
    def handle_arrival_event(self):
        self.queue_len = self.queue_len +1 # increment number in the system
        self.num_arrivals = self.num_arrivals +1 # increment number of arrivals
        self.time_in_service = self.generate_service()
        if self.queue_len <= 1: # if the customer who arrival is the only in the system
            self.time_depart = self.clock + self.time_in_service # in this case we set his departure time at the clock time + generate the service period for this customer
             # so if he is the only customer we schedule their departure
        else:
            self.time_arrival = self.clock + self.generate_interarrival() # otherwhise we need to see if there's more arrivals to process, by assign to next arrival clock + whatever value gets generated by interarrival period
    
    def handle_depart_event(self):
        self.queue_len = self.queue_len -1
        self.num_departs = self.num_departs +1
        if self.queue_len > 0:
            self.time_depart = self.clock + self.generate_service()
            self.state = 1
        else:
            self.time_depart = float('inf') # if there aren't any others customers in the system
            self.state = 0

    def generate_interarrival(self):
        return np.random.exponential(1./3) # Generate random exponential for generate random time inter_arrival
    
    def generate_service(self):
        return np.random.exponential(1./4)  # Generate random exponential for generating random time for service

s = Simulation()
wait_t = []
queue_c = []
utilization = []
event_calendar = []
services_times = []
val_utilization = 0
exp_queue_len = 0

for i in range(10):
    s.inc_time()
    queue_c.append(s.queue_len)
    services_times.append(s.time_in_service)
    event_list = {  #CREATING EVENT CALENDAR
        "Iteration": "I_"+str(i),
        "Queue_Len": queue_c,
        "Services_Times": services_times
    }
    event_calendar.append(event_list)
    print(event_calendar)


to = utilization[0]
tf = utilization[9]
val_utilization = 1-(to/tf)

#exp_queue_len = (1/val_utilization)*(sum(i*utilization)+(sum((i+1)*utilization)))

exp_wait_time=(sum(wait_t)/len(wait_t))
#EXP QUEUE
print("Queue costumers :",queue_c)

#UTILIZATION
print("Val Utilization :",val_utilization)
#EXP WAITING TIME
print("Expected waiting Time",exp_wait_time)

#EXP QUEUE LEN
print("Expect Queue Len : ",exp_queue_len)
#need to do last operation to compute everything

df["services_times"] = services_times

plt.hist(services_times)
plt.xlabel('Waiting Time')
plt.ylabel('Customers')
plt.show()