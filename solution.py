import pandas as pd
import numpy as np
from scipy import stats


chat_id = 225497605 # Ваш chat ID, не меняйте название переменной

def solution2(x: np.array, y: np.array) -> bool:
    alpha = 0.07
    return (stats.anderson_ksamp([x, y]).significance_level < alpha)
