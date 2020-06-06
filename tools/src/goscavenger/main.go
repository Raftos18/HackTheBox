package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"sync"
)

func readDir(dir string) []os.FileInfo {

	files, err := ioutil.ReadDir(dir)
	if err != nil {
		log.Fatal(err)
	}

	return files
}

func readFile(filename string) []byte {
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	return content
}

func containsPwd(filepath string) bool {
	matched, err := regexp.Match(`password.*`, readFile(filepath))

	if err != nil {
		log.Fatal(err)
	}

	return matched
}

func walkDir(dir string) []string {

	var filepaths []string

	err := filepath.Walk(dir,
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			if info.IsDir() == false {
				filepaths = append(filepaths, path)
			}
			return nil
		})
	if err != nil {
		log.Println(err)
	}

	return filepaths
}

func main() {

	currentDir := os.Args[1]

	var wg sync.WaitGroup

	filepaths := walkDir(currentDir)
	for _, filepath := range filepaths {

		wg.Add(1)

		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			containsPwd := containsPwd(filepath)
			if containsPwd {
				fmt.Printf("%v: %v\r\n", filepath, containsPwd)
			}
		}(&wg)

		wg.Wait()
	}

}
