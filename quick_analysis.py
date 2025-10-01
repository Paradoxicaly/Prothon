"""
FAST PROTHON ANALYSIS
Simple script that runs the analysis efficiently
"""

from Prothon import Prothon
import numpy as np
import os

data_folder = r'C:\Users\derri\OneDrive\Documents\Prothon\ubiquitin-md-generated-ensemble'
data = [
    os.path.join(data_folder, 'Q99.dcd'),
    os.path.join(data_folder, 'Q75.dcd'),
    os.path.join(data_folder, 'Q80.dcd'),
    os.path.join(data_folder, 'Q85.dcd'),
    os.path.join(data_folder, 'Q90.dcd'),
    os.path.join(data_folder, 'Q95.dcd')
]
topology = os.path.join(data_folder, 'topology.pdb')

print("Starting Prothon analysis...")
print(f"Processing {len(data)} ensembles")

prothon = Prothon(data=data, topology=topology, verbose=False)
ensembles = prothon.ensemble_representation(measure='CBCN')
x_min, x_max = (np.min(ensembles), np.max(ensembles))

results = []
names = ['Q75', 'Q80', 'Q85', 'Q90', 'Q95']

for i, ensemble in enumerate(ensembles[1:]):
    d = prothon.dissimilarity(ensemble, ensembles[0], x_min=x_min, x_max=x_max)
    results.append(d[0])
    print(f"{names[i]} vs Q99: {d[0]:.4f}")

print(f"\nResults: {results}")
print("Done!")