class body:
    def __init__(self, deg=None, notes=0, beats=0):
        self.notes = f'{notes}{deg}'
        self.beats = beats

    def notes(self):
        return self.notes

    def beats(self):
        return self.beats

    def __str__(self):
        return self


import PySimpleGUI as sg

# newsong=sg.PopupGetText('newsong')
note = 'note', ['A', 'B', 'C', 'D', 'E', 'F', 'G']
sharp_note = ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab']
beat = 'beat', ['Sixteenth', 'Eighth', 'Quarter', 'Half', 'Whole']
beatdotted = ['Sixteenth', 'Eighth', 'Quarter', 'Half', '']
sg.theme('DarkBlue16')
song_list = []
notel = []
old_event = None
count = 0


def ps(self):
    print(self)
    self = str(self).split('+')
    a = self[0][0]
    if self.__len__() >= 2:
        b = self[1][0]
        return f'{a}+{b}'
    else:
        return f'{a}'


def ret(overide=False):
    if overide == True:
        return str(event).split('_')
    else:
        return str(event).split('_')[1]


def menu(type):
    return sg.Col(([sg.Button(f'{type[1][i]}', key=f'{type[0]}_{type[1][i]}_{i}')] for i in range(len(type[1]))))


minor = [[sg.B('♭', key='har_flat'), sg.B('#', key='har_sharp'), sg.B('dotted')],
         [sg.Slider(enable_events=True, range=(1, 7), orientation='vertical', key='degree')]]
main_task = sg.Frame('setting', [[menu(note), sg.Col(minor), menu(beat)]], key='lol')
layout = [[main_task, sg.T('hi', key='hi', size=(12, 1), font=('Arial,20')), sg.B('Submit')]]
window = sg.Window('hi', layout, size=(600, 300))
a, b, d, disp = [[], []], [], [], []
a_ = 0, 0, 0
while True:
    event, value = window.read()
    sadness = int(value['degree'])
    print(event)
    if 'note' in str(event).split('_'):
        a = ret()
        if a[0] == 'A':
            a = 'LA'
        d = ret()
        disp = f'{d}'
        a_ = ret(True)
        print(a_)
    if 'beat' in str(event).split('_'):
        b = ret()
        b_ = ret(True)
    if event == 'dotted':
        if b_[1] == 'Sixteenth':
            dot = b[1]
        else:
            b = f'{b_[1]}+{beatdotted[int(b_[2]) - 1]}'
    if event == 'har_flat':
        a = f'{d}b'
        disp = f'{d}b'
    if event == 'har_sharp':
        disp = f'{d}#'
        a = sharp_note[int(a_[2])]
    if event == 'Submit':
        hi = body(notes=a, deg=sadness, beats=b)
        file = open('../song/cool.txt', 'a')
        file.write(f'tone(pin,{hi.notes},{ps(hi.beats)});' + '\n')

        file.close()
    print(b)
    window['hi'].update(f'{disp}{sadness} {b}')
