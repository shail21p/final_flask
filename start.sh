Once Heroku CLI is installed, login to heroku using command line
# heroku login

Login to heroku container registry
# heroku container:login

Create an heroku app, if no arguments are provided, heroku assigns random name to the app
# heroku create

This is the most important step. NAVIGATE TO THE PATH WHERE “Dockerfile” is located, this will build the image and push the image to heroku registry.
heroku container:push web -a flask-app-shailpatel815

Creating the container on heroku host and hosting it publicly
# heroku container:release web -a flask-app-shailpatel815

To open the app in your default browser
heroku open -a flask-app-shailpatel815

You can check the logs of that particular heroku app
# heroku logs --tail -a <name of heroku app>