def main():
    print "Method main"
    diaRegistro()
    registroPersona()




def diaRegistro():
    print 'Dia Actual'
    diaActual = input("Dia actual: \n")
    mesActual = input("Mes Actual: \n")
    anioActual = input("Anio actual: \n")


def registroPersona():
    primerNombre = raw_input("Primer nombre: \n")
    segundoNombre = raw_input("Segundo nombre: \n")
    apellidoPaterno = raw_input("Apellido paterno: \n")
    apellidoMaterno = raw_input("Apellido materno: \n")
    diaNacimiento = input("Dia de nacimiento: \n")
    mesNacimiento = raw_input("Mes de nacimiento: \n")
    anioNacimiento = input("Anio de nacimiento: \n")
    ciudadNacimiento = raw_input("Ciudad de nacimiento: \n")

    edadPersona = anioActual - anioNacimiento

    if mesActual > mesNacimiento:
        edadPersonaA = edadPersona - 1
        print edadPersonaA

    print ('{} {} {} {}'.format(apellidoPaterno, apellidoMaterno, primerNombre, segundoNombre))
    print edadPersonaA
"""
def switch_mes(mesNacimiento):
    switcher = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre"
            }

    print switcher.get(mesNacimiento)
"""

if __name__=='__main__':
    main()
