import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in json data
with open('generated_songs.json') as f:
    data = json.load(f)

print(data[0].keys())
