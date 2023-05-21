import PySimpleGUI as sg

def display_error_window():
    layout = [
        [ sg.Text("Script received invalid input ❌"), ],
        [ sg.Button("Cancel"), ],
    ]

    window = sg.Window("CRS converter", layout)

    while (True):
        event, values = window.read()
        
        if (event == sg.WIN_CLOSED or event == "Cancel"):
            break

    window.close()
