from time import sleep #Modulo pra adicionar um delay entre as informações

import database #Arquivo da classe com as funções que utiliza o Modulo do MySql

banco_de_dados = database.Database()

class Ouvidoria:
    

    def __init__(self,nome):
        """Classe com as funções da Ouvidoria

        Args:
            nome (str): Nome do Usuario
        """
        print('\033[1;35m*\033[m' * 5, f'Seja bem vindo a nossa ouvidoria, {nome}', '\033[1;35m*\033[m' * 5)

    
    def logar(self):
        """função para se conectar o banco de dados

        Returns:
            _type_: o banco de dados conectado
        """
        return banco_de_dados.logar('localhost','root','lucas')
    

    def deslogar(self):
        """função para deslogar o banco de dados

        Returns:
            _type_: o banco de dados desconectado
        """
        return banco_de_dados.deslogar(Ouvidoria.logar(self))    


    def msg_voltando(self):
        """Função com uma mensagem de voltando como os "." como se estivesse carregando
        """
        print('Voltando', end='',flush=True)
        for x in range(1,4):
            sleep(0.2)
            print('.', end='',flush=True)
        print()
 
    

    def msg_erro(self,msg=''):
        """Função que imprime uma mensagem na cor vermelha para se usar nas exeções do codigo

        Args:
            msg (str, optional): Mensagem que quer que apareça como erro. Defaults to ''.
        """
        sleep(0.2)
        print(f'\033[;31mErro! {msg}.\033[m')


    def msg_sucesso(self,msg='Ocorrido'):
        """Função que imprime uma mensagem na cor verde para se usar quando for executado

        Args:
            msg (str, optional): Mensagem que quer que apareça. Defaults to 'Ocorrido'.
        """
        sleep(0.2)
        print(f'\033[;32m{msg} com sucesso.\033[m')


    def menu(self,opcoes):
        """Função para se criar menus, já imprime com o id da opção ao lado 

        Args:
            opcoes (str): _description_
        """
        sleep(0.5)
        print('='*60)
        id=1
        print('\033[;33mNossas opções são:\033[m')
        sleep(0.15)
        for opcao in opcoes:
            print(f' \033[1;30m{id}\033[m: {opcao}')
            id+=1
            sleep(0.15)
        print('='*60)
        sleep(0.5)
        
    
    def fazer_coment(self,input,novo_comentario):
        """Função para adicionar comentários e passar para o banco de dados

        Args:
            input (str): input que vem do arquivo main com a opção escolhida pelo usuario
            novo_comentario (str): Comentário que o usuario deseja adicionar
        """
        conexao = Ouvidoria.logar(self)
        if input == '1':
            banco_de_dados.fazer_coment(conexao,'elogio',novo_comentario)
            Ouvidoria.msg_sucesso(self,'Elogio feito')
        
        elif input == '2':
            banco_de_dados.fazer_coment(conexao,'critica',novo_comentario)
            Ouvidoria.msg_sucesso(self,'Critica feita')
        
        elif input == '3':
            banco_de_dados.fazer_coment(conexao,'sugestão',novo_comentario)
            Ouvidoria.msg_sucesso(self,'Sugestão feita')
        
        Ouvidoria.deslogar(self)
    

    def ver_coment(self,input):
        """Fução para listar comentários e passar para o bancno de dados

        Args:
            input (str): input que vem do arquivo main com a opção escolhida pelo usuario
        """
        conexao = Ouvidoria.logar(self)
        if input == '1':
            banco_de_dados.ver_coment(conexao,'elogio','Seus \033[;32mElogios:\033[m')
        
        elif input == '2':
            banco_de_dados.ver_coment(conexao,'critica','Suas \033[;31mCriticas:\033[m')
        
        elif input == '3':
            banco_de_dados.ver_coment(conexao,'sugestão','Suas \033[;34mSugestões:\033[m')
        
        elif input == '4':
            banco_de_dados.ver_coment(conexao,'elogio','Seus \033[;32mElogios:\033[m')
            banco_de_dados.ver_coment(conexao,'critica','Suas \033[;31mCriticas:\033[m')
            banco_de_dados.ver_coment(conexao,'sugestão','Suas \033[;34mSugestões:\033[m')
        
        Ouvidoria.deslogar(self)
        

    def apagar_coment(self,input,id_comentario):
        """Função para apagar um comentário comentário

        Args:
            input (str): input que vem do arquivo main com a opção escolhida pelo usuario
            comentario (int): id do comentário que o usuario deseja apagar
        """
        conexao = Ouvidoria.logar(self)
        if input == '1':
            try:
                banco_de_dados.apagar_coment(conexao,'elogio',id_comentario)
            except:
                Ouvidoria.msg_erro(self,'Esse elogio não existe')
            else:
                Ouvidoria.msg_sucesso(self,'Elogio apagado')
        
        elif input == '2':
            try:
                banco_de_dados.apagar_coment(conexao,'critica',id_comentario)
            except:
                Ouvidoria.msg_erro(self,'Essa critica não existe')
            else:
                Ouvidoria.msg_sucesso(self,'Critica apagado')
        
        elif input == '3':
            try:
                banco_de_dados.apagar_coment(conexao,'sugestão',id_comentario)
            except:
                Ouvidoria.msg_erro(self,'Essa Sugestão não existe')
            else:
                Ouvidoria.msg_sucesso(self,'Sugestão apagada')
        
        Ouvidoria.deslogar(self)
    

    def apagar_tudo(self,input):
        """Função para apagar todas as linhas da tabela

        Args:
            input (str): input que vem do arquivo main com a opção escolhida pelo usuario
        """
        conexao = Ouvidoria.logar(self)
        if input == '1':
            banco_de_dados.apagar_todos_coment(conexao,'elogio')
            Ouvidoria.msg_sucesso(self,'Todos os elogios apagados')
        
        elif input == '2':
            banco_de_dados.apagar_todos_coment(conexao,'critica')
            Ouvidoria.msg_sucesso(self,'Todas as criticas apagadas')
        
        elif input == '3':
            banco_de_dados.apagar_todos_coment(conexao,'sugestão')
            Ouvidoria.msg_sucesso(self, 'Todas as sugestões apagadas')
        
        elif input == '4':
            banco_de_dados.apagar_todos_coment(conexao,'elogio')
            banco_de_dados.apagar_todos_coment(conexao,'critica')
            banco_de_dados.apagar_todos_coment(conexao,'sugestão')
            Ouvidoria.msg_sucesso(self,'Todos os comentários apagados')
        
        Ouvidoria.deslogar(self)
    

    def atualizar_coment(self,input,idcoment,novocoment):
        """Função para atualizar uma linha da tabela

        Args:
            input (str): input que vem do arquivo main com a opção escolhida pelo usuario
            idcoment (int): id da linha do comentário que o usuario deseja atualizar
            novocoment (str): Novo comentário que será posto
        """
        conexao = Ouvidoria.logar(self)
        if input=='1':
            banco_de_dados.atualizar_coment(conexao,'elogio',idcoment,novocoment)
        
        elif input=='2':
            banco_de_dados.atualizar_coment(conexao,'critica',idcoment,novocoment)
        
        elif input=='3':
            banco_de_dados.atualizar_coment(conexao,'sugestão',idcoment,novocoment)
       
        Ouvidoria.msg_sucesso(self,'Comentário Atualizado')
        Ouvidoria.deslogar(self)