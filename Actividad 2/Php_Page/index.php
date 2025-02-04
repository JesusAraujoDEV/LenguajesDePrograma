<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario Simple</title>
    <link rel="stylesheet" href="styles.css">

</head>
<body>

    <div class="div-form">
    <h2>Formulario de Contacto</h2>

        <form method="POST" action="">
            <label for="nombre">Nombre:</label><br>
            <input type="text" id="nombre" name="nombre" required><br>

            <label for="correo">Correo:</label><br>
            <input type="email" id="correo" name="correo" required><br>

            <button type="submit">Enviar</button>
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $nombre = htmlspecialchars($_POST["nombre"]);
            $correo = htmlspecialchars($_POST["correo"]);
            
            echo "<h3>Datos recibidos:</h3>";
            echo "<p><strong>Nombre:</strong> $nombre</p>";
            echo "<p><strong>Correo:</strong> $correo</p>";
        }
        ?>
    </div>



</body>
</html>
