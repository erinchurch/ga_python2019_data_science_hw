import pandas as pd
import glob




def files_to_df(fname):
    acq_header_file = pd.read_csv("header_aquisition_file.txt", sep=",")
    # print("headers file", acq_header_file.head())

    columns = acq_header_file["Field Name"]
    # print("headers", columns)

    # index = 'LOAN IDENTIFIER'
    # index_col = index
    filter_columns = ['LOAN IDENTIFIER', 'ORIGINAL INTEREST RATE', 'ORIGINAL UPB',
                      'ORIGINATION DATE', 'ORIGINAL LOAN-TO-VALUE (LTV)',
                      'ORIGINAL COMBINED LOAN-TO-VALUE (CLTV)', 'ORIGINAL DEBT TO INCOME RATIO',
                      'BORROWER CREDIT SCORE AT ORIGINATION', 'CO-BORROWER CREDIT SCORE AT ORIGINATION']

    # TO FILTER FOR SPEED, nrows=1000, FILTERED FOR 1000 ROWS, TURN THAT OFF FOR FINAL SUBMISSION
    df = pd.read_csv(fname, sep="|",
                     header=None, names=columns, usecols=filter_columns, infer_datetime_format=True, )

    return df


def df_to_files(df_name, fname):
    df_name.to_csv(fname, sep=',')

    return

files = glob.glob('acq_files_orig/*')

print(files)
print(files[0])
counter = 0

dfs = []

for file in files:
    name = file.replace('acq_files_orig/', '')
    print(name)
    df = files_to_df(file)
    df['SOURCE'] = name
    print(df.head())
    dfs.append(df)

df_all = pd.concat(dfs,axis=0, ignore_index=True)


print(df_all.head())
print(df_all.tail())
print(df_all.shape)
print(df_all.columns)

name_all = 'acq_files_analysis/acq_file_all.csv'

df_to_files(df_all, name_all)



