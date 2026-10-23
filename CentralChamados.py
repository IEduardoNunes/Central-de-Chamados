# Sistema simples de chamados de TI

# Lista de chamados abertos
chamados = []

# Lista de chamados concluídos
concluidos = []


def horario_comercial(hora): # Verificando se está em horário comercial (08:00h às 18:00h)
    return 8 <= hora < 18


while True:
    print("\n===== SISTEMA DE CHAMADOS =====")

    hora_atual = int(input("Informe a hora atual (0 a 23): ")) # Solicitando para o usuário informar o horário.

    # Verifica horário comercial
    if not horario_comercial(hora_atual):
        print("Fora do horário comercial. Sistema encerrado.")
        break # Caso não esteja no horário comercial, o sistema é encerrado.

    tipo_acesso = input("Você é um usuário ou analista? ").lower() # Perguntando se quem está acessando é um usuário (solicitante) 
    # ou um analista.


    # ÁREA DO USUÁRIO
    if tipo_acesso == "usuário" or tipo_acesso == "usuario": # Caso informe que é um usuário, o seguinte while será executado.
        nome = input("Informe seu nome: ")
        data = input("Informe a data da solicitação: ")
        while True:
            
            solicitacao = input("Descreva sua solicitação: ")

            chamado = {
                "nome": nome,
                "data": data,
                "solicitacao": solicitacao
            } # Após receber as informações sobre o usuário e qual o chamado dele, seus dados são armazenados dentro desse dicionário.

            chamados.append(chamado) # Irá adicionar o item armazenado no dicionário "chamado" dentro da lista "chamados"

            print("\nSolicitação salva com sucesso!")

            nova = input("Deseja fazer uma nova solicitação? (sim/não): ").lower()

            if nova != "sim":
                break # Sistema pergunta se o usuário quer realizar uma nova solicitação. Caso sim, ele realiza as mesmas 
            # perguntas anteriores para adicionar o chamado na lista, caso não, o processo reinicia com o sistema perguntando se 
            # quem está acessando é um usuário ou analista.


    # ÁREA DO ANALISTA
    elif tipo_acesso == "analista": # Caso informe que é um analista, o seguinte while será executado:

        nome_analista = input("Informe o nome do analista: ")

        while True:

            # Verifica se existem chamados
            if len(chamados) == 0: #Caso não tenham chamados pendentes, o processo reinicia com o sistema perguntando se quem 
                # está acessando é um usuário ou analista.
                print("\nNão há chamados pendentes.")
                break

            print("\n===== CHAMADOS PENDENTES =====")

            for i, chamado in enumerate(chamados): # Imprimindo cada chamado utilizando o for com o enumerate (Utilizado para 
                # extrair o índice (posição) e o valor correspondente).
                print(f"""
Id: {i} 
Nome: {chamado['nome']}
Data: {chamado['data']}
Solicitação: {chamado['solicitacao']}
""")# Cada chamado receberá um "id", no qual será utilizado para realizar o acesso e conclusão do mesmo.

            posicao = int(input("Informe o id do chamado que deseja resolver: ")) 

            # Verifica posição válida
            if posicao < 0 or posicao >= len(chamados):
                print("Id inválido.")
                continue # Caso a id seja diferente das disponíveis, o sistema informa que a id está inválida e solicita que 
            # digite novamente.

            conclusao = input("Informe a conclusão do chamado: ")

            chamado_resolvido = chamados.pop(posicao) # Adiciona uma variável "chamado_resolvido" para adicionar o chamado pela 
            # id que foi resolvida.

            registro_conclusao = {
                "analista": nome_analista,
                "solicitacao": chamado_resolvido["solicitacao"],
                "conclusao": conclusao
            } # Dicionário de concluído recebendo os devídos dados (analista, solicitação e conclusão)

            concluidos.append(registro_conclusao) # Dicionário de concluído adicionado dentro da lista de concluídos

            print("\nChamado resolvido com sucesso!")

            novo = input("Deseja resolver outro chamado? (sim/não): ").lower() 

            if novo != "sim":
                break # Sistema pergunta se o analista quer realizar uma nova conclusão. Caso sim, ele realiza as mesmas 
            # perguntas anteriores para concluir o chamado, caso não, o processo reinicia com o sistema perguntando se quem está 
            # acessando é um usuário ou analista.

    else:
        print("Tipo de acesso inválido.") # Caso informe um algo diferente de "usuário" ou "analista", o sistema reinicia, 
        # perguntando novamente qual é o horário atual.


    # MOSTRAR RESUMO
    print("\n===== CHAMADOS EM ABERTO =====")
    for chamado in chamados:
        print(chamado) # Imprimi um por um os chamados que estão pendentes.

    print("\n===== CHAMADOS CONCLUÍDOS =====")
    for concluido in concluidos:
        print(concluido) # Imprimi um por um os chamados que foram concluídos.