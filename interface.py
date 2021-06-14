# -*- encoding: utf-8 -*-
import PySimpleGUI as sg
from random import randint


class Arquivos:
    def __init__(self):
        self.clientes = 'clientes.txt'
        self.veiculos = 'veiculos.txt'
        self.vendas = 'vendas.txt'
        self.temp = 'temp.txt'

    def criar_arquivos(self):
        if not self.arquivo_existe(self.temp):
            self.criar_arquivo(self.temp)

        if not self.arquivo_existe(self.clientes):
            self.criar_arquivo(self.clientes)

        if not self.arquivo_existe(self.veiculos):
            self.criar_arquivo(self.veiculos)

        if not self.arquivo_existe(self.vendas):
            self.criar_arquivo(self.vendas)

    def arquivo_existe(self, nome_arquivo):
        try:
            a = open(nome_arquivo, 'rt')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def criar_arquivo(self, nome_arquivo):
        try:
            a = open(nome_arquivo, 'wt+')
            a.close()
        except:
            sg.popup_error('ERRO ao criar arquivo.', 'Não consegui criar o arquivo.')
        else:
            sg.popup(f'Arquivo {nome_arquivo} criado com sucesso.')

    def ler_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as a:
                self.id = randint(0, 9999)
                if nome_arquivo == self.clientes:
                    for linha in a:
                        dado = linha.split(';')
                        dado[3] = dado[3].replace('\n', '')
                        print(f'ID{dado[0]}\t{dado[1]}, {dado[2]} anos.\tCPF{dado[3]}')
                    print('~' * 43)
                elif nome_arquivo == self.veiculos:
                    for linha in a:
                        dado = linha.split(';')
                        dado[4] = dado[4].replace('\n', '')
                        print(f'ID{dado[0]}\t{dado[1]}, {dado[2]}\t{dado[3]}, {dado[4]}')
                    print('~' * 43)
            with open(nome_arquivo, 'r') as a:
                if nome_arquivo == self.vendas:
                    for linha in a:
                        dado = linha.split(';')
                        dado[9] = dado[9].replace('\n', '')
                        print(f'NF: {dado[0]}\nID{dado[1]} {dado[2]}\t {dado[3]}anos.\tCPF{dado[4]}'
                              f'\nID: {dado[5]}, {dado[6]}, {dado[7]}, Fabricado em {dado[8]}\nPlaca: {dado[9]}')
                        print('~' * 43)
        except:
            sg.popup_error('Erro ao abrir o arquivo.')

    def cadastro(self, nome_arquivo, nome='', idade=0, cpf=0, marca='', modelo='', ano=0, placa=''):
        try:
            if nome_arquivo == 'clientes.txt':
                with open('clientes.txt', 'a')as c:
                    c.write(f'{self.id};{nome};{idade};{cpf}\n')
                    sg.popup('Cadastro realizado com sucesso.')
            if nome_arquivo == 'veiculos.txt':
                with open('veiculos.txt', 'a') as v:
                    v.write(f'{self.id};{marca};{modelo};{ano};{placa}\n')
                    sg.popup('Cadastro realizado com sucesso.')
        except:
            sg.popup(Exception)

    def apagar_cadastro(self, id, nome_arquivo):
        # copia pra temp
        with open(nome_arquivo, 'r') as a:
            linhas = a.readlines()
            for linha in linhas:
                dado = linha.split(';')
                if not dado[0] == id:
                    with open('temp.txt', 'a') as temp:
                        temp.write(linha)
        # apaga arquivo original
        a = open(nome_arquivo, 'w')
        a.close()
        # copia temp pro original
        with open('temp.txt', 'r') as c:
            linhas = c.readlines()
            c.seek(0)
            for linha in linhas:
                with open(nome_arquivo, 'a')as new:
                    new.write(linha)
        # apagar temp
        a = open('temp.txt', 'w')
        a.close()

    def fecha_venda(self, id_comprador, id_veiculo, nome_arquivo):
        id = randint(10000, 15000)
        with open('clientes.txt', 'a+') as a:
            a.seek(0)
            linhas = a.readlines()
            for linha in linhas:
                dado = linha.split(';')
                if dado[0] == id_comprador:
                    linha.join(';')
                    linha = linha.replace('\n', ';')
                    with open(nome_arquivo, 'a+') as v:
                        v.write(f'{id};')
                        v.write(linha)
        with open('veiculos.txt', 'r') as a:
            a.seek(0)
            linhas = a.readlines()
            for linha in linhas:
                dado = linha.split(';')
                if dado[0] == id_veiculo:
                    linha.join(';')
                    with open(nome_arquivo, 'a+') as v:
                        v.write(linha)
        self.apagar_cadastro(id_veiculo, 'veiculos.txt')


######################################################################################

class TelaMenu(Arquivos):
    def __init__(self):
        super().__init__()
        sg.change_look_and_feel('Topanga')

    def index(self):
        # criação do layout
        self.menu = [
            [sg.Button('Listar Clientes', size=(15, 0)),
             sg.Text('Mostra uma lista dos clientes cadastrados', size=(40, 0))],
            [sg.Button('Cadastrar Cliente', size=(15, 0)),
             sg.Text('Realiza o cadastro de um novo cliente', size=(40, 0))],
            [sg.Button('Listar Veículos', size=(15, 0)),
             sg.Text('Mostra uma lista dos veículos cadastrados', size=(40, 0))],
            [sg.Button('Cadastrar Veículo', size=(15, 0)),
             sg.Text('Realiza o cadastro de um novo veículo', size=(40, 0))],
            [sg.Button('Registrar Venda', size=(15, 0)), sg.Text('Registra venda de veículo', size=(40, 0))],
            [sg.Button('Listar Vendas', size=(15, 0)), sg.Text('Lista as vendas já realizadas', size=(40, 0))],
            [sg.Button('Sair', size=(15, 0))],
        ]
        self.janela_menu = sg.Window('Programa de Vendas', layout=self.menu, finalize=True)
        return self.janela_menu

    def cadastro_cli(self):
        self.cad_cli = [
            [sg.Output(size=(60, 15), key='output_cli')],
            [sg.Text('Nome: ', size=(10, 0)), sg.Input(size=(30, 0), key='nome')],
            [sg.Text('Idade: ', size=(10, 0)), sg.Input(size=(4, 0), key='idade')],
            [sg.Text('CPF: ', size=(10, 0)), sg.Input(size=(11, 0), key='cpf')],
            [sg.Button('Cadastrar', size=(10, 0), key='cad_cli'), sg.Button('Voltar', key='voltar1', size=(10, 0))]
        ]
        self.janela_ccad = sg.Window('Cadastro de Cliente', layout=self.cad_cli, finalize=True)
        return self.janela_ccad

    def cadastro_vei(self):
        self.cad_veiculo = [
            [sg.Output(size=(60, 15), key='output_vei')],
            [sg.Text('Marca: ', size=(10, 0)), sg.Input(size=(30, 0), key='marca')],
            [sg.Text('Modelo: ', size=(10, 0)), sg.Input(size=(30, 0), key='modelo')],
            [sg.Text('Fabricação: ', size=(10, 0)), sg.Input(size=(7, 0), key='ano')],
            [sg.Text('Placa: ', size=(10, 0)), sg.Input(size=(7, 0), key='placa')],
            [sg.Button('Cadastrar', size=(10, 0), key='cad_vei'), sg.Button('Voltar', key='voltar2', size=(10, 0))]
        ]
        self.janela_cvei = sg.Window('Cadastro de Veículo', layout=self.cad_veiculo, finalize=True)
        return self.janela_cvei

    def lista_cli(self):
        self.list_cli = [
            [sg.Output(size=(60, 15), key='output_cli')],
            [sg.Text('ID do cliente:', size=(10, 0)), sg.Input(size=(4, 0), key='id_cli'),
             sg.Button('Apagar', key='del_cli'), sg.Button('Voltar', key='voltar3')]
        ]
        self.janela_listc = sg.Window('Listar cliente', layout=self.list_cli, finalize=True)
        return self.janela_listc

    def lista_vei(self):
        self.list_vei = [
            [sg.Output(size=(60, 15), key='output_vei')],
            [sg.Text('ID do veículo:', size=(10, 0)), sg.Input(size=(4, 0), key='id_vei'),
             sg.Button('Apagar', key='del_vei'), sg.Button('Voltar', key='voltar4')]
        ]
        self.janela_listv = sg.Window('Listar veículo', layout=self.list_vei, finalize=True)
        return self.janela_listv

    def registro_venda(self):
        self.reg_venda = [
            [sg.Output(size=(50, 15), key='output_venda')],
            [sg.Text('ID do comprador: ', size=(15, 0)), sg.Input(size=(4, 0), key='id_comprador'),
             sg.Text('Registro de Compra: ', size=(15, 0)), sg.Input(size=(2, 0)), sg.Button('Detalhes', key='det')],
            [sg.Text('ID do Veículo: ', size=(15, 0)), sg.Input(size=(4, 0), key='id_veiculo')],
            [sg.Button('Finalizar Venda', key='fim_venda'), sg.Button('Cancelar Venda', key='cancel'),
             sg.Text('', size=(5, 0)), sg.Button('Voltar', key='voltar5')]
        ]
        self.janela_venda = sg.Window('Registro de Venda', layout=self.reg_venda, finalize=True)
        return self.janela_venda

    def listagem_vendas(self):
        self.lista_vendas = [
            [sg.Output(size=(50, 15), key='output_vendas')],
            [sg.Button('Menu')]
        ]
        self.janela_lista = sg.Window('Listagem de Vendas', layout=self.lista_vendas, finalize=True)
        return self.janela_lista