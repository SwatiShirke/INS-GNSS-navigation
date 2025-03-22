"""This file constains implementation of observation model for GNSS system."""


import numpy as np
from scipy.spatial.transform import Rotation as R
import earth

class Observation:
    def __init__(self, filename):        
        self.filename = filename
        self.RATE = 7.292115e-5
        self.prev_omega_en = np.array([0, 0, 0])
        self.prev_omega_ie = np.array([0, 0, 0])
        self.bias_g = np.array([1, 1, 1]) * 0.01
        self.bias_a = np.array([1, 1, 1]) * 0.01   