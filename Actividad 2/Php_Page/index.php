<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>


<div class="div-form">
<h2 style="color: white;">Iniciar Sesión</h2>

<form method="POST" action="procesar.php">
    <label for="usuario">Usuario:</label><br>
    <input type="text" id="usuario" name="usuario" required><br>

    <label for="correo">Correo:</label><br>
    <input type="email" id="correo" name="correo" required><br>

    <label for="telefono">Teléfono:</label><br>
    <input type="tel" id="telefono" name="telefono" required><br>

    <label for="password">Contraseña:</label><br>
    <input type="password" id="password" name="password" required><br>

    <button type="submit">Ingresar</button>
</form>
</div>

</body>
</html>
