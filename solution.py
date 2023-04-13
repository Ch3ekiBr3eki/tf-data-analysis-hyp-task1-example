import pandas as pd
import numpy as np
from scipy import stats

chat_id = 323297403 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p_pool = (x_success + y_success) / (x_cnt + y_cnt)
    
    se = np.sqrt(p1 * (1 - p1) / x_cnt + p2 * (1 - p2) / y_cnt)
    z_score = (p1 - p2) / se
    
    alpha = 0.02
    z_crit = stats.norm.ppf(1 - alpha/2)
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    
    if abs(z_score) > z_crit and p_value < alpha:
        return True
    else:
        return False
