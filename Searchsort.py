import Project6Loader

def main():
    state_data = Project6Loader.get_data()
    state_data.sort(key=get_key, reverse=True)
    for state in state_data:
        print(state)

def get_key(state_record):
    return state_record['income2021']

main()