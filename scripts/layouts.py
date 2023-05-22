import PySimpleGUI as sg

input_crs = [
    [sg.Text("Welcome to the CRS converter!"), ],
    [sg.Text("Select the input CRS:"), ],
    [sg.Text("[1] Pseudo-Mercator"), ],
    [sg.Text("[2] World Geodetic System"), ],
    [sg.Text("[3] Poland CS2000"), ],
    [
        sg.Text("Enter your choice:"),
        sg.InputText(),
    ],
    [
        sg.Button("Confirm"),
        sg.Button("Cancel"),
    ],
]

output_crs = [
    [sg.Text("Welcome to the CRS converter!"), ],
    [sg.Text("Select the output CRS:"), ],
    [sg.Text("[1] Pseudo-Mercator"), ],
    [sg.Text("[2] World Geodetic System"), ],
    [sg.Text("[3] Poland CS2000"), ],
    [
        sg.Text("Enter your choice:"),
        sg.InputText(),
    ],
    [
        sg.Button("Confirm"),
        sg.Button("Cancel"),
    ],
]

result = [
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

error = [
    [sg.Text("Script received invalid input ❌"), ],
    [sg.Button("Cancel"), ],
]
