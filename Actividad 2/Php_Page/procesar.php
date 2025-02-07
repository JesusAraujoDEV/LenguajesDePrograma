<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenido</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>


<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $usuario = htmlspecialchars($_POST["usuario"]);
    $correo = htmlspecialchars($_POST["correo"]);
    $telefono = htmlspecialchars($_POST["telefono"]);
    $password = htmlspecialchars($_POST["password"]);

    // Datos de usuario de prueba
    $usuario_correcto = "admin";
    $correo_correcto = "admin@example.com";
    $password_correcto = "123456";

    // Validar credenciales
    if ($usuario == $usuario_correcto && $correo == $correo_correcto && $password == $password_correcto) {
        echo "<div class='card'>";
        echo "<h2>Resultado del Inicio de Sesión</h2>";

        echo "<h3>¡Bienvenido, $usuario!</h3>";
        echo "<p><strong>Nombre:</strong> $usuario</p>";
        echo "<p><strong>Correo:</strong> $correo</p>";
        echo "<p><strong>Teléfono:</strong> $telefono</p>";
        echo "</div>";
    } else {
        echo "<p style='color:red;'>Usuario o contraseña incorrectos.</p>";
        echo "<a href='index.php'>Volver al Login</a>";
    }
} else {
    echo "<p>No se han recibido datos.</p>";
}
?>

</body>
</html>
