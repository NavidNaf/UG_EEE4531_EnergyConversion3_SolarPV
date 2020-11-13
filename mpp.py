from typing import OrderedDict
from pvlib import pvsystem
import pandas as pd
import matplotlib.pyplot as plt

info = pvsystem.max_power_point(
    photocurrent=4,
    saturation_current=.0000000000001,
    resistance_series=2,
    resistance_shunt=1,
    nNsVth=152.8,
    d2mutau=0.00020833,
    method='newton'
)

for k, v in info.items():
    print(k, v)
