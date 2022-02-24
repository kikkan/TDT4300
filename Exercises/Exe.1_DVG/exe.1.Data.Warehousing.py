import numpy as np
import matplotlib.pyplot as plt
import csv

f1 = open('data\\airlines.csv', "r")
airlines = csv.reader(f1)
for l in airlines:
    print(l)
