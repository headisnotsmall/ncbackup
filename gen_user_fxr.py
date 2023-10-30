import pandas as pd
import os
            
def read_user_app_mapping(file_path):
    user_app_mapping = {}
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        username = row['登入者']
        app = row['軟體名稱']
        if username in user_app_mapping:
            user_app_mapping[username].append(app)
        else:
            user_app_mapping[username] = [app]
    return user_app_mapping

def gen_user_fxr(user_app_mapping, masking_rules_folder, output_folder):
    if not os.path.exists(output_folder):
          os.makedirs(output_folder)
          
    all_apps = []

    for index, row in excel_data.iterrows():
        app_name = row['Application Name']
        if app_name not in all_apps:
            all_apps.append(app_name)
                  
    for username, apps in user_app_mapping.items():
        personal_rule = []
        unallowed_apps = list(all_apps)
        for app in apps:
            try:
                unallowed_apps.remove(app)
            except ValueError:
                pass
        for app in unallowed_apps:
            app_rule_file = os.path.join(masking_rules_folder, f"{app}.fxr")
            if os.path.exists(app_rule_file):
                with open(app_rule_file, 'r', encoding='utf-16') as file:
                    for line in file:
                        rule = line.strip()
                        personal_rule.append(rule)
        personal_rule_file = os.path.join(output_folder, f"{username}.fxr")
        with open(personal_rule_file, 'w', encoding='utf-16') as file:
            file.write(username + '\n')
            for rule in personal_rule:
                file.write(f"{rule}\n")
        print(f"Personal rule for {username} created in {personal_rule_file}")
        # print(username, len(unallowed_apps))

        
if __name__ == "__main__":
    user_app_mapping_file = "user_fxr_0918.xlsx"  # Replace with the user-app mapping Excel file
    masking_rules_folder = "appfxr"  # Replace with the folder containing the application masking rules
    output_folder = "userfxr"  # Replace with the folder where personal rules will be saved
    excel_file_path = "mask_rule_0913.xlsx"  # Replace with your Excel file path
    user_app_mapping = read_user_app_mapping(user_app_mapping_file)
    excel_data = pd.read_excel(excel_file_path)
    gen_user_fxr(user_app_mapping, masking_rules_folder, output_folder)
 
    # Read the Excel file into a DataFrame with UTF-16 encoding
