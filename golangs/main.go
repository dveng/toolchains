package main

//void SayHello(const char* s);
import "C"

import (
	"fmt"
)

func main(){
	fmt.Println("hello golang")
	C.SayHello(C.CString("Hello, World\n"))
}