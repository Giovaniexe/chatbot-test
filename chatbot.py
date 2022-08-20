from time import sleep

continua = True
inicio = print('-=' * 25)
print('Olá, sou o robo assitente da Microlins')
nome = input('Qual o seu nome? ')
print('É um prazer {}' .format(nome.title()))
while continua == True:
    print('-=' * 25)
    sleep(1)
    escolha = int(
        input('\n Com o que posso te ajudar {}? \n Digite [1] para duvidas de aula \n Digite [2] para aula de reposição '
          '\n Digite [3] agendar sexta-livre \n' .format(nome.title())))
    print('-=' * 25)
    sleep(1)
    if escolha == 1:
        duvidas = int(input(
            'a sua duvida é sobre: \n [1] introdução e windows \n [2] Excel, VBA ou PowerBI \n [3] PowerPoint e internet'))
        if duvidas == 1:
            print('-=' * 35)
            sleep(1)
            opcao1 = int(input('Sua duvida é sobre:\n[1] O que é um sistema operacional e quantos existem\n'
                  '[2] Unidade de memoria e order de precedencia de memória\n[3] História do computador\n'
                  '[4] Outros '))
            print('-=' * 35)
            sleep(1)
            if opcao1 == 1:
                sleep(1)
                print('-=' * 35)
                print('     Um sistema operacional é um programa desenvolvido para que o usuário consiga utilizar o '
                      'computador de maneira facil e pratica os principais são o WIN1'
                  'DOWS \n desenvolvido pela '
                      'empresa MICROSOFT, o sistema LINUX que é um sistema de codigo aberto \n com varias versões '
                      'independentes e também temos os sistemas operacionais Mobile como o IOS \n da empresa APPLE e o '
                      'ANDROID que vem na maioria dos smartphones atuais e pertence a GOOGLE')
            elif opcao1 == 2:
                print('-=' * 35)
                print('Quando falamos de unidade de memória temos as seguintes unidades: \n'
                  'BIT: que É a menor unidade de memoria \n BYTE: a segunda unidade de memoria \n'
                  'KILOBYTE: É a nossa terceira unidade de memoria e pode ser abreviada pela sigla (KB)\n'
                  'MEGABYTE: É a quarta unidade de memoria e pode ser abreviada pela sigla (MB) \n'
                  'GIGABYTE: É a quinta unidade de memoria e também a mais comum de vermos, ela pode ser abreviada pela '
                  'sigla (GB) \n TERABYTE: Uma das maiores unidades de memoria para usuarios comuns e pode ser '
                  'abreviada pela sigla (TB) \n'
                  'Cada uma dessas unidades se complementam e uma acaba formando a outra ficando assim: '
                  '8 BITS = 1 BYTE \n 1024 BYTES = 1KB \n 1024KB = 1MB \n 1024MB = 1GB \n 1024GB = 1TB')
            elif opcao1 == 3:
                print('-=' * 35)
                print('A história do computador: \n O primeiro computador foi criado entre 1943 e 1946 e se chamava '
                  'ELETRONIC NUMERICAL INTEGRATOR AND COMPUTER - ENIAC. \n Para seu desenvolvimento, foi investido cerca '
                  'de 6 Milhões de dolares e seu funcionamento dependia de uma serie de fatories, como 200 mil watts de '
                  'energia. \n Um fator de grande importância é a memoria, algo que não tinha na época do ENIAC. \n'
                  'Cerca de 10 anos depois, foi lançado o RAMAX 305...........1'
                  ' ')
            elif opcao1 == 4:
                print('-=' * 35)
                sleep(1)
                print('Aguarde que em breve um professor irá te responder :) ')
        elif duvidas == 2:
            print('-=' * 35)
            sleep(1)
            opção2 = int(input('Certo {}, sobre qual programa é a sua duvida?\n[1] Excel\n[2] VBA\n[3] PowerBI  '
                  .format(nome.capitalize())))
            if opção2 == 1:
                print('-=' * 35)
                print('O excel é um programa da Microsoft desenvolvido para a criação de planilhas que ajudam na realização'
                      'de calculos e também na organização de uma empresa. \n uma planilha é formada pelo que chamamos'
                      'de celulas que é a junção de uma linha com uma coluna e são nas celular que colocamos nossos\n'
                      'comandos no Excel e sempre que o usuario for dar um comando para o excel ele deve começar '
                      'utilizando o sinal de IGUAL (=) como por exemplo: \n=SOMA(intervalo)\num intervalo '
                      'significa as celulas que farão parte da operação, também é possivel inserirmos graficos no excel\n'
                      'mas é preferivel fazermos isso através do programa PowerBI')
            elif opção2 == 2:
                print('-=' * 35)
                print('VBA ou Visual Basic, é uma ferramenta da Microsoft que através dela podemos criar novas'
                      'funcionalidades\nprincipalmente para o excel, utilizando o VBA no excel podemos por exemplo criar'
                      'novas funções\ncomo inserir botões ou comandos automatizados tudo isso através da programação VBA.')
            elif opção2 == 3:
                print('-=' * 35)
                print('O PowerBI é um programa da Microsoft para a criação de Dashboards (Graficos), muito utilizado\n'
                      'nas empresas para conseguirem visualizar seus resultados de forma visual e simples, o PowerBi\n'
                      'trabalha junto com o Excel e por isso para utilizarmos ele precisamos preferencialmente ter uma\n'
                      'planilha pronta antes.')
            else:
                print('-=' * 35)
                print('Opção invalida!')
            Letíci

    elif escolha == 2:
        print('-=' * 35)
        sleep(1)
        falta = input('As reposições acontecem todas as sextas-feiras e devem ser agendadas no mês da falta,'
                      ' digite a data da falta ')
        repor = input('Agora digite a data da reposição: ')
        aluno = input('Digite o nome do aluno ')
        hora = input('Digite o horario que você desaja realizar a reposição')
        print('Perfeito! sua reposição do {} está agendada para o dia {} as {}'.format(aluno.title(), repor, hora))

    elif escolha == 3:
        print('-=' * 35)
        sleep(1)
        aluno = input('Certo, digite o nome do aluno ')
        horario = input('Digite o horario que aluno irá vir ')
        print('Perfeito reposição do aluno {} agendada para dia {}'.format(aluno, horario))
    adeus = input('Posso te ajudar com mais alguma coisa? '.lower())

    if adeus == 'sim':
        continua == True
    else:
        continua == False
        print('Ok {} espero ter te ajudado :) ' .format(nome.capitalize()))
