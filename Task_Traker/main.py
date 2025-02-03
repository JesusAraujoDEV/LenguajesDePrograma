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

def id_task():
    while True:
        try:    
            id = int(input("Indica el indice de la tarea que desea modificar: "))
            return id 
        except ValueError:

            # Si ocurre un ValueError, significa que el valor no es un número válido
            print("Por favor, ingresa un número válido.")



if __name__ == '__main__':

    print("\t ===================================")
    print("\t ----------- Task Traker -----------")
    print("\t ===================================")

    print("\nBienvenido al task traker, <utiliza el comando 'help' para mostrar la lista de comandos>\n")

    # si tiene mas de un argumento accede a las condiciones
    if(len(sys.argv) == 2):

        #print(sys.argv)

        # lista de comandos
        if(sys.argv[1].lower() == 'help'):
            mostrar_ayuda()
        
        # verificamos si el argumento es 'create'
        elif(sys.argv[1].lower() == 'create'):

            # creamos una tarea
            Utilidad_json().create_task()

        # verificamos si el argumento es 'modify-tittle'
        elif(sys.argv[1].lower() == 'modify-tittle'):
            
            # Verificamos si existen tareas
            if(len(Utilidad_json().list_all_task()) > 0):

                # ingresamos el id de la tarea que desea modificar
                id = id_task()

                # modificamos el titulo de la tarea
                Utilidad_json().modify_task(id, "titulo")

            else:
                print("No hay tareas para modificar")

        # verificamos si el argumento es 'modify-status'
        elif(sys.argv[1].lower() == 'modify-status'):
            
            # Verificamos si existen tareas
            if(len(Utilidad_json().list_all_task()) > 0):

                # ingresamos el id de la tarea que desea modificar
                id = id_task()

                # modificamos el status de la tarea
                Utilidad_json().modify_task(id, "status")

            else:
                print("No hay tareas para modificar")

        # verificamos si el argumento es 'modify-expiration_date'
        elif(sys.argv[1].lower() == 'modify-expiration_date'):

            # Verificamos si existen tareas
            if(len(Utilidad_json().list_all_task()) > 0):

                # ingresamos el id de la tarea que desea modificar
                id = id_task()

                # modificamos el vencimiento de la tarea
                Utilidad_json().modify_task(id, "vencimiento")

            else:
                print("No hay tareas para modificar")

        # verificamos si el argumento es 'list-all'
        elif(sys.argv[1].lower() == 'list-all'):
            
            # Verificamos si existen tareas
            if(len(Utilidad_json().list_all_task()) > 0):

                # listamos todas las tareas
                task = Utilidad_json().list_all_task()

                # Mostrar todos los elementos del JSON
                for tarea in task["tareas"]:
                    print(tarea)

            else:
                print("No hay tareas para listar")

        # verificamos si el argumento es 'list-status'
        elif(sys.argv[1].lower() == 'list-status'):
            
            # Verificamos si existen tareas
            if(len(Utilidad_json().list_all_task()) > 0):

                # listamos las tareas por status
                Utilidad_json().read_tasks("status")

            else:
                print("No hay tareas para listar")

        # verificamos si el argumento es 'list-expiration_date'
        elif(sys.argv[1].lower() == 'list-expiration_date'):
            
            # Verificamos si existen tareas
            if(len(Utilidad_json().list_all_task()) > 0):

                # listamos las por fecha de vencimiento tareas
                Utilidad_json().read_tasks("vencimiento")

            else:
                print("No hay tareas para listar")

        # verificamos si el argumento es 'delete'
        elif(sys.argv[1].lower() == 'delete'):

            # Verificamos si existen tareas
            if(len(Utilidad_json().list_all_task()) > 0):

                Utilidad_json().delete_task(id)

            else:
                print("No hay tareas para eliminar")

    else:
    
        # Manejo de errores con los comandos
        print(f"Error el comando '{sys.argv}' es desconocido")
        mostrar_ayuda() # mostrar la lista de comandos disponibles





