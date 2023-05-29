import PySimpleGUI as sg
from styles import font, white, black

name = "CRS Converter"
ratio_16x9 = (496, 279)

input_crs = [
    [
        sg.Text("Welcome to the CRS converter!", 
            font=font, 
            text_color=white, 
            background_color=black
        ), 
    ],
    [
        sg.Text("Select the input CRS:", 
            font=font, 
            text_color=white,
            background_color=black
        ), 
    ],
    [
        sg.Text("[1] Pseudo-Mercator", 
            font=font, 
            text_color=white,
            background_color=black
        ), 
    ],
    [   
        sg.Text("[2] World Geodetic System", 
            font=font, 
            text_color=white,
            background_color=black
        ), 
    ],
    [
        sg.Text("[3] Poland CS2000", 
            font=font, 
            text_color=white,
            background_color=black
        ), 
    ],
    [
        sg.Text("Enter your choice:", 
            font=font, 
            text_color=white,
            background_color=black
        ),
        sg.InputText(
            font=font, 
            text_color=black,
            background_color=white
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
    [
        sg.Text("Select the output CRS:", 
            font=font, 
            text_color=white,
            background_color=black
        ), 
    ],
    [
        sg.Text("[1] Pseudo-Mercator", 
            font=font, 
            text_color=white,
            background_color=black
        ), 
    ],
    [   
        sg.Text("[2] World Geodetic System", 
            font=font, 
            text_color=white,
            background_color=black
        ), 
    ],
    [
        sg.Text("[3] Poland CS2000", 
            font=font, 
            text_color=white,
            background_color=black
        ), 
    ],
    [
        sg.Text("Enter your choice:", 
            font=font, 
            text_color=white,
            background_color=black
        ),
        sg.InputText(
            font=font, 
            text_color=black,
            background_color=white
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
            text_color=white,
            background_color=black
        ),
        sg.InputText(
            font=font, 
            text_color=black ,
            background_color=white
        ),
    ],
    [
        sg.Text("Enter the longitude: ", 
            font=font, 
            text_color=white,
            background_color=black
        ),
        sg.InputText(
            font=font, 
            text_color=black,
            background_color=white
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
            text_color=white,
            background_color=black
        ), 
    ],
    [
        sg.Button("Cancel", 
            font=font
        ), 
    ],
]
