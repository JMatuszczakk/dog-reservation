#file for data management handling
#can be used for csv, databases, etc

import pandas as pd
import numpy as np
import os
#save sample csv
if not os.path.exists('data/users.csv'):
    df = pd.DataFrame({'username': ['admin', 'user'], 'password': ['admin', 'user']})
    df.to_csv('data/users.csv', index=False)
csv = True

def check_user_password(username, password):
    if csv:
        df = pd.read_csv('data/users.csv')
        for i in range(len(df)):
            if df['username'][i] == username and df['password'][i] == password:
                return True
    return False


def check_user_role(username):
    if csv:
        df = pd.read_csv('data/users.csv')
        for i in range(len(df)):
            if df['username'][i] == username:
                if df['role'][i] == 'admin':
                    return 'admin'
                else:
                    return 'user'
    return 'user'