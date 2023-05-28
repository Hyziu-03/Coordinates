from layouts import input_crs, output_crs, coords
from handle_error import display_error_window
from receive_code import receive_code
from pyproj import Transformer
import PySimpleGUI as sg
from styles import font, dark_color, text_color


def main():
    has_raised_error = False
    was_closed = False

    # Input CRS

    layout = input_crs
    window = sg.Window("CRS converter", layout, background_color=dark_color)

    while (True):
        event, values = window.read()

        if (event in (sg.WIN_CLOSED, "Cancel")):
            was_closed = True
            break

        try:
            input_code = receive_code(int(values[0]))
            if (input_code == 0):
                raise ValueError
        except ValueError:
            display_error_window()
            has_raised_error = True
            break

        if (not has_raised_error):
            break

    window.close()

    if (has_raised_error or was_closed):
        return

    # Output CRS

    layout = output_crs
    window = sg.Window("CRS converter", layout, background_color=dark_color)

    while (True):
        event, values = window.read()

        if (event in (sg.WIN_CLOSED, "Cancel")):
            was_closed = True
            break

        try:
            output_code = receive_code(int(values[0]))
            if (output_code in (0, input_code)):
                raise ValueError
        except ValueError:
            display_error_window()
            has_raised_error = True
            break

        if (not has_raised_error):
            break

    window.close()

    if (has_raised_error or was_closed):
        return

    # Coordinates

    layout = coords
    window = sg.Window("CRS converter", layout, background_color=dark_color)

    while (True):
        event, values = window.read()

        if (event in (sg.WIN_CLOSED, "Cancel")):
            was_closed = True
            break

        try:
            latitude = float(values[0])
            longitude = float(values[1])
        except ValueError:
            display_error_window()
            has_raised_error = True
            break

        if (not has_raised_error):
            break

    window.close()

    if (has_raised_error or was_closed):
        return

    # Transformation

    transformer = Transformer.from_crs(
        input_code, output_code, always_xy=True
    )
    coordinates = transformer.transform(longitude, latitude)

    layout = [
        [sg.Text("Transformed coordinates", 
            font=font,
            background_color=dark_color
        ), ],
        [sg.Text(f"Longitude: {coordinates[0]}", 
            font=font,
            background_color=dark_color
        ), ],
        [sg.Text(f"Latitude: {coordinates[1]}", 
            font=font,
            background_color=dark_color
        ), ],
        [sg.Button("Cancel", 
            font=font,
        ), ],
    ]
    window = sg.Window("CRS converter", layout, background_color=dark_color)

    while (True):
        event, values = window.read()

        if (event in (sg.WIN_CLOSED, "Cancel")):
            was_closed = True
            break

    window.close()


if (__name__ == "__main__"):
    main()
