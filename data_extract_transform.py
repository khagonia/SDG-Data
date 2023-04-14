import pandas as pd
from utilities import *
import os
import time

start = time.perf_counter()

##############################
### SDG Overall Data #########
##############################

df = pd.read_csv(os.path.join(os.getcwd(), "sdg/sdg___overall_data.csv"))

# pad null values
cols = df.columns
df = pad_null(df, list(cols[2:6]), 0)

print(cols)

##############################
### SDG Goal Data ############
##############################

df_goal = pd.read_csv(os.path.join(os.getcwd(), "sdg/sdg___goal_data.csv"))

# pad null values
cols = df_goal.columns
df_goal = pad_null(df_goal, [cols[3]], 'No Data')
summarize_null(df_goal)

##############################
### SDG Definition Data ######
##############################

def_df = pd.read_csv(os.path.join(os.getcwd(),'sdg/sdg_definition.csv'))

# print(def_df['target_19'])

end = time.perf_counter() - start