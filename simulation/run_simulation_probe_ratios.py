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
probe_ratios = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 4, 4.5, 5]
# probe_ratios = [1, 1.4, 2, 2.5, 3, 3.5, 4, 4.5, 5]
"""
for load in loads:
    for probe_ratio in probe_ratios:
        print "Now simulating Sparrow with cancellation, at probe ratio %s" %probe_ratio
        simulation_cancellation.WORK_STEALING = False
        simulation_cancellation.CANCELLATION = True
        simulation_cancellation.NETWORK_DELAY = 10
        simulation_cancellation.PROBE_RATIO = probe_ratio 
        s = simulation_cancellation.Simulation(NUM_JOBS, "probe_ratio_%s_r%s" % (load, probe_ratio), load, DISTRIBUTION)
        s.run()
"""

data = []
data_ideal = []
response_times = []
ideal_response_times = []
response_ratio= []
labels = []
data_ratio = []
"""
for probe_ratio in probe_ratios:
    for load in loads:
        datafile = open('probe_ratio_%s_r%s_response_times.data' % (load, probe_ratio), 'r')
        datareader = csv.reader(datafile, delimiter='\t')
        tmp = 0
        for row in datareader:
            if row[0]=="0.99":
                response_times.append(row[1])
                tmp = row[1]
        datafile = open('probe_ratio_%s_r%s_ideal_response_time.data' % (load, probe_ratio), 'r')
        datareader = csv.reader(datafile, delimiter='\t')
        for row in datareader:
            if row[0]=="0.99":
                ideal_response_times.append(row[1])
                response_ratio.append(float(tmp)/float(row[1]))
"""
for probe_ratio in probe_ratios:
    for load in loads:
        datafile = open('probe_ratio_%s_r%s_response_times.data' % (load, probe_ratio), 'r')
        datareader = csv.reader(datafile, delimiter='\t')
        cdf = []
        for row in datareader:
            if float(row[0]) >= 0.05 and float(row[0])<= 0.95:
                cdf.append(float(row[1]))
        data.append(cdf)
        datafile = open('probe_ratio_%s_r%s_ideal_response_time.data' % (load, probe_ratio), 'r')
        datareader = csv.reader(datafile, delimiter='\t')
        cdf = []
        for row in datareader:    
            if float(row[0]) >= 0.05 and float(row[0])<= 0.95:
                cdf.append(float(row[1]))
        data_ideal.append(cdf)
    
    
    
plt.figure(2)
plt.xticks(range(1,len(probe_ratios)),probe_ratios, rotation=15)
plt.boxplot(data)
plt.show()
    
"""
plt.figure(1)
plt.suptitle('95th-%tile response time vs. load', fontsize=20)

plt.ylabel('response time', fontsize=18)
plt.xlabel('probe ratio', fontsize=16)
plt.plot(probe_ratios, response_times, marker='o', linestyle='--', color = 'r')
plt.plot(probe_ratios, ideal_response_times, marker='o', linestyle='--', color = 'b')
plt.figure(2)

plt.suptitle('95th-%tile response time vs. load ratio', fontsize=20)
plt.plot(probe_ratios, response_ratio, marker='o', linestyle='--', color = 'b')
"""