import csv
import pandas as pd
import os

user_csv_path = "./csv_exported/User_data.csv"
calc_csv_path = "./csv_exported/Calc_datas.csv"
def to_csv(dict_user, dict_calc):
    if dict_user and dict_calc:
        if os.path.isfile(user_csv_path):
            os.remove(user_csv_path)
            df_user = pd.DataFrame((dict_user))
            df_user.to_csv(user_csv_path)
        else:
            df_user = pd.DataFrame((dict_user))
            df_user.to_csv(user_csv_path)
       
        if os.path.isfile(calc_csv_path):
            os.remove(calc_csv_path)
            df_calc = pd.DataFrame((dict_calc))
            df_calc.to_csv(calc_csv_path)
        else:
            df_calc = pd.DataFrame((dict_calc))
            df_calc.to_csv(calc_csv_path)
    elif dict_user:
        if os.path.isfile(user_csv_path):
            os.remove(user_csv_path)
            df_user = pd.DataFrame((dict_user))
            df_user.to_csv(user_csv_path)
        else:
            df_user = pd.DataFrame((dict_user))
            df_user.to_csv(user_csv_path)
    elif dict_calc:
        if os.path.isfile(calc_csv_path):
            os.remove(calc_csv_path)
            df_calc = pd.DataFrame((dict_calc))
            df_calc.to_csv(calc_csv_path)
        else:
            df_calc = pd.DataFrame((dict_calc))
            df_calc.to_csv(calc_csv_path)

#Faltou verificar se o .csv ja existe se já existir vai deletar e criar um novo





