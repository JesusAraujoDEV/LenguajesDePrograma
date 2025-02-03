import sys
import datetime
import json

# Clase para crear una tarea del task traker
class Task:

    def __init__(self,titulo,descripcion,fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.status = "Pendiente"
        self.fecha_creacion = datetime.datetime().now().strftime("%Y-%m-%d %H:%M:%S")
        self.fecha_vencimiento = fecha_vencimiento



# Clase de utilidad para manejar el json donde se guardan las tareas del task traker
class Utilidad_json():

    def __init__(self):
        pass

    def read_tasks(self,operation):

        # listar alls task, for status (Pending, progress, Completed), for expiration date

        if(operation == "Pendiente"):
            pass

        elif(operation == "Progreso"):
            pass
        
        elif(operation == "Completada"):
            pass

        elif(operation == "Vencimiento"):
            pass

        else:
            pass
        
        pass

    def write_task(self):
        pass

    def create_task(self):

        titulo = input("Titulo de la tarea: ")
        descripcion = input("Descripcion de la tarea: ")
        vencimiento = input("Vencimiento de la tarea: ")
        

    def modify_task(self, operation):

        # modify status, tittle, description, expiration date 

        if(operation == "Titulo"):
            pass

        elif(operation == "descripcion"):
            pass
        
        elif(operation == "Vencimiento"):
            pass

        elif(operation == "status"):
            pass

        pass

    def delete_task(self):
        pass



