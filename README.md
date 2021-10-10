# Studies Repo
This is a repo that I use to study everything that I need to know and curious about something.

> As this repo is a block building infrastruct and template for new implementation solutions, I'll be looking to fast deployment.

I currently have two setups as follows:

1. Desktop = Linux (ArchLinux - Manjaro Distro)
2. Notebook = MacOS ( MacBook Air M1)
# Summary

1. Docker

***

# Docker

## Objective of Learning
> This would help me implement everything as fast as I can.

## Why's and What's
Docker is a open source platform to build, execute and deploy of containers.

Containers are "encapsulated" applications that uses controlled environments of your system to maintain consistency of execution. Making everything replicable by using scriptable deployment called Dockerfile, like requirements.txt in Python and pom.xml in Java with Maven or package.json in JavaScript with NPM.

Dockerfile builds Containers with commands and look like this:

```Dockerfile
FROM image
ENV environment_attributes
WORKDIR directory
COPY file to_directory
RUN bash_command
```

## Installation
```terminal
sudo pamac install docker
```
Couldn't make AUR [docker-git](https://aur.archlinux.org/packages/docker-git/) work by any means at moment.

Followed the getting-started tutorial to learn the basics:
 - docker pull
 - docker run

### Dockerfile
> Dockerfile is an automated docker container builder.

