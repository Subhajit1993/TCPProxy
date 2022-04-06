from flaskr.controllers.home import home_bp
from flask import current_app, render_template, request, json, Response
import logging
import os
import subprocess
import sys
import psutil


@home_bp.before_app_request
def before_request():
    pass


@home_bp.route('/', methods=['GET'])
def index():
    data = {
        "env": os.getenv("FLASK_ENV")
    }
    return render_template('index.html', data=data)


@home_bp.route('/upstream', methods=['post'])
def upstream():
    post_data = request.data
    post_data_dict = json.loads(post_data)
    tunnel = post_data_dict.get('tunnel')
    upstream = post_data_dict.get('upstream')
    delay = post_data_dict.get('delay')
    command = ["python3", "./flaskr/lib/ProxyCreator.py", tunnel["ip"], tunnel["port"], upstream["ip"],
               upstream["port"], str(delay)]
    process = subprocess.Popen(command)
    return {
               "pid": process.pid
           }, 200


@home_bp.route('/kill-process/<pid>', methods=['delete'])
def killProcess(pid):
    process = psutil.Process(int(pid))
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()
    return {}, 200
