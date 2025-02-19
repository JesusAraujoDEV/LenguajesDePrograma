// URL de la API
const API_URL = "http://localhost:3000/songs";

// Función para obtener las canciones de la API
async function fetchSongs() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error("Error al obtener las canciones");
    }
    const songs = await response.json();
    displaySongs(songs);
  } catch (error) {
    console.error("Error:", error);
  }
}

// Función para mostrar las canciones en la página
function displaySongs(songs) {
  const songsList = document.getElementById("songs-list");
  songsList.innerHTML = ""; // Limpiar la lista antes de agregar nuevas canciones

  songs.forEach((song) => {
    const songItem = document.createElement("a"); // Convertimos la tarjeta en un enlace
    songItem.classList.add("song-item");
    songItem.href = song.URL_Song; // Enlace a la canción
    songItem.target = "_blank"; // Abrir en nueva pestaña
    songItem.style.textDecoration = "none"; // Quitar subrayado del enlace

    songItem.innerHTML = `
      <h3>${song.Title}</h3>
      <p><strong>Álbum:</strong> ${song.Album}</p>
      <p><strong>Duración:</strong> ${song.Duration}</p>
      <img src="${song.URL_Image}" alt="${song.Title}" loading="lazy">
    `;

    songsList.appendChild(songItem);
  });
}
//Profe escuche ado :D
// Llamar a la función para obtener y mostrar las canciones al cargar la página
fetchSongs();
