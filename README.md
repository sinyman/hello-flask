# Hello Flask

This is a basic application made to have something to push to DockerHub in exercise 1.15 of the DevOpswithDocker MOOC course at the University of Helsinki. [Here is the repo for the submissions for that course](https://github.com/sinyman/devopsWithDocker)

This isn't a in-depth project nor does it really have any complexity in writing the Dockerfile, but I assume the main point of the exercise is to prove that you are able to push something to DockerHub. This repo will do just that.

## How to run it?

The following two steps will start a local server that is accessible via your web browser on the URL `localhost:5000`

### Docker

Pull the image from DockerHub like this:
```bash
$ docker pull sinyman/hello-flask
```

And there are really no specifics to run the project, other than that it is a flask app, so it will be availasble on port 5000.
So you can for example run it like this:
```bash
$ docker run -d -p 5000:5000 sinyman/hello-flask:<tag>
```

### Python
First, make sure you have all the requirements installed (basically only flask). You can install these with the following command (you might want to do this in a virtual environment as to not make a mess of your local pip):
```bash
$ (python -m) pip install -r requirements.txt
```

Then, just run the following command in the project root to start a local server:
```bash
$ python app.py
```

