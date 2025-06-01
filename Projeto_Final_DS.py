def adicionar_tarefa(lista_de_tarefas,tarefa):
  """Adicionar nova tarefa a uma lista pré-existente"""
  lista_de_tarefas.append(tarefa)
  print ("\t✅ - Tarefa adicionada com sucesso!")
  print(("\t")+"-" * 50)
  return (lista_de_tarefas)

def listar_tarefas(lista_de_tarefas):
    """Ëxibe lista de tarefas numeradas"""
    print("\n")
    print(("\t")+"-" * 50)
    n = 1
    print (f"\t Lista de Tarefas")
    print(("\t")+"-" * 50)
    for tarefa in lista_de_tarefas:
       print(f"\t{n} - {tarefa}")
       n+=1
    print(("\t")+"-" * 50)
    print ("\n")
    print(("\t")+"-" * 50)


def deletar_tarefa(lista_de_tarefas, tarefa):
   """Deleta tarefa de uma lista pré-existe a partir de um número fornecido pelo usuário"""
   lista_de_tarefas.pop((tarefa -1))
   print ("\t✅ - Tarefa deletada com sucesso!")
   print(("\t")+"-" * 50)

   return lista_de_tarefas

def exibir_menu():
    """Exibe menu com opções para usuárie escolher"""
    print("\tEscolha uma opção:\n"\
          "\t1 - Inserir nova tarefa\n"\
            "\t2 - Listar tarefas\n" \
            "\t3 - Deletar tarefas\n"\
            "\t4 - Sair"
    )
    print(("\t")+"-" * 50)
lista_de_tarefas = []
continuar = True
print(("\t")+"-" * 50)
print ("\tBem-vinde à sua Lista de Tarefas!")
print(("\t")+"-" * 50)

while continuar:
    exibir_menu()
    opcao = input ("\tInsira o que deseja fazer: ")
    if opcao =="1":
      tarefa=input('\tInsira uma nova tarefa: ')
      lista_de_tarefas=adicionar_tarefa(lista_de_tarefas,tarefa)
    elif opcao =="2":
      listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
      """Checa se o valor é númerico, se é menor que zero ou maior que o tamanho da lista"""
      tarefa =input("\tInsira o número da tarefa que deseja deletar: ")
      if not tarefa.isnumeric():
         print ("\t❌ - Este valor não é númerico! Tente novamente.")
         print(("\t")+"-" * 50)
      elif int(tarefa)>len(lista_de_tarefas):
         print ("\t❌ - Não existe tarefa que corresponda a esse número! Tente novamente.")
         print(("\t")+"-" * 50)
      elif int(tarefa)<=0:
         print ("\t❌ - Não existe tarefa que corresponda a esse número! Tente novamente.")
         print(("\t")+"-" * 50)
      else:
        deletar_tarefa(lista_de_tarefas,int(tarefa))
    elif opcao =="4":
      continuar=False
    else:
       print ("\t❌ - Opção inválida! Por favor, tente novamente.")
print ("\tObrigade por usar esse script, Até a próxima!")
print(("\t")+"-" * 50)
print("\n")
