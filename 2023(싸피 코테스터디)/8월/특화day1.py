# 혹시 사용할 수도 있는 라이브러리는 모두 import 해놓았습니다. 혹시 더 필요할 경우 추가하셔도 무방합니다.
from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#답
x_train = torch.FloatTensor([[10], [11], [14], [18], [19], [22], [24]])
y_train = torch.FloatTensor([[45], [50], [55], [70], [58], [80], [85]])
print(x_train.shape, '|', x_train.dim())