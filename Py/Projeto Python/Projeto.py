import PySimpleGUI as sg
from datetime import date
import random
import requests
import locale as l
import mysql.connector as mysql

def banco():
    nome = values['-nome-']
    email = values['-email-']
    telefone = values['-telefone-']

    try:
        conexao = mysql.connect(
            host="127.0.0.1", 
            user = "root", 
            password = "",
            database = "dbpython"
        )
        print("Conexão realizada com sucesso.")
        cursor = conexao.cursor()
        sql = "INSERT INTO contatos(nome, email, telefone) VALUES (%s, %s, %s)"
        vals = (nome, email, telefone)
        cursor.execute(sql, vals)
        conexao.commit()
        print("Salvo com sucesso.")
    except mysql.Error as e:
        print(e.msg)

def grafico():
    BAR_WIDTH = 50
    BAR_SPACING = 75 
    EDGE_OFFSET = 3
    GRAPH_SIZE = DATA_SIZE = (300, 400)
    sg.theme('Dashboard')
    layout = [[sg.Text('Gráfico de barras com PySimpleGUI')],
              [sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE, k='-GRAPH-')],
              [sg.Button('OK'), sg.T('Click para ver mais dados'), sg.Exit()]]
    window = sg.Window('Gráfico de barras', layout, finalize=True)
    graph = window['-GRAPH-']
    while True:
        graph.erase()
        for i in range(7):
            graph_value = random.randint(0, GRAPH_SIZE[1])
            graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                                 bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                 fill_color=sg.theme_button_color()[1])
            graph.draw_text(text=graph_value, location=(i * BAR_SPACING + EDGE_OFFSET + 25, graph_value + 10))
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()

theme_dict = {'BACKGROUND': '#18478D',
              'TEXT': '#FFFFFF',
              'INPUT': '#F2EFE8',
              'TEXT_INPUT': '#000000',
              'SCROLL': '#F2EFE8',
              'BUTTON': ('#000000', '#C2D4D8'),
              'PROGRESS': ('#FFFFFF', '#C7D5E0'),
              'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}
sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')
BORDER_COLOR = '#FFFFFF'
DARK_HEADER_COLOR = '#FFFFFF'
BPAD_TOP = ((20, 20), (20, 10))
BPAD_LEFT = ((20, 10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10, 20), (10, 20))

l.setlocale(l.LC_TIME, "pt")
data_atual = date.today()
data_em_texto = data_atual.strftime("%d de %B de %Y").title()
top_banner = [[sg.Text(' ' * 2, background_color='#FFFFFF'), sg.Image('icone.png', background_color='#ffffff'),
               sg.Text(' ' * 128, background_color='#FFFFFF'),
               sg.Text(data_em_texto, font='Any 14', background_color='#005DAD')]]
API_KEY = "7753ee82ffac2836bdb825e03be43f51"
cidade = "Brasília"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
top = [[sg.Text(' ' * 30, ),
        sg.Text(f"Temperatura em Brasília {temperatura:.2f} ºC", size=(50, 1), justification='c', pad=BPAD_TOP,
                font='Any 16')],
       [sg.T(f'{i * 25}-{i * 34}') for i in range(7)], ]

block_2 = [[sg.Text('Entrar', font='Any 15')],
           [sg.Text('')],
           [sg.Text('Nome do Usuário'), sg.Input(key='-user-')],
           [sg.Button('Login'), sg.Button('Cancelar')]]

block_3 = [[sg.Text('Estatística', font='Any 16')],
           [sg.Text('\t  Gráfico', font='Any 10')],
           [sg.Image(data=sg.DEFAULT_BASE64_ICON)],
           [sg.Button('Graf'), sg.Button('Finalizar')]]

block_4 = [[sg.Text('Cadastro', font='Any 16')],
           [sg.Text(''), ],
           [sg.OptionMenu(values=('Java', 'PHP', 'Python'), default_value='Curso', k='-OPTION MENU-'), ],
           [sg.Button(image_data=sg.DEFAULT_BASE64_ICON, key='-LOGO-'), sg.Text('\tContato')],
           [sg.Text('Nome\t'), sg.Input(key='-nome-')],
           [sg.Text('Endereço\t'), sg.Input(key='-email-')],
           [sg.Text('Telefone\t'), sg.Input(key='-telefone-')],
           [sg.Checkbox('Cadastro', default=True, k='-CB-'),
            sg.Radio('Masc', "RadioDemo", default=True, size=(10, 1), k='-R1-'),
            sg.Radio('Fem', "RadioDemo", default=True, size=(10, 1), k='-R2-'),
            sg.Combo(values=('Lógica', 'CRUD', 'Web'), default_value='Módulo', readonly=True, k='-COMBO-')],
           [sg.Text('')],
           [sg.Button('Cadastro'), sg.Button('Exit')],
           ]

layout = [[sg.Column(top_banner, size=(960, 60), pad=(0,0), background_color=DARK_HEADER_COLOR)],
          [sg.Column(top, size=(920, 90), pad=BPAD_TOP)],
          [sg.Column([[sg.Column(block_2, size=(450, 150), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_3, size=(450, 150), pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT,
                     background_color=BORDER_COLOR),
           sg.Column(block_4, size=(450, 320), pad=BPAD_RIGHT)]]
window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0, 0), background_color=BORDER_COLOR,
                   no_titlebar=True, grab_anywhere=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Finalizar':
        break
    elif event == 'Graf':
        grafico()  
    elif event == "Login":
        sg.popup('Bem vindo ', values['-user-'], image=sg.EMOJI_BASE64_HAPPY_JOY, keep_on_top=True)
    elif event == 'Cadastro':
        banco()
window.close()