import sys
import os
import json

import pandas as pd
import numpy as np
from pandas import ExcelFile

print(f'os.getcwd(): {os.getcwd()}')
df = pd.read_excel('txpl_project_updated.xlsx')
print(f"df.shape: {df.shape}")