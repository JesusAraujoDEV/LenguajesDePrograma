# 🛠 Guía de Entorno y Pruebas Unitarias


## 📦 Dependencias Utilizadas
Este proyecto utiliza las siguientes dependencias:
- **pytest** → Se usa para ejecutar pruebas unitarias de manera automática.

Puedes instalarlas con:
```sh
pip install pytest
```

---

## 📂 Estructura del Proyecto
- **`src/main.py`** → Contiene las funciones principales que se ponen a prueba.
- **`src/models/LanguajeModel.py`** → Contiene modelos y funciones que también son testeadas.
- **`src/tests/`** → Carpeta donde se encuentran los códigos que ejecutan las pruebas unitarias.

Los archivos de prueba **empiezan con "test"** y se encargan de importar las funciones de los archivos mencionados, verificando los resultados esperados con `assert`.

---

## 🧪 Ejecutar Pruebas Unitarias
Para ejecutar todas las pruebas unitarias, usa el siguiente comando en la raíz del proyecto:

```sh
pytest -v
```

Esto mostrará detalles sobre cada prueba realizada.

---


🚀 ¡Listo para probar tu código de forma eficiente! 🎯

