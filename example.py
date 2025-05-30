# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:50:25 2016

@author: raneem
"""

from optimizer import run

# Select optimizers
# "SSA","PSO","GA","BAT","FFA","GWO","WOA","MVO","MFO","CS","HHO","SCA","JAYA","DE"
optimizer = ["PSO","GA"]

# Select benchmark function"
# "F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","F13","F14","F15","F16","F17","F18","F19"
# "Ca1","Ca2","Gt1","Mes","Mef","Sag","Tan","Ros"
objectivefunc = ["Mobile1"]

# Select number of repetitions for each experiment.
# To obtain meaningful statistical results, usually 30 independent runs are executed for each algorithm.
NumOfRuns = 2

# Select general parameters for all optimizers (population size, number of iterations) ....
params = {"PopulationSize": 100, "Iterations": 1000}

# Choose whether to Export the results in different formats
export_flags = {
    "Export_avg": True,
    "Export_details": True,
    "Export_convergence": True,
    "Export_boxplot": True,
}

run(optimizer, objectivefunc, NumOfRuns, params, export_flags)


