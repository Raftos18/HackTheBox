package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"regexp"
)

func postForm(client http.Client, URL string, value string) []byte {

	resp, err := client.PostForm(URL,
		url.Values{"hash": {value}})

	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		log.Fatal(err)
	}

	return body
}

func extractValueToHash(data []byte) []byte {

	exp, err := regexp.Compile(`<h3 align='center'>(.*)<\/h3>`)

	if err != nil {
		log.Fatal(err)
	}

	value := exp.FindAllStringSubmatch(string(data), -1)

	if value == nil {
		log.Fatal("Matching value not found")
	}

	fmt.Println("Value to hash", string(value[0][1]))

	return []byte(value[0][1])
}

func md5Hash(value []byte) string {
	hasher := md5.New()
	hasher.Write(value)
	hashed := hex.EncodeToString(hasher.Sum(nil))
	fmt.Println("Hashed value", hashed)
	return hashed
}

func main() {

	URL := "http://docker.hackthebox.eu:31135/"

	var client http.Client

	resp, err := client.Get(URL)

	if err != nil {
		log.Fatal(err)
	}

	cookieJar, _ := cookiejar.New(nil)
	cookieURL, _ := url.Parse(URL)
	cookieJar.SetCookies(cookieURL, resp.Cookies())
	client.Jar = cookieJar

	defer resp.Body.Close()

	body, _ := ioutil.ReadAll(resp.Body)

	value := extractValueToHash(body)

	hashedValue := md5Hash(value)

	body = postForm(client, URL, hashedValue)

	fmt.Println(string(body))
}
