import psycopg
# print(psycopg)

class Usuario:
  def __init__(self, login, senha):
    self.login = login
    self.senha = senha

def existe (usuario):
  with psycopg.connect(
    host="localhost",
    dbname="20231_pbdi_login_python",
    port=5432,
    user='rodrigo',
    password="123456"
  ) as conexao:
    with conexao.cursor() as cursor:
      cursor.execute(
        'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
        (f'{usuario.login}', f'{usuario.senha}')
      )
      result = cursor.fetchone()
      return result != None

# u = Usuario('admin', 'fewafewfwa')
# print(existe(u))
#0-Sair
#1-Login
#2-Logoff
def menu():
  texto = '0-Fechar sistema\n1-Login\n2-Logoff\n'
  usuario = None
  opcao = int(input(texto))
  while opcao != 0:
    if opcao == 1:
      login = input("Digite seu login\n")
      senha = input("Digite sua senha\n")
      usuario = Usuario(login, senha)
      # expressão condicional (if/else de uma linha só)
      print("Usuário OK!" if existe(usuario) else "Usuário NOK!")
    elif opcao == 2:
      usuario = None
      print ("Logoff realizado com sucesso")
    opcao = int(input(texto))
  else:
    print ("Até mais")

menu()



