package main

import (
    "fmt"
    "singleton"
)

func main() {
    s1 := singleton.GetInstance()
    fmt.Printf("%p\n", s1)
}
