#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
import os 
import json 



app = Flask(__name__)
api = Api(app)

class DiskUsage(Resource):
    def df_h(self):
        df = []
        dfCmd = os.popen("df -h ")
        i = 0
        while True: 
            line = dfCmd.readline()
            if line != '':
                i = i + 1
                if i > 1: #Suppression de la première ligne du df -h
                    lineDatas = line.split()[0:6] #Pour parser le fichier
                    df.append({ #Les attributs d'un objet pour le JSON de fin
                        "filesystem" : lineDatas[0],
                        "size" : lineDatas[1],
                        "used" : lineDatas[2],
                        "available" : lineDatas[3],
                        "used_percent" : lineDatas[4],
                        "mountpoint" : lineDatas[5],
                    })
            else:
                break
        return df

    def get(self):
        return self.df_h()

class Processes(Resource):
    def listProcesses(self):
        content = []
        statusCmd = os.popen("ps -ef")
        i = 0
        while True:
            line = statusCmd.readline()
            if line != '':
                i = i + 1
                if i > 1:
                    lineDatas = line.split()[0:8]
                    content.append({
                        'uid': lineDatas[0],
                        'pid': lineDatas[1],
                        'ppid': lineDatas[2],
                        'c': lineDatas[3],
                        'stime': lineDatas[4],
                        'tty': lineDatas[5],
                        'time': lineDatas[6],
                        'cmd': lineDatas[7]
                    })
            else:
                break
        return content

    def killService(self):
        data = request.form
        if 'process' in data:
            os.popen("systemctl stop " + data['process'])
            return { True }
        return { False }

    def get(self):
        return self.listProcesses()
    
    def post(self):
        return self.killService()

api.add_resource(DiskUsage, '/disk_usage')
api.add_resource(Processes, '/processes')


if __name__ == '__main__':
    app.run(debug=True)