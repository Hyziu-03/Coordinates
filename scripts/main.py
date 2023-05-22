from layouts import input_crs, output_crs, result
from handle_error import display_error_window
from receive_code import receive_code
from pyproj import Transformer
import PySimpleGUI as sg


def main():
    has_raised_error = False
    was_closed = False

    layout = input_crs
    window = sg.Window("CRS converter", layout)

    while (True):
        event, values = window.read()

        if (event in (sg.WIN_CLOSED, "Cancel")):
            was_closed = True
            break

        try:
            input_code = receive_code(int(values[0]))
            if (input_code == 0): raise ValueError
        except ValueError:
            display_error_window()
            has_raised_error = True
            break

        if (not has_raised_error): break

    window.close()

    if (has_raised_error or was_closed): return 
    
    layout = output_crs
    window = sg.Window("CRS converter", layout)

    while (True):
        event, values = window.read()

        if (event in (sg.WIN_CLOSED, "Cancel")):
            was_closed = True
            break

        try:
            output_code = receive_code(int(values[0]))
            if (output_code in (0, input_code)): raise ValueError
        except ValueError:
            display_error_window()
            has_raised_error = True
            break

        if (not has_raised_error): break

    window.close()

    if (has_raised_error or was_closed): return 
    
    layout = result
    window = sg.Window("CRS converter", layout)

    while (True):
        event, values = window.read()

        if (event in (sg.WIN_CLOSED, "Cancel")):
            was_closed = True
            break

        try:
            latitude = float(values[0])
            longitude = float(values[1])

            transformer = Transformer.from_crs(
                input_code, output_code, always_xy=True
            )
            coordinates = transformer.transform(longitude, latitude)
            print(f"The transformed coordinates are: {coordinates}")
        except ValueError:
            display_error_window()
            has_raised_error = True
            break

    window.close()


if (__name__ == "__main__"): main()
