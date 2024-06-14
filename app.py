from flask import Flask

app = Flask(__name__)

main_html = "<body style='background-color:aquamarine;'> \
		<h1>Hello DevOps with Docker!</h1><br> \
		<a href='https://github.com/sinyman/devopsWithDocker'>Here is a link to the repo for my submission</a><br> \
		<a href='https://github.com/sinyman/hello-flask'>And here is a link to the the repo for this project</a> \
	    </body>"

@app.route('/')
def hello_world():
    return main_html

if __name__ == '__main__':
    app.run(host='0.0.0.0')

