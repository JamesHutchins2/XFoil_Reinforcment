#series of functions for managing the .dat file, and loading the polar file
#will also hold the corrdinates in memory for faster loading speed

import numpy as np
import os
import subprocess

class Airfoil:
    def __init__(self):
        
        self.name = None
        self.start_path = None
        self.end_path = None
        self.cordinates = [[]]
        self.last_CL = None
        self.last_CD = None
        self.last_CM = None
        self.Re = 0
        self.n_iter = 0
        self.alpha_i = 0
        self.alpha_f = 0
        self.alpha_step = 0
        self.viscosity = 0


    def load_cordinates(path, self):
        

        file = os.path.join(path)

        with open(file) as f:
            content = f.readlines()
            self.cordinates = np.array([line.split() for line in content[1:]], dtype=np.float64)
        