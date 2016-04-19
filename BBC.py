import os
import numpy as np
import pylab as plt
import pandas as pd
import numpy as np
from Bio import Geo

def load_geo(myfile):
    handle = open(myfile)
    records = Geo.parse(handle)
    return records
    
records = load_geo('data/GSE45604_family.soft')

print(records)

# loop over records
for r in records:    
    
    rea = r.entity_attributes
    print(rea)
