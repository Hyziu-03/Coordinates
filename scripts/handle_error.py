import PySimpleGUI as sg
from layouts import error, name, ratio_16x9
from styles import black, icon_path


def display_error_window():
    try:
        layout = error
        window = sg.Window(
            name, 
            layout, 
            background_color=black, 
            size=ratio_16x9, 
            icon=icon_path
        )

        while (True):
            event, values = window.read()
            if (event in (sg.WIN_CLOSED, "Cancel")):
                break

        window.close()
    except:
        return
