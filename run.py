from .python-flask-api.app import app
if __name__ == '__main__':
    app.debug = True
    app.run(port=8060)