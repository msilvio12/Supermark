class Usuario():
      
      numUsuarios=0

    
      def __init__(self, nombre, contraseña):
         self.nombre=nombre
         self.contraseña=contraseña

         self.conectado=False
         self.intentos=3

         Usuario.numUsuarios+=1
      
      
      def conectar(self, contrasenia=None):
        if contrasenia==None:
          miContra= input("Ingrese su contraseña: ")
        else:
          miContra=contrasenia 
          if miContra==self.contraseña:
            print("Se conecto con exito: ")
            self.conectado= True
            return True
          else:
            self.intentos-=1
            if self.intentos > 0:
               print("Contraseña incorrecta, intenta de nuevo!: ")
               if contrasenia!=None:
                return False
               print("Intentos restantes", self.intentos)
               self.conectar() 
            else:
                print("Error no se pudo iniciar sesion")
                print("intente mas tarde o restablezca su contraseña")



      def desconectar(self):
           if self.conectado:
            print("Se cerro con exito su sesion")
            self.conectado= False
        


      def __str__(self):
          if self.conectado:
              connect="Conectado"
          else:
              connect="Desconectado"
              return f'Mi nombre de usuario es: {self.nombre} y estoy {connect}'          

#user1= Usuario(input("Ingrese un nombre"), input("Ingrese su contraseña"))
#print(user1)

#user1.conectar()
#print(user1)

#user1.desconectar()
#print(user1)