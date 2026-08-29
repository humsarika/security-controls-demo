from flask import Flask, request
import os
 
app = Flask(__name__)
 
@app.route("/ping")
def ping():
    # Command Injection Vulnerability
    ip = request.args.get("ip")
    os.system("ping -c 1 " + ip)
    return "Pinging " + ip
 
if __name__ == "__main__":
    app.run()
