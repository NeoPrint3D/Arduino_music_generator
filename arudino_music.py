def main():
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
    import os

    newsong = sg.PopupGetText('newsong')
    if newsong.__contains__(' '):
        newsong = newsong.replace(' ', '_')
    os.mkdir(f'song/{newsong}')

    path = f'song/{newsong}/{newsong}.ino'
    file = open(path, 'w')
    note = 'note', ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    sharp_note = ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab']
    beat = 'beat', ['Sixteenth', 'Eighth', 'Quarter', 'Half', 'Whole']
    beatdotted = ['Sixteenth', 'Eighth', 'Quarter', 'Half', '']
    sg.theme('DarkBlue16')
    song_list = []

    def setup():
        f = open('dependicies/long.txt', 'r')
        content = str(f.read()).split('\n')
        for i in range(len(content)):
            if i >= len(content) - 1:
                break
            file.write(f'{content[i]}\n')
        file.write('int pin=' + str(sg.PopupGetText('pin')) + ';\n')
        f.close()
        file.close()

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

    minor = [[sg.B('♭', key='har_flat'), sg.B('#', key='har_sharp'), sg.B('dotted')], [sg.B('rest')],
             [sg.Slider(enable_events=True, range=(1, 7), orientation='vertical', key='degree', default_value=3)]]
    main_task = sg.Frame('setting', [[menu(note), sg.Col(minor), menu(beat)]], key='lol')
    layout = [[main_task, sg.T('hi', key='hi', size=(12, 1), font=('Arial,20')), sg.B('Submit')]]
    window = sg.Window(newsong, layout, size=(600, 300))

    a, b, d = [[], []], [], [],
    dispnote = ''
    dispbeat = ''
    a_ = 0, 0, 0
    b_ = 0, 0, 0
    dot_val = False
    setup()
    file = open(path, 'a')
    file.write("""void setup() {     
    pinMode(pin, OUTPUT); 
    """)
    file.close()
    bt = False
    b_tamper = 0
    rest_val = False
    nt = False


    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        sadness = int(value['degree'])
        if event == 'degree':
            disp = f'{d}{sadness}'
        if 'note' in str(event).split('_'):
            a = ret()
            if a[0] == 'A':
                a = 'LA'
            d = ret()
            dispnote = f'{d}{sadness}'
            a_ = ret(True)
            print(a_)
            nt = True
        if 'beat' in str(event).split('_'):
            b = ret()
            b_tamper = b
            dispbeat = f'{b}'
            b_ = ret(True)
        if event == 'dotted':
            dot_val = not dot_val
            if dot_val:
                dispbeat = f'dotted {b}'
                if b_[1] == 'Sixteenth':
                    dot = b[1]
                else:
                    b = f'{b_[1]}+{beatdotted[int(b_[2]) - 1]}'
            else:
                b = b_tamper
                dispbeat = f'{b}'
            window['dotted'].update(button_color=['midnight blue', 'red'][dot_val])
        if event == 'har_flat':
            a = f'{d}b'
            dispnote = f'{d}b{sadness}'
        if event == 'har_sharp':
            dispnote = f'{d}#{sadness}'
            a = sharp_note[int(a_[2])]
        if event == 'rest':
            rest_val = not rest_val
            if rest_val:
                bt = True
                dispbeat = f'{b_tamper} rest'
            else:
                bt = False
                dispbeat = f'{b_tamper}'
            window['rest'].update(button_color=['midnight blue', 'red'][rest_val])
        if event == 'Submit':
            hi = body(notes=a, deg=sadness, beats=b)
            if nt:
                nt = False
                somenote = f'tone(pin,{hi.notes},{ps(hi.beats)});\n'
                somebeat = f'delay(1+{ps(hi.beats)});\n'
            if bt:
                bt = False
                somenote = ''
                somebeat = f'delay(1+{ps(hi.beats)});\n'
            file = open(path, 'a')
            file.write(f'{somenote}{somebeat}')
        window['hi'].update(f'{dispnote} {dispbeat}')
    window.Close()
    file.write("""}
    void loop(){
    }""")
    file.close()


if __name__ in '__main__':
    main()
