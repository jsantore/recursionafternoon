import openpyxl

def get_data()->list[dict]:
    state_data = []
    data_file = openpyxl.load_workbook("StateMedianIncome.xlsx")
    worksheet = data_file['Sheet1']
    for row in worksheet:
        state_entry = {}
        if type(row[2].value) is not int:
            continue # if we are looking at the heading go to next row
        state_entry['Name']=row[0].value
        state_entry['income2022'] = row[1].value
        state_entry['income2021'] = row[2].value
        state_data.append(state_entry)
    return state_data