def main():
    import PySimpleGUI as sg
    # newsong=sg.PopupGetText('newsong')
    f = open(f'../song/cool.txt', 'w')
    note = 'note', ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    beat = 'beat', ['Eighth', 'Quarter', 'Half', 'Whole']
    degree = 'degree', ['1', '2', '3', '4', '5']
    sg.theme('DarkBlue16')
    song_list = []

    def menu(type):
        return sg.ButtonMenu(type[0], [type[0], [f'{type[1][x]}' for x in range(len(type[1]))]], size=(4, 0))

    layout = [[menu(note), sg.B('♯', size=(2, 0), key='Sharp'), menu(degree), menu(beat)],
              [sg.T(size=(4, 0)), sg.B('♭', size=(2, 0), key='Flat')],
              [sg.T('', key='name', size=(20, 1), font=('Arial', 12)), sg.Button('Submit')]]
    window = sg.Window('hi', layout, size=(400, 200))

    class body:
        def __init__(self, notes=0, harm=None, degrees=0, beats=0):
            self.notes = notes + harm + degrees
            self.beats = beats

        def notes(self):
            return self.notes

        def beats(self):
            return self.beats

        def __str__(self):
            return self

    while True:
        event, value = window.read()
        if event == 'Flat':
            value_fin = value[0] + 'b'
        if event == 'Submit':
            print(value[0], value[1], value[2])
            hi = body(notes=value[0], degrees=value[1], beats=value[2])
            f.write('hi')
        window['name'].update(f'{value[0]} {value[1]}  {value[2]} Note')


if __name__ == "__main__":
    main()
