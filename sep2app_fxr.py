## separate to app.fxr

import pandas as pd
import os

def sep2app_fxr(data):
    app_data = {}  # Dictionary to store application data

    for index, row in data.iterrows():
        app_name = row['Application Name']
        if app_name not in app_data:
            app_data[app_name] = []
        list_rule = ''
        for n in range(1, 6):
            if str(row[n]) == 'nan':
                list_rule = list_rule + '\t'
            else:
                list_rule = list_rule + str(row[n]) + '\t'
        # print(list_rule)
        app_data[app_name].append(list_rule)

    for app_name, paths in app_data.items():
        fxr_file_path = "appfxr/" + f"{app_name}.fxr"

        with open(fxr_file_path, 'w', encoding='utf-16') as fxr_file:
            fxr_file.write(app_name + '\n')
            for path in paths:
                fxr_file.write(f"{path}\n")

        print(f"{fxr_file_path} created.")

        # print('"' + app_name + '",')

if __name__ == "__main__":
    excel_file_path = "mask_rule_0913.xlsx"  # Replace with your Excel file path

    # Read the Excel file into a DataFrame with UTF-16 encoding
    excel_data = pd.read_excel(excel_file_path)

    # Call the function to create .fxr files
    sep2app_fxr(excel_data)
