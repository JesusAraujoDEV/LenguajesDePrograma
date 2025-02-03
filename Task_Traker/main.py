import sys
import datetime
import json
from Class_task import Utilidad_json


def mostrar_ayuda():

    print("""
        - 'create' <crear una tarea>
        - 'modify-tittle' <modificar el titulo de una tarea>
        - 'modify-status' <modificar el status de una tarea>
        - 'modify-expiration_date' <modificar el vencimiento de una tarea>
        - 'list-all' <listar todas las tareas>
        - 'list-status' <listar por status>
        - 'list-expiration_date' <listar por fecha de vencimiento>
        - 'delete' <eliminar una tarea>
    """)


if __name__ == '__main__':

    print("\t ===================================")
    print("\t ----------- Task Traker -----------")
    print("\t ===================================")

    print("\nBienvenido al task traker, <utiliza el comando 'help' para mostrar la lista de comandos>\n")

    # si tiene mas de un argumento accede a las condiciones
    if(len(sys.argv) > 1):

        # lista de comandos
        if(sys.argv[1].lower() == 'help'):
            mostrar_ayuda()
        
        # verificamos si el argumento es 'create'
        elif(sys.argv[1].lower() == 'create'):

            # creamos una tarea
            Utilidad_json().create_task()

        # verificamos si el argumento es 'modify-tittle'
        elif(sys.argv[1].lower() == 'modify-tittle'):
            pass

        # verificamos si el argumento es 'modify-status'
        elif(sys.argv[1].lower() == 'modify-status'):
            pass

        # verificamos si el argumento es 'modify-expiration_date'
        elif(sys.argv[1].lower() == 'modify-expiration_date'):
            pass

        # verificamos si el argumento es 'list-all'
        elif(sys.argv[1].lower() == 'list-all'):
            pass

        # verificamos si el argumento es 'list-status'
        elif(sys.argv[1].lower() == 'list-status'):
            pass

        # verificamos si el argumento es 'list-expiration_date'
        elif(sys.argv[1].lower() == 'list-expiration_date'):
            pass

        # verificamos si el argumento es 'delete'
        elif(sys.argv[1].lower() == 'delete'):
            pass





