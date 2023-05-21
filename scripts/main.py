from epsg_codes import epsg_codes
from handle_error import display_error_window
from pyproj import Transformer
import PySimpleGUI as sg

def main():
    has_raised_error = False

    # Input CRS

    layout = [
        [ sg.Text("Welcome to the CRS converter!"), ],
        [ sg.Text("Select the input CRS:"), ],
        [ sg.Text("[1] Pseudo-Mercator"), ],
        [ sg.Text("[2] World Geodetic System"), ],
        [ sg.Text("[3] Poland CS2000"), ],
        [ sg.Text("[4] Poland CS1992"), ],
        [
            sg.Text("Enter your choice:"),
            sg.InputText(),
        ],
        [
            sg.Button("Confirm"),
            sg.Button("Cancel"),
        ],
    ]

    window = sg.Window("CRS converter", layout)

    while (True):
        event, values = window.read()

        if (event == sg.WIN_CLOSED or event == "Cancel"):
            break

        try:
            input_code = int(values[0])
            if (input_code == 1):
                input_code = epsg_codes["pseudo_mercator"]
            elif (input_code == 2):
                input_code = epsg_codes["world_geodetic_system"]
            elif (input_code == 3):
                input_code = epsg_codes["poland_cs2000"]
            elif (input_code == 4):
                input_code = epsg_codes["poland_cs1992"]

        except ValueError:
            display_error_window()
            has_raised_error = True
            break

    window.close()

    # Output CRS

    if (not has_raised_error):
        layout = [
            [ sg.Text("Welcome to the CRS converter!"), ],
            [ sg.Text("Select the output CRS:"), ],
            [ sg.Text("[1] Pseudo-Mercator"), ],
            [ sg.Text("[2] World Geodetic System"), ],
            [ sg.Text("[3] Poland CS2000"), ],
            [ sg.Text("[4] Poland CS1992"), ],
            [
                sg.Text("Enter your choice:"),
                sg.InputText(),
            ],
            [
                sg.Button("Confirm"),
                sg.Button("Cancel"),
            ],
        ]

        window = sg.Window("CRS converter", layout)

        while (True):
            event, values = window.read()

            if (event == sg.WIN_CLOSED or event == "Cancel"):
                break

            try:
                output_code = int(values[0])
                if (output_code == 1):
                    output_code = epsg_codes["pseudo_mercator"]
                elif (output_code == 2):
                    output_code = epsg_codes["world_geodetic_system"]
                elif (output_code == 3):
                    output_code = epsg_codes["poland_cs2000"]
                elif (output_code == 4):
                    output_code = epsg_codes["poland_cs1992"]
                else:
                    display_error_window()
                    has_raised_error = True
                    break

                if (input_code == output_code):
                    display_error_window()
                    has_raised_error = True
                    break

            except ValueError:
                display_error_window()
                has_raised_error = True
                break

        window.close()

    # Result

    if(not has_raised_error):
        layout = [
            [
                sg.Text("Enter the latitude: "),
                sg.InputText(),
            ],
            [
                sg.Text("Enter the longitude: "),
                sg.InputText(),
            ],
            [
                sg.Button("Confirm"),
                sg.Button("Cancel"),
            ],
        ]

        window = sg.Window("CRS converter", layout)

        while (True):
            event, values = window.read()

            if (event == sg.WIN_CLOSED or event == "Cancel"):
                break

            try:
                latitude = float(values[0])
                longitude = float(values[1])

                transformer = Transformer.from_crs(
                input_code, output_code, always_xy=True)
                coordinates = transformer.transform(longitude, latitude)
                print(f"The transformed coordinates are: {coordinates}")

            except ValueError:
                display_error_window()
                has_raised_error = True
                break

        window.close()

if(__name__ == "__main__"):
    main()
