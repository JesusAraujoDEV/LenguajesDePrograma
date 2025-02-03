import sys
import datetime
import json
import Class_task


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

    print("\nBienvenido al task traker, <utiliza el comando 'help' para mostrar la lista de comandos>")

    if(len(sys.argv) > 1):

        if(sys.argv[1].lower() == 'help'):
            mostrar_ayuda()





