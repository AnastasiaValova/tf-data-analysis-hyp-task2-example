import pandas as pd
import numpy as np
from scipy import stats


chat_id = 225497605 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.07
    stat, p_value = stats.ks_2samp(x, y)
    return ( p_value < alpha)
