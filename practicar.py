def login_usuarios(usuario,contraseña):
    
    print("Inicio de Sesión")
    
    #Pregunta para inicio de sesion

    input1 = None
    input2 = None
    
    while input1 != usuario or input2 != contraseña:
         input1 = input("Indica tu Usuario: ")
         input2 = input("Indica tu Contraseña: ")
         
         if input1 != usuario and input2 == contraseña:
            print("Error de Usuario")
            
         elif input1 == usuario and input2 != contraseña:
            print("Error de contraseña")
            
         else:
            print("Bienvenido a nuestro sistema: ", usuario)
        
def run():
    #Registro de Usuario
    print("Bienvenido a la interfaz de pruebas")
    usuario = input("Indica un Usuario: ")
    contraseña = input("Indica una Contraseña: ")
    print("Usuario Registrado con exito")
    login_usuarios(usuario,contraseña)
    
run()