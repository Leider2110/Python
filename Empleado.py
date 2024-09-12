__auhor__= 'Leider Cadena'
__licence__= 'gpl'
__version__='1.0.0'
__email__= 'leider.cadena@campusucc.edu.co'

'''--------------------------------------------------------
# Importaciones
--------------------------------------------------------'''

from Fecha import Fecha

class Empleado:
    # Aqui inicia mi clase

    '''#--------------------------------------------------
    # Atributos
    --------------------------------------------------#'''

    nombre=''
    apellido=''
    salario=0

    '''#--------------------------------------------------
    # 1 Maculino y 2 Femenino
    --------------------------------------------------#'''

    sexo=0

    '''#--------------------------------------------------
    # Asociaciones
    --------------------------------------------------#'''

    fechaNacimiento= Fecha()
    fechaIngreso= Fecha()

    '''#--------------------------------------------------
    # Metodos
    --------------------------------------------------#'''

    __method__='CambiarSalario'
    __params__='NuevoSalario'
    __returns__='Nada'
    __description__='Este metodo permite cambiar el salario del empleado po uno nuevo'

    def CambiarSalario(self, nuevoSalario):
        # Aqui inicia el metodo
        self.salario = nuevoSalario

    __method__='CambiarSalario'
    __params__='NuevoSalario'
    __returns__='Nada'
    __description__='Este metodo permite cambiar el salario del empleado po uno nuevo'

    def DarSalario(self):
        # Aqui inicia el metodo
        return self.salario

    __method__='DarSalario'
    __params__='Ninguno'
    __returns__='Salario empleado'
    __description__='Devuelve el salario del empleado'

    def AumentoSalarial(self, Aumento):
        #Aqui inicia el meotodo
        self.salario = self.salario+Aumento

    __method__='AumentoSalarial'
    __params__='Aumento'
    __returns__='Salario empleado'
    __description__='Permite aumentar el salario en un valor ingresado por el usuario'