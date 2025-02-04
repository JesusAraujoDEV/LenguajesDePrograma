import sys
from datetime import datetime
import json
import re

# Clase para crear una tarea del task traker
class Task:

    def __init__(self,id,titulo,descripcion,fecha_vencimiento):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.status = "Pendiente"
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d")
        self.fecha_vencimiento = fecha_vencimiento



# Clase de utilidad para manejar el json donde se guardan las tareas del task traker
class Utilidad_json():

    def __init__(self):
        pass

    def read_tasks(self,operation):

        # listar alls task, for status (Pending, progress, Completed), for expiration date

        if(operation == "pendiente"):
            
            # obtengo todas las tareas
            task = self.list_all_task()

            for tarea in task["tareas"]:

                # Solo mostramos las tareas que tengan el status Pendiente
                if(tarea["status"].lower() == "pendiente"):
                    print(tarea)

        elif(operation == "progreso"):
            
            # obtengo todas las tareas
            task = self.list_all_task()

            for tarea in task["tareas"]:

                # Solo mostramos las tareas que tengan el status Progreso
                if(tarea["status"].lower() == "progreso"):
                    print(tarea)
        
        elif(operation == "completada"):
            
            # obtengo todas las tareas
            task = self.list_all_task()

            for tarea in task["tareas"]:

                # Solo mostramos las tareas que tengan el status Completada
                if(tarea["status"].lower() == "completada"):
                    print(tarea)   
        
        else:
            print(f"Esta operacion {operation} no existe")

    def list_all_task(self):
        
        # Abrir y leer el archivo
            with open("trello_task.json", "r") as archivo:
                datos = json.load(archivo)
            return datos

    def write_task(self,datos):
        
        with open("trello_task.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)

    def create_task(self):

        # entrada de datos para crear la tarea
        titulo, descripcion, vencimiento = entrada_datos()

        data = self.list_all_task()

        if len(data) == 0:
            id = 0
        else:
            id = 0
            for tarea in data["tareas"]:
                if(tarea["id"] > id):
                    id = tarea["id"]

        create_task = Task(id+1,titulo,descripcion, vencimiento)

        new_task  = {
            "id": create_task.id,
            "titulo": create_task.titulo,
            "descripcion" : create_task.descripcion,
            "status": create_task.status,
            "creacion": create_task.fecha_creacion,
            "vencimiento" : create_task.fecha_vencimiento
        }

        # obtenemos todas las tareas
        task = self.list_all_task()

        # agregamos la tarea nueva a las otras tareas
        task["tareas"].append(new_task)

        # actualizamos el json
        self.write_task(task)
        

    def modify_task(self, id, operation):

        # modify status, tittle, description, expiration date 

        # Leer todas las tareas
        tasks = self.list_all_task()
        
        # Buscar tarea por ID
        task_found = None
        for tarea in tasks["tareas"]:
            if tarea["id"] == id:
                task_found = tarea
                break

        if task_found is None:
            print("Tarea no encontrada.")
            return

        if(operation == "titulo"):
            task_found["titulo"] = input("Nuevo título: ")

        elif(operation == "descripcion"):
            task_found["descripcion"] = input("Nueva descripción: ")
        
        elif(operation == "vencimiento"):
            task_found["vencimiento"] = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")

        elif(operation == "status"):
            task_found["status"] = input("Nuevo estado (pendiente/progreso/completada): ")

        else:
            print("Operación inválida.")
            return
        
        # Guardar los cambios en el archivo JSON
        self.write_task(tasks)
        print("Tarea actualizada con éxito.")

    def delete_task(self,id):
        
        # Leer todas las tareas del archivo JSON
        tasks = self.list_all_task()
        
        # Buscar y eliminar la tarea con el ID especificado
        found = False
        for tarea in tasks["tareas"]:
            if tarea["id"] == id:
                tasks["tareas"].remove(tarea)
                found = True
                break

        if not found:
            print("Tarea no encontrada.")
        else:
            # Escribir los datos actualizados en el archivo
            self.write_task(tasks)
            print("Tarea eliminada con éxito.")



def entrada_datos():

    while True:
        try:

            titulo = input("Titulo de la tarea: ")

            # Verifica si está vacío o solo tiene espacios
            if not titulo.strip():  
                raise ValueError("El título no puede estar vacío.")
            
            descripcion = input("Descripcion de la tarea: ")

            # Verifica si está vacío o solo tiene espacios
            if not descripcion.strip():
                raise ValueError("La descripción no puede estar vacía.")
            
            vencimiento = input("Vencimiento de la tarea (YYYY-MM-DD): ")

            # Validar formato de fecha
            if not re.match(r"\d{4}-\d{2}-\d{2}", vencimiento):
                raise ValueError("La fecha de vencimiento debe estar en el formato YYYY-MM-DD.")
            

            return titulo, descripcion, vencimiento

        except ValueError as e:
            print(f"Error: {e}. Por favor, ingresa los datos nuevamente.")
