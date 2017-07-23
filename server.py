from geemusic import app
import os

if __name__ == '__main__':
    ip = os.environ.get("OPENSHIFT_PYTHON_IP", "0.0.0.0")
    port = int(os.environ.get("OPENSHIFT_PYTHON_PORT", 4000))
    app.run(host=ip, port=port, debug=True)
