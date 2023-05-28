import PySimpleGUI as sg
from styles import font, text_color, dark_color

input_crs = [
    [sg.Text("Welcome to the CRS converter!", 
        font=font, 
        text_color=text_color, 
        background_color=dark_color
    ), ],
    [sg.Text("Select the input CRS:", 
        font=font, 
        text_color=text_color,
        background_color=dark_color
    ), ],
    [sg.Text("[1] Pseudo-Mercator", 
        font=font, 
        text_color=text_color,
        background_color=dark_color
    ), ],
    [sg.Text("[2] World Geodetic System", 
        font=font, 
        text_color=text_color,
        background_color=dark_color
    ), ],
    [sg.Text("[3] Poland CS2000", 
        font=font, 
        text_color=text_color,
        background_color=dark_color
    ), ],
    [
        sg.Text("Enter your choice:", 
            font=font, 
            text_color=text_color,
            background_color=dark_color
        ),
        sg.InputText(
            font=font, 
            text_color=dark_color,
            background_color=text_color
        ),
    ],
    [
        sg.Button("Confirm", 
            font=font
        ),
        sg.Button("Cancel", 
            font=font
        ),
    ],
]

output_crs = [
    [sg.Text("Welcome to the CRS converter!",
        font=font, 
        text_color=text_color,
        background_color=dark_color
    ), ],
    [sg.Text("Select the output CRS:", 
        font=font, 
        text_color=text_color,
        background_color=dark_color
    ), ],
    [sg.Text("[1] Pseudo-Mercator", 
        font=font, 
        text_color=text_color,
        background_color=dark_color
    ), ],
    [sg.Text("[2] World Geodetic System", 
        font=font, 
        text_color=text_color,
        background_color=dark_color
    ), ],
    [sg.Text("[3] Poland CS2000", 
        font=font, 
        text_color=text_color,
        background_color=dark_color
    ), ],
    [
        sg.Text("Enter your choice:", 
            font=font, 
            text_color=text_color,
            background_color=dark_color
        ),
        sg.InputText(
            font=font, 
            text_color=dark_color,
            background_color=text_color
        ),
    ],
    [
        sg.Button("Confirm", 
            font=font
        ),
        sg.Button("Cancel", 
            font=font
        ),
    ],
]

coords = [
    [
        sg.Text("Enter the latitude: ", 
            font=font, 
            text_color=text_color,
            background_color=dark_color
        ),
        sg.InputText(
            font=font, 
            text_color=dark_color ,
            background_color=text_color
        ),
    ],
    [
        sg.Text("Enter the longitude: ", 
            font=font, 
            text_color=text_color,
            background_color=dark_color
        ),
        sg.InputText(
            font=font, 
            text_color=dark_color,
            background_color=text_color
        ),
    ],
    [
        sg.Button("Confirm", 
            font=font
        ),
        sg.Button("Cancel", 
            font=font
        ),
    ],
]

error = [
    [
        sg.Text("Script received invalid input",
            font=font, 
            text_color=text_color,
            background_color=dark_color
        ), 
    ],
    [
        sg.Button("Cancel", 
            font=font
        ), 
    ],
]
