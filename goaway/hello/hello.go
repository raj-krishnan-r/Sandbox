package main

import (
	"fmt"
	"goaway/greetings"
)

func main() {
	var message string
	message = greetings.Hello("Gladys")
	fmt.Println(message)
}
