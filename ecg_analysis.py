import numpy as np, os, sys, joblib
import pandas as pd
from scipy.io import loadmat
import matplotlib.pyplot as plt
from Ecg import Ecg
import visualise


# Load challenge data.
def load_challenge_data(header_file):
    with open(header_file, 'r') as f:
        header = f.readlines()
        print(header)
    mat_file = header_file.replace('.hea', '.mat')  # Get corresponding Matlab file
    x = loadmat(mat_file)
    recording = np.asarray(x['val'], dtype=np.float64)
    return recording, header


# Get ECG info from first line of header
def get_ecg_info(header):
    global name, leads  # TODO fix scope
    info = header[0].split(',')[0].split(' ')
    name = info[0]
    leads = info[1]


rec, hdr = load_challenge_data("Resources/Training_2/Q0001.hea")
get_ecg_info(hdr)

# create new ECG object
ecg = Ecg(name, leads)
ecg.to_string()

# visualise.plot_twelve_lead(rec)
visualise.plot_lead_single(rec, "V2")

plt.show()
