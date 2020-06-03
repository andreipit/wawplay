import torch
from tqdm import tqdm
from ..utils import EarlyStopping

try:
    import torch_xla.core.xla_model as xm

    _xla_available = True
except ImportError:
    _xla_available = False

try:
    from apex import amp

    _apex_available = True
except ImportError:
    _apex_available = False


class Engine:
    @staticmethod
    def train(
        data_loader
    ):
        print("engine training data_loader=",data_loader)
        return 999

    
