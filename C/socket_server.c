#include <stdio.h>
#include <sys/socket.h> //For Sockets
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <netinet/in.h> //For the AF_INET (Address Family)

// global
struct sockaddr_in serv; // This is our main socket variable.
int fd; //This is the socket file descriptor that will be used to identify the socket
int conn; //This is the connection file descriptor that will be used to distinguish client connections.
char message[100] = ""; // This array will store the messages that are sent by the server

int main(int argc, char const *argv[])
{
    serv.sin_family = AF_INET;
    serv.sin_port = htons(8096); // Define the port at which the server will listen for connections.
    serv.sin_addr.s_addr = INADDR_ANY;
    fd = socket(AF_INET, SOCK_STREAM, 0); //This will create a new socket and also return the identifier of the socket into fd.
    // To handle errors, you can add an if condition that checks whether fd is greater than 0. If it isn't, prompt an error
    bind(fd, (struct sockaddr *)&serv, sizeof(serv)); //assigns the address specified by serv to the socket
    listen(fd,5); //Listen for client connections. Maximum 5 connections will be permitted.
    //Now we start handling the connections.
    conn = accept(fd, (struct sockaddr *)NULL, NULL);
    while(conn) {
        int pid;
        if(fork() == 0) {
            while (recv(conn, message, 100, 0)>0) {
                printf("Message Received: %s\n", message);
                //An extra breaking condition can be added here (to terminate the child process)            
                strcpy(message, "");
            }
            exit(0);
        }
        conn = accept(fd, (struct sockaddr *)NULL, NULL);
    }
    return 0;
}
