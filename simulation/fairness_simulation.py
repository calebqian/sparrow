"""
Python script to simulation the Sparrow probe ratio adapting mechanism
Authors: Jianxiong Gao, Junle Qian

"""


import matplotlib.pyplot as plt
import csv

import fairness
import util

NUM_JOBS = 10000
DISTRIBUTION = util.TaskDistributions.EXP_JOBS
#loads = [0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95]
loads = [0.95]

loads.reverse()
""" 95th percentile, load """
#probe_ratios = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]
#probe_ratios = [1, 1.4, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]



for load in loads:
    print "Now simulating Sparrow with cancellation, with fairness metrics"
    fairness.WORK_STEALING = False
    fairness.CANCELLATION = True
    s = fairness.Simulation(NUM_JOBS, "fairness_%s" % load, load, DISTRIBUTION)
    fair_list =  s.fairness_pair_list
    s.run()

