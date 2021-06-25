import PySimpleGUI as sg
import pathlib
sg.theme('DarkGrey8')

width = 90
height = 25
STARTUP = True
filename = None

file_new =  'New file             (Ctrl + N)'
file_open = 'Open file           (Ctrl + O)'
file_save = 'Save file            (Ctrl + S)'
file_save_as = 'Save as'

menu_layout = [['File', [file_new, file_open, file_save, file_save_as, '---', 'Exit']],
			   ['Tools',['Word Count']],
			   ['Help',['About']]]

layout = [[sg.Menu(menu_layout)],
		  [sg.Text('untitled', font=('Consolas', 10), size=(width, 1), key='_INFO_')],
		  [sg.Multiline(font=('Consolas', 12), size=(width, height), key='_BODY_')]]

window = sg.Window('PacPad', layout=layout, margins=(0,0), resizable=True, return_keyboard_events=True)

def new_file():
	window['_BODY_'].update(value='')
	window['_INFO_'].update(value='untitled')
	file = None
	return file_new

def open_file():
	filename = sg.popup_get_file('Open', no_window=True)
	if filename:
		file = pathlib.Path(filename)
		window['_BODY_'].update(value=file.read_text())
		window['_INFO_'].update(value=file.absolute())
		return file

def save_file(file):
	if file:
		file.write_text(values.get('_BODY_'))
	else:
		save_file_as()

def save_file_as():
	filename = sg.popup_get_file('Open', no_window=True)
	if filename:
		file = pathlib.Path(filename)
		file.write_text(values.get('_BODY_'))
		window['_INFO_'].update(value=file.absolute())
		return file

def word_count():
	num_of_lines = 0
	num_of_words = 0
	num_of_char = 0
	for line in values['_BODY_'].split("\n"):
		print(line)
		line = line.strip("\n")
		words = line.split()
		num_of_lines += 1
		num_of_words += len(words)
		num_of_char += len(line)
	sg.popup_no_wait('Word Count: {:,d}'.format(num_of_words),
					 'Character Count: {:,d}'.format(num_of_char),
					 'Line Count: {:,d}'.format(num_of_lines - 1))

def about():
	sg.popup_no_wait('Made by Michał Paczkowski 2021','https://github.com/PaC1337')

while True:
	event, values = window.read(timeout=1)
	if STARTUP:
		window.maximize()
		window['_BODY_'].expand(expand_x=True, expand_y=True)
		STARTUP = False
	if event in('Exit', None):
		break
	if event in (file_new, 'n:78'):
		file = new_file()
	if event in (file_open, 'o:79'):
		file = open_file()
	if event in (file_save, 's:83'):
		save_file(file)
	if event in (file_save_as,):
		file = save_file_as()   
	if event in ('Word Count',):
		word_count() 
	if event in ('About',):
		about()


