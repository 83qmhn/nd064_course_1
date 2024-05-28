# set the base image. Since we're running 
# a Go application a Golang base image is used
FROM golang:alpine
LABEL maintainer="Lois Li"

# set the working directory to /go/src/app
WORKDIR /go/src/app

# copy all the files from the current directory to the container working directory
ADD . .

# import dependencies using `go mod init` and build the application using `go build -o helloworld` command
RUN  go mod init && go build -o helloworld

# expose the port 6111
EXPOSE 6111

# start the container and run helloworld
CMD ["./helloworld"]