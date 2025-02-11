package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

type song struct {
	ID        int    `json:"ID"`
	Title     string `json:"Title"`
	Album     string `json:"Album"`
	Duration  string `json:"Duration"`
	URL_Image string `json:"URL_Image"`
	URL_Song  string `json:"URL_Song"`
}

type Allsongs []song

var songs = Allsongs{
	{
		ID:        1,
		Title:     "Elf",
		Album:     "Elf",
		Duration:  "4:20",
		URL_Image: "https://i.scdn.co/image/ab67616d0000b2739e1c223d7a087f9dfb3757fe",
		URL_Song:  "https://open.spotify.com/track/0235CQ0hquNPhCvcDVPj0Y?si=dc13c6b2f5544937",
	},
	{
		ID:        2,
		Title:     "踊 (Odo)",
		Album:     "狂言 (Kyogen)",
		Duration:  "3:30",
		URL_Image: "https://m.media-amazon.com/images/I/71-QIs-F2ZL._UF1000,1000_QL80_.jpg",
		URL_Song:  "https://open.spotify.com/track/2MuWTIM3b0YEAskbeeFE1i?si=0f9b748b79964d7e",
	},
	{
		ID:        3,
		Title:     "うっせぇわ (Usseewa)",
		Album:     "狂言 (Kyogen)",
		Duration:  "3:24",
		URL_Image: "https://m.media-amazon.com/images/I/71-QIs-F2ZL._UF1000,1000_QL80_.jpg",
		URL_Song:  "https://open.spotify.com/track/5xrtzzzikpG3BLbo4q1Yul?si=6e8694777a4b4e1d",
	},
	{
		ID:        4,
		Title:     "新時代 (Shinjidai)",
		Album:     "ONE PIECE FILM RED",
		Duration:  "3:49",
		URL_Image: "https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/Ado_-_Uta%27s_Songs%2C_One_Piece_Film_Red.png/220px-Ado_-_Uta%27s_Songs%2C_One_Piece_Film_Red.png",
		URL_Song:  "https://open.spotify.com/track/1ew7qJcTiwJvMeU97jxi7z?si=90a42b50c3f74e7e",
	},
	{
		ID:        5,
		Title:     "ギラギラ (Gira Gira)",
		Album:     "ギラギラ",
		Duration:  "3:57",
		URL_Image: "https://m.media-amazon.com/images/I/71-QIs-F2ZL._UF1000,1000_QL80_.jpg",
		URL_Song:  "https://open.spotify.com/track/4GtTUp9fak2ueWnjk1sov7?si=5405b0f7f2834dd2",
	},
	{
		ID:        6,
		Title:     "私は最強 (Watashi wa Saikyou)",
		Album:     "ONE PIECE FILM RED",
		Duration:  "4:10",
		URL_Image: "https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/Ado_-_Uta%27s_Songs%2C_One_Piece_Film_Red.png/220px-Ado_-_Uta%27s_Songs%2C_One_Piece_Film_Red.png",
		URL_Song:  "https://open.spotify.com/track/6HR1pSOrwxrxLrKm7dT1YF?si=48b7c2873c99482e",
	},
}

func createsongs(w http.ResponseWriter, r *http.Request) {
	var newsong song
	reqBody, err := ioutil.ReadAll(r.Body)
	if err != nil {
		fmt.Fprint(w, "Insert a valid song")
	}
	json.Unmarshal(reqBody, &newsong)
	newsong.ID = len(songs) + 1
	songs = append(songs, newsong)

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(newsong)
}

func getsongs(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(songs)
}

func getsong(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	vars := mux.Vars(r)
	song_id, err := strconv.Atoi(vars["id"])
	if err != nil {
		fmt.Fprint(w, " Invalid ID")
		return
	}

	for _, song := range songs {
		if song.ID == song_id {
			json.NewEncoder(w).Encode(song)
		}
	}
}

func Deletesong(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	song_id, err := strconv.Atoi(vars["id"])
	if err != nil {
		fmt.Fprint(w, " Invalid ID")
		return
	}

	for i, song := range songs {
		if song.ID == song_id {
			songs = append(songs[:i], songs[i+1:]...)
			fmt.Fprintf(w, "The song with ID %v has been removed successfully", song_id)
		}
	}
}

func Updatesong(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	song_id, err := strconv.Atoi(vars["id"])
	var updatedsong song
	if err != nil {
		fmt.Fprint(w, " Invalid ID")
		return
	}

	reqBody, err := ioutil.ReadAll(r.Body)
	if err != nil {
		fmt.Fprint(w, " Please Enter Valid Data")
		return
	}
	json.Unmarshal(reqBody, &updatedsong)

	for i, song := range songs {
		if song.ID == song_id {
			songs = append(songs[:i], songs[i+1:]...)
			updatedsong.ID = song_id
			songs = append(songs, updatedsong)
			fmt.Fprintf(w, "The song with ID %v has been updated successfully", song_id)
		}
	}
}

func main() {
	router := mux.NewRouter().StrictSlash(true)

	// Servir archivos estáticos desde la carpeta "static"
	router.PathPrefix("/static/").Handler(http.StripPrefix("/static/", http.FileServer(http.Dir("./static"))))

	// Ruta para la página principal
	router.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, "static/index.html")
	})

	// Rutas de la API
	router.HandleFunc("/songs", getsongs).Methods("GET")
	router.HandleFunc("/songs", createsongs).Methods("POST")
	router.HandleFunc("/songs/{id}", getsong).Methods("GET")
	router.HandleFunc("/songs/{id}", Deletesong).Methods("DELETE")
	router.HandleFunc("/songs/{id}", Updatesong).Methods("PUT")

	log.Fatal(http.ListenAndServe(":3000", router))
}
