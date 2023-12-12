import Project6Loader

def main():
    state_data = Project6Loader.get_data()
    state_data.sort(key=get_key)
    state = binary_search(state_data, 76620)
    print(state)
    # for state in state_data:
    #     print(state)


def binary_search(states_data, to_find):
    if states_data == []:
        return None
    middle = len(states_data)//2
    middle_state = states_data[middle]
    if middle_state['income2021']  == to_find:
        return middle_state
    if middle_state['income2021'] > to_find:
        return binary_search(states_data[:middle], to_find)
    else:
        return binary_search(states_data[middle+1:], to_find)



def get_key(state_record):
    return state_record['income2021']

main()