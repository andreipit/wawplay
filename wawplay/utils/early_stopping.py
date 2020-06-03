import torch
import numpy as np


class EarlyStopping:
    def __init__(self, mode="max"):
        self.mode = mode

    def __call__(self):
        print("mode=",self.mode)
        

    def save_checkpoint(self):
        print("save_checkpoint with mode=",self.mode)
