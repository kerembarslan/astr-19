import numpy as np
import pandas as pd
import math

def calculate_sin(x):
    return math.sin(x)

def calculate_cos(x):
    return math.cos(x)

x_value = np.linspace(0, 2*np.pi, 1000)

sin_value = [calculate_sin(x) for x in x_value]

cos_value = [calculate_cos(x) for x in x_value]

for i in range(10):
    print(f"{sin_value[i]:.4f}|{cos_value[i]:.4f}")