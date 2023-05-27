import PySimpleGUI as sg
import pandas as pd

EXCEL_FILE = 'dane01.xlsx'
df = pd.read_excel(EXCEL_FILE)


sg.theme("DarkTeal9")

layout = [
    [sg.Text('Wypełnij WSZYSTKIE pola!')],
    [sg.Text('Nr Atestu:', size=(15, 2)), sg.InputText(key='Nr Atestu')],
    [sg.Text('Ilot:', size=(15, 1)), sg.InputText(key='Ilot')],
    [sg.Text('Part Number:', size=(15, 1)), sg.InputText(key='Part Number')],
    [sg.Text('Batch:', size=(15, 1)), sg.InputText(key='Batch')],
    [sg.Text('Ilość:', size=(15, 1)), sg.InputText(key='Ilość')],
    [sg.Text('Dostawca:', size=(15, 1)), sg.InputText(key='Dostawca')],
    [sg.Text('Data przyjęcia:', size=(15, 1)), sg.InputText(key='Data przyjęcia')],
    [sg.Text('Data zwolnienia:', size=(15, 1)), sg.InputText(key='Data zwolnienia')],    
    [sg.Text('Inspektor:', size=(15, 1)), sg.InputText(key='Inspektor')],
    [sg.Text('Alert?', size=(15, 1)), sg.Combo(['Tak', 'Nie'], key='Alert')],    
    [sg.Text('Czas sprawdzania alertu:', size=(25, 1)), sg.InputText(key='Czas sprawdzania alertu', size=(10, 1))],
    [sg.Text('VITAL?', size=(15, 1)), sg.Combo(['Tak', 'Nie'], key='VITAL')],
    [sg.Text('ITAR?', size=(15, 1)), sg.Combo(['Tak', 'Nie'], key='ITAR')],
    [sg.Text('Komentarz:', size=(15, 1)), sg.InputText(key='Komentarz')],
    [sg.Text('Rodzaj dostawy:', size=(15, 1)), sg.Combo(['Mat. surowy', 'Kooperacja', 'Standardowa', 'DQR', 'Rysunkowa'], key='Rodzaj dostawy')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]
window = sg.Window("Rejestr Atestów 2023", layout)

def clear_input():

    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Clear":
        clear_input()
    if event == "Submit":
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index = False)
        sg.popup('Dane wprowadzone!')
        clear_input()
window.close()
