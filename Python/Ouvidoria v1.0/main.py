from time import sleep
elogios=[]
criticas=[]
sugestoes=[]
dele= 0
sair= False
nome= str(input('Para iniciar a ouvidoria é necessario dizer seu nome: ')).strip().title()
sleep(0.2)
print('\033[1;34m=\033[m'*5,f'Seja bem vindo a nossa ouvidoria {nome}','\033[1;34m=\033[m'*5)
sleep(0.4)
while not sair==True:
  voltar= False
  opção= input('Nossas opções são: \n \033[1;30m1\033[m. Comentário \n \033[1;30m2\033[m. Seus comentários \n \033[1;30m3\033[m. Apagar comentário(s) \n \033[1;30m4\033[m. Sair \nO que deseja fazer? ').strip()
  if opção=='1':
    while not voltar==True:
      comentario=str(input(' \033[1;30m1\033[m. Fazer um elogio \n \033[1;30m2\033[m. Fazer uma critica \n \033[1;30m3\033[m. Fazer uma sugestão \nO que deseja fazer? ')).strip()
      if comentario=='1':
          elogio= str(input('Em que você deseja nos elogiar? ')).strip()
          elogios.append(elogio)
          print('Elogio registrado com \033[1;32msucesso\033[m')
          print()
          sleep(0.4)
          while not voltar==True:
            comemais= str(input('Deseja comentar mais alguma coisa? ')).strip().upper()
            if comemais in 'SIM':
              break
            elif comemais in 'NÃONAO':
              voltar=True
            else:
              print('Não entendi. ', end='')      
      elif comentario=='2':
        critica= str(input('Em que você deseja nos criticar? ')).strip()
        criticas.append(critica)
        print('Critica registrado com \033[1;32msucesso\033[m')
        print()
        sleep(0.4)
        while not voltar==True:
          comemais= str(input('Deseja comentar mais alguma coisa? ')).strip().upper()
          if comemais in 'SIM':
            break
          elif comemais in 'NÃONAO':
            voltar=True
          else:
            print('Não entendi. ', end='')   
      elif comentario=='3':
        sugestao= str(input('Qual a sugestão que você deseja dar? ')).strip()
        sugestoes.append(sugestao)
        print('Sugestão registrado com \033[1;32msucesso\033[m')
        print()
        sleep(0.4)
        while not voltar==True:
          comemais= str(input('Deseja comentar mais alguma coisa? ')).strip().upper()
          if comemais in 'SIM':
            break
          elif comemais in 'NÃONAO':
            voltar=True    
          else:
            print('Não entendi. ', end='') 
      else:
        print('Você não escolheu uma opção valida')
        sleep(0.2)

  elif opção=='2':
    while not voltar==True:
      ver= str(input(' \033[1;30m1\033[m. Elogios \n \033[1;30m2\033[m. Criticas \n \033[1;30m3\033[m. Sugestões \n \033[1;30m4\033[m. Ver tudo \nQuais comentários você deseja ver? ')).strip()
      if ver=='1':
        print(f'Seus elogios:')
        sleep(0.4)
        for x in range(len(elogios)):
          print(f'{x+1}. {elogios[x]}')
        while not voltar==True:
          vermais= str(input('Deseja ver mais alguma coisa? ')).strip().upper()
          if vermais in 'SIM':
            break
          elif vermais in 'NÃONAOo':
            voltar=True
          else:
            sleep(0.2)
            print('Não entendi. ', end='') 
      elif ver=='2':
        print(f'Suas criticas:')
        for c in range(len(criticas)):
          print(f'{c+1}. {criticas[c]}')
        sleep(0.4)
        while not voltar==True:
          vermais= str(input('Deseja ver mais alguma coisa? ')).strip().upper()
          if vermais in 'SIM':
            break
          elif vermais in 'NÃONAO':
            voltar=True
          else:
            sleep(0.2)
            print('Não entendi. ', end='') 
      elif ver=='3':
        print(f'Suas sugestões:')
        for v in range(len(sugestoes)):
          print(f'{v+1}. {sugestoes[v]}')
        sleep(0.4)
        while not voltar==True:
          vermais= str(input('Deseja ver mais alguma coisa? ')).strip().upper()
          if vermais in 'SIM':
            break
          elif vermais in 'NÃONAO':
            voltar=True
          else:
            sleep(0.2)
            print('Não entendi. ', end='') 
      elif ver=='4':
        print(f'Seus \033[1;37melogios\033[m:\n')
        for o in range(len(elogios)):
          print(f'{o+1}. {elogios[o]}')
        print()
        print(f'Suas \033[1;37mcriticas\033[m:\n')
        for t in range(len(criticas)):
          print(f'{t+1}. {criticas[t]}')
        print()
        print(f'Suas \033[1;37mSugestões\033[m:\n')
        for p in range(len(sugestoes)):
          print(f'{p+1}. {sugestoes[p]}')
        sleep(0.4)
        while not voltar==True:
          vermais= str(input('Deseja ver mais alguma coisa? ')).strip().upper()
          if vermais in 'SIM':
            break
          elif vermais in 'NÃONAO':
            voltar=True
          else:
            sleep(0.2)
            print('Não entendi. ', end='') 
      else:  
        print('Você não escolheu uma opção valida.')
        sleep(0.2)
  elif opção=='3':
    while not voltar==True:
      apagar= str(input(' \033[1;30m1\033[m. Elogios \n \033[1;30m2\033[m. Criticas \n \033[1;30m3\033[m. Sugestões \n \033[1;30m4\033[m. Apagar tudo \nQuais comentários você deseja apagar? ')).strip()
      if apagar=='1' and elogios==[]:
        print('Você ainda não faz nenhum elogio.')
        sleep(0.2)
        break
      elif apagar=='1':
        print(f'Seus elogios:')
        for x in range(len(elogios)):
          print(f'{x+1}. {elogios[x]}')
        dele= input('Qual numero do elogio que você deseja apagar? ')
        if dele.isdigit()==False:
          print('Esse elogio não existe')
        else:
          dele=int(dele)
          if len(elogios)<dele:
            print('esse elogio não existe')
          else:
            elogios.pop(dele-1)
            print(f'Você \033[1;31mapagou\033[m o {dele}º elogio')
            sleep(0.4)
          while not voltar==True:
            apagarmais= str(input('Deseja apagar mais alguma coisa? ')).strip().upper()
            if apagarmais in 'SIM':
              break
            elif apagarmais in 'NÃONAO':
              voltar=True 
            else:
              sleep(0.2)
              print('Não entendi. ', end='')
      elif apagar=='2' and criticas==[]:
        print('Você ainda não fez nenhuma critica.')
        sleep(0.2)
        break
      elif apagar=='2':
        print(f'Suas criticas:')
        for x in range(len(criticas)):
          print(f'{x+1}. {criticas[x]}')
        dele=input('Qual numero da critica que você deseja apagar? ')
        if dele.isdigit()==False:
          print('Não existe essa critica')
        else: 
            dele=int(dele)
            if len(criticas)<dele:
              print('Não existe essa critica')
            else: 
              criticas.pop(dele-1)
              print(f'Você \033[1;31mapagou\033[m o {dele}º critica')
              sleep(0.4)
        while not voltar==True:
          apagarmais= str(input('Deseja apagar mais alguma coisa? ')).strip().upper()
          if apagarmais in 'SIM':
            break
          elif apagarmais in 'NÃONAO':
            voltar=True 
          else:
            sleep(0.2)
            print('Não entendi. ', end='')
      elif apagar=='3' and sugestoes==[]:
        print('Você ainda não deu nenhuma sugestão.')
        sleep(0.2)
        break
      elif apagar=='3':
        print(f'Suas sugestões:')
        for x in range(len(sugestoes)):
          print(f'{x+1}. {sugestoes[x]}')
        dele=input('Qual numero da sugestão que você deseja apagar? ')
        if dele.isdigit()==False:
          print('Essa sugestão não existe')
        else:
          dele=int(dele)
          if len(sugestoes)<dele:
            print('Essa sugestão não existe')
          else:  
            sugestoes.pop(dele-1)
            print(f'Você \033[1;31mapagou\033[m a {dele}º sugestão')
            sleep(0.4)
        while not voltar==True:
          apagarmais= str(input('Deseja apagar mais alguma coisa? ')).strip().upper()
          if apagarmais in 'SIM':
            break
          elif apagarmais in 'NÃONAO':
            voltar=True 
          else:
            sleep(0.2)
            print('Não entendi. ', end='')
      elif apagar=='4' and sugestoes==[] and criticas==[] and elogios==[]:
        print('Você ainda não fez nenhum tipo de comentário.')
        sleep(0.2)
        break
      elif apagar=='4':
        while not voltar==True:
          apagartudo= input('apagar:\n \033[1;30m1\033[m. Todas os elogios \n \033[1;30m2\033[m. Todos as criticas \n \033[1;30m3\033[m. Todas as sugestões \n \033[1;30m4\033[m. Apagar tudo \nO que deseja fazer? ')
          if apagartudo=='1':
            elogios.clear()
            print('Você \033[1;31mapagou\033[m todos os elogios.')
            sleep(0.2)
            voltar=True
          elif apagartudo=='2':
            criticas.clear()
            print('Você \033[1;31mapagou\033[m todas as criticas.')
            sleep(0.2)
            voltar=True
          elif apagartudo=='3':
            sugestoes.clear()  
            print('Você \033[1;31mapagou\033[m todas as sugestões.')
            sleep(0.2)
            voltar=True
          elif apagartudo=='4':
            criticas.clear()
            elogios.clear()
            sugestoes.clear() 
            print('Você \033[1;31mapagou\033[m todos os comentários.')
            sleep(0.2)
            voltar=True
          else:
            print('Você não escolheu uma opção valida.')
            sleep(0.2)
      else:
        print('Você não escolheu uma opção valida. ')
  elif opção=='4':
    while not voltar==True:
      op4sair= str(input('Tem certeza que deseja sair? ')).strip().upper()
      if op4sair in 'SIM':
        print('Foi um prazer, volte sempre')
        sair=True
        voltar=True
      elif op4sair in 'NÃONAO':
        print('Voltando para o menu...')
        voltar= True
        sleep(0.2)
      else:
        sleep(0.2)
        print('Não entendi.', end='')        
  else:
    print('Você não escolheu uma opção valida')
    sleep(0.2)
