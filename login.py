import psycopg
print(psycopg)

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

print(existe(Usuario('admin', 'a')))
