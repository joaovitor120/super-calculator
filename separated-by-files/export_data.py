import csv
import pandas as pd

user_csv_name = "User_data.csv"
calc_csv_name = "Calc_datas.csv"
def to_csv(dict_user, dict_calc):
    if dict_user and dict_calc:
        df_user = pd.DataFrame(f'./csv_exported/{dict_user}')
        df_user.to_csv(user_csv_name)
        df_calc = pd.DataFrame(f'./csv_exported/{dict_calc}')
        df_calc.to_csv(calc_csv_name)
    elif dict_user:
        df_user = pd.DataFrame(f'./csv_exported/{dict_user}')
        df_user.to_csv(user_csv_name)
    elif dict_calc:
        df_calc = pd.DataFrame(f'./csv_exported/{dict_calc}')
        df_calc.to_csv(calc_csv_name)

#Faltou verificar se o .csv ja existe se já existir vai deletar e criar um novo





