import PySimpleGUIWeb as sg

def print_list(input_list):
    output = ''
    for item in input_list:
        output += item
    return output


#operations
def addition(num_1, num_2):
    return num_1 + num_2
def subtraction(num_1, num_2):
    return num_1 - num_2
def multiplication(num_1, num_2):
    return num_1 * num_2
def division(num_1, num_2):
    return num_1 / num_2

operations = {'+' : addition,
              '-' : subtraction, 
              '*' : multiplication,
              '/' : division}

numbers = ['0','1','2','3','4','5','6','7','8','9']

def unwrap_list(input_list):
    numbers = [item for idx, item in enumerate(input_list) if idx % 2 == 0]
    actions = [item for idx, item in enumerate(input_list) if idx % 2 != 0]
    return numbers, actions
    
def calculate_list(numbers, actions):

    if len(numbers) > 1:
        operation = operations[actions[0]]
        result = str(operation(float(numbers[0]), float(numbers[1])))

        numbers = [result] + numbers[2:]
        actions = actions[1:]

        return calculate_list(numbers, actions)
    else : 
        return numbers

def calculator():

    layout = [[sg.Text('Function output:'), sg.Text(size=(12,1), key='-OUTPUT-')],
              [sg.Text('Operation:'), sg.Text(size=(12,1), key='-operation_output-')],
              [sg.Button('1'), sg.Button('2'), sg.Button('3')],
              [sg.Button('4'), sg.Button('5'), sg.Button('6')],
              [sg.Button('7'), sg.Button('8'), sg.Button('9')],
              [sg.Button('0')],
              [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/')],
              [sg.Button('=')],
              [sg.Button('Clear')],
              [sg.Button('Exit')]]

    window = sg.Window('Window Title', layout)

    input_list = []
    idx = 0    

    state = {'output_result' : None, 'action' : None}

    while True:  # Event Loop
        #logging inputs
        event, values = window.read()
        print(event, values)
        #break if window is closed or if exit button is pressed


        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        
        #this is near unreadable, but it does work
        if event in operations.keys():
            if idx == 0:
                window['-OUTPUT-'].update("please select a number")

            elif idx % 2 == 0:
                input_list[idx-1] = event
                window['-operation_output-'].update(print_list(input_list))

            else : 
                input_list.append(event)
                idx = len(input_list)
                window['-operation_output-'].update(print_list(input_list))
        
        if event in numbers:
            if idx % 2 == 0:
                input_list.append(event)
                window['-operation_output-'].update(print_list(input_list))
                idx = len(input_list)
            else : 
                input_list[idx-1] = input_list[idx-1] + event
                window['-operation_output-'].update(print_list(input_list))
        
        #need to decide on logic to calculate answer based on input string
        if event == '=':
            input_numbers, input_operations = unwrap_list(input_list)
            result = calculate_list(input_numbers, input_operations)

            #result = '9999'
            input_list = result
            idx = len(input_list)
            window['-OUTPUT-'].update(print_list(input_list))
            window['-operation_output-'].update(print_list(input_list))
                
            
        if event == 'Clear':
            input_list = []
            idx = len(input_list)
            window['-OUTPUT-'].update('')
            window['-operation_output-'].update(print_list(input_list))

    window.close()


if __name__ == "__main__":
    calculator()
