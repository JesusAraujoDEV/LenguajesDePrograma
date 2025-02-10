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

type task struct {
	ID      int    `json:ID`
	Name    string `json:Name`
	Content string `json:Content`
}

type AllTasks []task

var tasks = AllTasks{
	{
		ID:      1,
		Name:    "Tarea 1",
		Content: "Some Content",
	},
}

func createTasks(w http.ResponseWriter, r *http.Request) {
	var newTask task
	reqBody, err := ioutil.ReadAll(r.Body)
	if err != nil {
		fmt.Fprint(w, "Insert a valid Task")
	}
	json.Unmarshal(reqBody, &newTask)
	newTask.ID = len(tasks) + 1
	tasks = append(tasks, newTask)

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(newTask)
}

func getTasks(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(tasks)
}

func getTask(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	vars := mux.Vars(r)
	task_id, err := strconv.Atoi(vars["id"])
	if err != nil {
		fmt.Fprint(w, " Invalid ID")
		return
	}

	for _, task := range tasks {
		if task.ID == task_id {
			json.NewEncoder(w).Encode(task)
		}
	}
}

func DeleteTask(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	task_id, err := strconv.Atoi(vars["id"])
	if err != nil {
		fmt.Fprint(w, " Invalid ID")
		return
	}

	for i, task := range tasks {
		if task.ID == task_id {
			tasks = append(tasks[:i], tasks[i+1:]...)
			fmt.Fprint(w, "The task with ID %v has been removed succesfully", task_id)
		}
	}

}

func UpdateTask(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	task_id, err := strconv.Atoi(vars["id"])
	var updatedTask task
	if err != nil {
		fmt.Fprint(w, " Invalid ID")
		return
	}

	reqBody, err := ioutil.ReadAll(r.Body)
	if err != nil {
		fmt.Fprint(w, " Please Enter Valid Data")
		return
	}
	json.Unmarshal(reqBody, &updatedTask)

	for i, task := range tasks {
		if task.ID == task_id {
			tasks = append(tasks[:i], tasks[i+1:]...)
			updatedTask.ID = task_id
			tasks = append(tasks, updatedTask)
			fmt.Fprint(w, "The task id with ID %v has been updated succesfully", task_id)
		}
	}
}

func indexRoute(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "WELCOME TO ADO API LETSGOOOOO")
}

func main() {

	router := mux.NewRouter().StrictSlash(true)

	router.HandleFunc("/", indexRoute)
	router.HandleFunc("/tasks", getTasks).Methods("GET")
	router.HandleFunc("/tasks", createTasks).Methods("POST")
	router.HandleFunc("/tasks/{id}", getTask).Methods("GET")
	router.HandleFunc("/tasks/{id}", DeleteTask).Methods("DELETE")
	router.HandleFunc("/tasks/{id}", UpdateTask).Methods("PUT")
	log.Fatal(http.ListenAndServe(":3000", router))
}
