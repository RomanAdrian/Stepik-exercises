

l = [
        {'nume': 'Alex', 'limbaje': ['c++', 'c', 'python', 'java script', 'html']}, 
        {'nume': 'Andrei', 'limbaje': ['html', 'css']}
    ]

val = input()

new_dict = {i['nume']:i['limbaje'] for i in l}

def get_names(val):
    matching_names = []
    for k,v in new_dict.items():
        for x in v:
            if val == x:
                matching_names.append(k)
    if len(matching_names) > 0:
        return matching_names
    else:
        return 'no matching name'
print(get_names(val))