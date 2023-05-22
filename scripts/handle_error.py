import PySimpleGUI as sg
from layouts import error

def display_error_window():
    try:
        layout = error
        window = sg.Window("CRS converter", layout)

        while (True):
            event, values = window.read()
            if (event in (sg.WIN_CLOSED, "Cancel")): break

        window.close()
    except:
        return 
