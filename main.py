# -*- encoding: utf-8 -*-
from interface import TelaMenu
import PySimpleGUI as sg

app = TelaMenu()
app.criar_arquivos()
app.janela1, app.janela2, app.janela3, app.janela4, app.janela5, app.janela6, app.janela7 = \
    app.index(), None, None, None, None, None, None

while True:
    # monta as janelas
    window, event, values = sg.read_all_windows()
    if window == app.janela1 and event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif window == app.janela2 and event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif window == app.janela3 and event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif window == app.janela4 and event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif window == app.janela5 and event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif window == app.janela6 and event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif window == app.janela7 and event == sg.WIN_CLOSED or event == 'Sair':
        break

    # Quando escolher função
    if window == app.janela1 and event == 'Cadastrar Cliente':
        app.janela2 = app.cadastro_cli()
        app.janela1.hide()
    if window == app.janela2 and event == 'cad_cli':
        nome = values['nome']
        idade = values['idade']
        cpf = values['cpf']
        app.cadastro('clientes.txt', nome=nome, idade=idade, cpf=cpf)
        app.janela2['output_cli'].update(app.ler_arquivo('clientes.txt'))


    if window == app.janela1 and event == 'Cadastrar Veículo':
        app.janela3 = app.cadastro_vei()
        app.janela1.hide()
    if window == app.janela3 and event == 'cad_vei':
        marca = values['marca']
        modelo = values['modelo']
        ano = values['ano']
        placa = values['placa']
        app.cadastro('veiculos.txt', marca=marca, modelo=modelo, ano=ano, placa=placa)
        app.janela3['output_vei'].update(app.ler_arquivo('veiculos.txt'))


    if window == app.janela1 and event == 'Listar Clientes':
        app.janela4 = app.lista_cli()
        app.janela1.hide()
        app.janela4['output_cli'].update(app.ler_arquivo('clientes.txt'))

    if window == app.janela1 and event == 'Listar Veículos':
        app.janela5 = app.lista_vei()
        app.janela1.hide()
        app.janela5['output_vei'].update(app.ler_arquivo('veiculos.txt'))

    if window == app.janela1 and event == 'Registrar Venda':
        app.janela6 = app.registro_venda()
        app.janela1.hide()
        app.janela6['output_venda'].update(app.ler_arquivo('clientes.txt'))
        app.janela6['output_venda'].update(app.ler_arquivo('veiculos.txt'))

    if window == app.janela1 and event == 'Listar Vendas':
        app.janela7 = app.listagem_vendas()
        app.janela1.hide()
        app.janela7['output_vendas'].update(app.ler_arquivo('vendas.txt'))


    # apaga item
    if window == app.janela4 and event == 'del_cli':
        id = str(values['id_cli'])
        app.apagar_cadastro(id, 'clientes.txt')
        app.ler_arquivo('clientes.txt')
    if window == app.janela5 and event == 'del_vei':
        id = str(values['id_vei'])
        app.apagar_cadastro(id, 'veiculos.txt')
        app.ler_arquivo('veiculos.txt')
    if window == app.janela6 and event == 'fim_venda':
        id_comprador = str(values['id_comprador'])
        id_veiculo = str(values['id_veiculo'])
        app.fecha_venda(id_comprador, id_veiculo, 'vendas.txt')

    # Pra voltar pro Menu
    if event == 'voltar1':
        app.janela1.un_hide()
        app.janela2.hide()
    elif event == 'voltar2':
        app.janela3.hide()
        app.janela1.un_hide()
    elif event == 'voltar3':
        app.janela4.hide()
        app.janela1.un_hide()
    elif event == 'voltar4':
        app.janela5.hide()
        app.janela1.un_hide()
    elif event == 'voltar5':
        app.janela6.hide()
        app.janela1.un_hide()
    elif event == 'Menu':
        app.janela7.hide()
        app.janela1.un_hide()

