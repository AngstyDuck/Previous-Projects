import os
from firebase import firebase
import time
import numpy as np
import pandas as pd
import pickle


#
# sub_dataframe = pd.DataFrame({'coefficient of x':[1.28904693],'coefficient of c':[-6.55107321]})
# pickle_out = open(r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\linear_regression_coefficient.pickle', 'wb')
# pickle.dump(sub_dataframe, pickle_out)
# pickle_out.close()
#
# print('done')
#
filename = r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\linear_regression_coefficient.pickle'
with open(filename,'rb') as f:
    model = pickle.load(f)
print(model)


# #For pandas to open and print an excel file
# file_read = pd.ExcelFile(r"C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\temp_51.xlsx")
# sheet_1 = pd.read_excel(r"C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\temp_51.xlsx",sheet_name=0)
#
# print(sheet_1)
# print(sheet_1['time (s)'])


