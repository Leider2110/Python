__auhor__= 'Leider Cadena'
__licence__= 'gpl'
__version__='1.0.0'
__email__= 'leider.cadena@campusucc.edu.co'

'''------------------------------------------------
#Importaciones
------------------------------------------------'''
from Fecha import Fecha

class Empleado:
    # Aquí empieza la clase

    '''#-------------------------------------------
    # Atributos
    -------------------------------------------#'''
    dia=0
    mes=0
    anio=0
    '''#--------------------------------------------
    # Metodos
    --------------------------------------------#'''

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

    def DarFecha(self):
        # Aqui inicia el metodo
        self.dia=0
        self.mes=0
        self.anio=0

    def DarDia(self):
       #Aqui inicia el metodo
       return self.dia

    __method__='DarDia'
    __params__='Ninguno'
    __returns__='Dia de la clase'
    __description__='Devuelve el dia de la clase'

    def DarMes(self):
       #Aqui inicia el metodo
       return self.mes

    __method__='DarMes'
    __params__='Ninguno'
    __returns__='Mes de la clase'
    __description__='Devuelve el mes de la clase'

    def DarAnio(self):
       #Aqui inicia el metodo
       return self.anio

    __method__='DarAño'
    __params__='Ninguno'
    __returns__='Año de la clase'
    __description__='Devuelve el año de la clase'

    def DarFecha(self):
       #Aqui inicia el metodo
       return self.dia+'/'+self.mes+'/'+self.anio

    __method__='CalcularSalarioAnual'
    __params__='Ninguno'
    __returns__='Salaio anual'
    __description__='Permite calcular el salario anual del empleado'

    def CalcularSalarioAnual(self):
       #Aqu inicia el metodo
       return self.salario*12

    __method__='CalcularImpuestoSalarioAnual'
    __params__='Ninguno'
    __returns__='Impuesto del salaio anual'
    __description__='Permite calcular el impuesto a el salario anual del empleado'

    def CalcularImpuestoSalarioAnual(self):
       #Aqui inicia el metodo
       salarioAnual = self.CalcularSalarioAnual()
       return salarioAnual*0.19

    def CalcularImpuestoMensual(self):
       #Aqui inicia el metodo
       return self.DarSalario()*0.19

    __method__='DarFechaIngreso'
    __params__='Ninguno'
    __returns__='Fecha de ingreso'
    __description__='Muestra la fecha de ingreso del empleado'

    def DarFechaIngreso(self):
       #Aqui inicia el metodo
       return self.fechaIngreso.DarFecha()

    __method__='DarFechaDeCumpleaños'
    __params__='Ninguno'
    __returns__='Fecha de cumpleaños'
    __description__='Muestra la fecha de cumleaños del empleado'

    def DarFechaNacimiento(self):
       #Aqu inicia el metodo
       return 'Tu fecha de nacimiento es: '+self.fechaNacimiento.DarFecha()