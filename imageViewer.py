import PySimpleGUI as sg
import os.path


def imageViewer():
    """
    A simple image viewer that allows you to view images in a directory.
    """
    # columns for the file listv
    file_list_columns = [
        [
            sg.Text("Image folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse()
        ],
        [
            sg.Listbox(
                values=[],
                enable_events=True,
                size=(40, 20),
                key="-FILE LIST-"
            )
        ],
    ]

    # columns for the image viewer
    image_viewer_columns = [
            [sg.Text("Choose an image from list on left:")],
            [sg.Text(size=(40, 1), key="-TOUT-")],
            [sg.Image(key="-IMAGE-")],
    ]

    # layout for the window
    layout = [
        [
            sg.Column(file_list_columns),
            sg.VSeparator(),
            sg.Column(image_viewer_columns)
        ],
    ]

    # create the window
    window = sg.Window("Image Viewer", layout)


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".jpg", ".png"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":
            try:
                filename = os.path.join(
                    values["-FOLDER-"],
                    values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)
            except:
                pass

    window.close()
