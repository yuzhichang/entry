package main

import (
	//"net"
	"os"
	"strconv"
	"log"
	"git.dev.sh.ctripcorp.com/container/entry/server"
)

func main() {
	port_s := os.Getenv("PORT")
	port := 8070
	if s, err := strconv.ParseUint(port_s, 10, 16); err == nil {
		port = int(s)
	}
	port_s = strconv.Itoa(port)
	log.Println("listening on", port)
	//server.StartServer(port_s, net.JoinHostPort("10.18.5.24", "443"))
	server.StartServer(port_s, "unix:///var/run/docker.sock")
}
