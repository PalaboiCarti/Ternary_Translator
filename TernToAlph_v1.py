import pandas as pd

data = {
    'letter': [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    't_num': ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110', '111', '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222']
}
translation_matrix = pd.DataFrame(data)

def get_message():
    while True:
        try:
            message = input("Enter Ternary: ")
            return message
        except ValueError:
            print("Use a string, dumbass.")

message = get_message()
message_array = []

for i in range(0, len(message), 3):
    tern = message[i:i+3]
    bool_res = translation_matrix['t_num'] == tern
    translation_item = translation_matrix[bool_res]
    if not translation_item.empty:
        alphabetical = translation_item['letter'].values[0]
        message_array.append(alphabetical)
    else:
        message_array.append(tern)

translation = ''.join(message_array)

print(translation)
