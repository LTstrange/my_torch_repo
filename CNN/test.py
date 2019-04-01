import torch
import torch.nn as nn
import torchvision
import os
import matplotlib.pyplot as plt

train_data = torchvision.datasets.MNIST('./mnist', True)
print(train_data.train_labels)


class CNN(nn.Module):
    def __init__(self):
        super


