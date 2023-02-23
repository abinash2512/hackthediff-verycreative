from project import app
from gunicorn.app.wsgiapp import run

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)