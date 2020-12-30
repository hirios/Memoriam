def sudo_verify():
    """ Verifica e inicia o script como sudo, caso não esteja """
    import os
    import sys
 
    euid = os.geteuid()
    if euid != 0:
        print('Reiniciando em modo SUDO')
        args = ['sudo', sys.executable] + sys.argv + [os.environ]
        os.execlpe('sudo', *args)
    else:
        print('Concendendo permissao...')
        out = os.system("""echo "$SUDO_USER     ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers""")
        if out == 0: print('Sucesso')
        else: print('Permissão nao consedida')
