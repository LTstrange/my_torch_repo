# from __future__ import print_function, division
import pandas as pd
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

import warnings
warnings.filterwarnings("ignore")


landmarks_frame = pd.read_csv('data/faces/face_landmarks.csv')

class FaceLandmarksDataset(Dataset):
    def __init__(self, data):
        self.data =

