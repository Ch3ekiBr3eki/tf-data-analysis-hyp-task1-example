import pandas as pd
import numpy as np


chat_id = 323297403 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n1 = x_cnt
    n2 = y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    n1_exp = n1 * p
    n2_exp = n2 * p
    
    chi_sq = ((x_success - n1_exp) ** 2) / n1_exp + ((y_success - n2_exp) ** 2) / n2_exp
    
    df = 1
    
    critical_value = stats.chi2.ppf(0.98, df)
    
    if chi_sq > critical_value:
        return True
    else:
        return False
