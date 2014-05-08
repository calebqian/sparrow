"""
Python script to simulation the Sparrow probe ratio adapting mechanism
Authors: Jianxiong Gao, Junle Qian

"""


import matplotlib.pyplot as plt
import csv

import simulation_cancellation
import util

NUM_JOBS = 10000
DISTRIBUTION = util.TaskDistributions.EXP_JOBS
#loads = [0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95]
loads = [0.95]

loads.reverse()
""" 95th percentile, load """
#probe_ratios = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]
#probe_ratios = [1, 1.4, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
delays = [0.5, 5, 15, 20, 25, 50]

"""
for load in loads:
    for delay in delays:
        print "Now simulating Sparrow with cancellation, at network delay %s" %delay
        simulation_cancellation.WORK_STEALING = False
        simulation_cancellation.CANCELLATION = True
        simulation_cancellation.NETWORK_DELAY = delay 
        s = simulation_cancellation.Simulation(NUM_JOBS, "delay_%s_r%s" % (load, delay), load, DISTRIBUTION)
        s.run()
"""
data = []
response_times = []
ideal_response_times = []
response_ratio= []
for delay in delays:
    for load in loads:
        datafile = open('delay_%s_r%s_response_times.data' % (load, delay), 'r')
        datareader = csv.reader(datafile, delimiter='\t')
        tmp = 0
        for row in datareader:
            if row[0]=="0.95":
                response_times.append(row[1])
                tmp = row[1]
                break
        datafile = open('delay_%s_r%s_ideal_response_time.data' % (load, delay), 'r')
        datareader = csv.reader(datafile, delimiter='\t')
        for row in datareader:
            if row[0]=="0.95":
                ideal_response_times.append(row[1])
                response_ratio.append(float(tmp)/float(row[1]))
                break

    
    
plt.figure(1)
plt.suptitle('95th-%tile response time vs. network delay', fontsize=20)

plt.ylabel('response time', fontsize=18)
plt.xlabel('network delays(ms)', fontsize=16)
plt.plot(delays, response_times, marker='o', linestyle='--', color = 'r')
plt.plot(delays, ideal_response_times, marker='o', linestyle='--', color = 'b')
plt.figure(2)

plt.suptitle('95th-%tile response time vs. network delay ratio', fontsize=20)
plt.plot(delays, response_ratio, marker='o', linestyle='--', color = 'b')