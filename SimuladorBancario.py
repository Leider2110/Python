__auhor__= 'Leider Cadena'
__licence__= 'gpl'
__version__='1.0.0'
__email__= 'leider.cadena@campusucc.edu.co'

'''#-----------------------------------------
#Importaciones
-----------------------------------------#'''
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from Cdt import CDT

class SimuladorBancario:

    #-------------------------------------------
    #Atributos
    #-------------------------------------------

    cedula=''
    nombre=''

    cuentaCorriente = CuentaCorriente()
    cuentaAhorros = CuentaAhorros()
    cdt = CDT()

    __mesActual = 0

    #-------------------------------------------
    # Metodos
    #-------------------------------------------

    __method__='ConsignarCuentaCorriente'
    __params__='Monto'
    __returns__='Nada'
    __description__='Este metodo comsignar un monto a la cuenta corriente'
    def ConsignarCuentaCorriente(self, monto):
        #Aqui inicia el metodo
        self.__cuentaCorriente.ConsignarValor(monto)

    __method__='CalcularSaldoTotal'
    __params__='Ninguno'
    __returns__='Saldo Total'
    __description__='Este metodo suma el saldo de todas las cuentas'
    def CalcularSaldoTotal(self):
        #Aqui inicia el metodo
        total = self.__cuentaCorriente.DarSaldo()+self.__ceuntaAhorros.DarSaldo()
        return total

    __method__='PasarAhorrosACorriente'
    __params__='Ninguno'
    __returns__='Ninguno'
    __description__='Este metodo transfiere el saldo de ahorro a corriente'
    def PasarAhorrosACorriente(self):
        saldoTemporal = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.ConsignarValor(saldoTemporal)

    __method__ = "RetirarTodo"
    __parameter__ = "Monto"
    __return__ = "Ninguna"
    __Description__="metodo que permita retirar el saldo total de la cuenta"    
    def RetirarTodo(self):
        # Aqui inicia mi codigo
        SaldoCorriente= self.__CuentaCorriente.DarSaldo()
        self.__CuentaCorriente.RetirarSaldo(SaldoCorriente)
        SaldoAhorros= self.__CuentaAhorros.DarSaldo()
        self.__CuentaAhorros.RerirarSaldo(SaldoAhorros)
        return self(SaldoAhorros+SaldoCorriente)

    

    __method__ = "DuplicarAhorro"
    __parameter__ = "Monto*2"
    __return__ = "Ninguna"
    __Description__="metodo que permita duplicar monto de la cuenta de ahorros"    
    def DuplicarAhorros(self):
        # Aqui va mi codigo
        SaldoAhorros = self.__CuentaAhorros.DarSaldo()
        return self(SaldoAhorros*2)