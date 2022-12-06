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

class Simulation:
    def __init__(self):
        self.num_in_system = 0
        
        #SIMULATION VARIABLES

        self.clock = 0.0
        self.t_arrival = self.generate_interarrival()
        self.t_depart  = float('inf') #for now set to infinity
        
        #STATISTICAL COUNTERS
        
        self.num_arrivals = 0
        self.num_departs = 0
        self.total_wait = 0.0

    def advance_time(self):
        pass
    def handle_arrival_event(self):
        pass
    def handle_depart_event(self):
        pass
    def generate_interarrival(self):
        return np.random.exponential(1./3) # Generate random exponential
    def generate_service(self):
        return np.random.exponential(1./4)  # Generate random exponential

s = Simulation()