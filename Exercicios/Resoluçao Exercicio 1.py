usuarios = [input("Digite o primeiro usuario: "), input("Digite o segundo usuario: "), input("Digite o terceiro usuario: ")]

for user in usuarios:
    if user.lower()=="admin":
        print("Olá administrador, temos relátorios à observar")
    elif user.lower()=="user":
        print("Olá usuario seja bem vindo")
    elif user.lower()=="estagiario":
        print("Por favor, não mexa em nada!")
    else:
        print("Ola visitante")