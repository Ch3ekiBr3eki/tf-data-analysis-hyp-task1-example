import pandas as pd
import numpy as np
from scipy import stats

chat_id = 323297403 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt

    p_pool = (x_success + y_success) / (x_cnt + y_cnt)
    se_pool = np.sqrt(p_pool * (1 - p_pool) * (1 / x_cnt + 1 / y_cnt))

    z_score = (p1 - p2) / se_pool

    alpha = 0.02
    z_crit = stats.norm.ppf(1 - alpha/2)

    return abs(z_score) > z_crit
