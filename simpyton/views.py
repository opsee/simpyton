from simpyton.services import Markov
from simpyton.util import *
import falcon
import base64
import json
import os
import pprint
import copy

__all__=['Services']

class Services:
    def __init__(self):
        """
            initialize default services if they don't exist
        """
        self.SERVICEMAP = dict()
        service_ext = '.json'
        for f in os.listdir('./data/service_models'):
            if f.endswith(service_ext):
                with open('./data/service_models/'+f) as _file:
                    service_id = f[:len(f)-len(service_ext)]
                    self.SERVICEMAP[service_id] = Markov(_file.read().replace('\n',''))
                    if len(self.SERVICEMAP[service_id].ID) > 0:
                        print "init: registered ", service_id
                    else:
                        print "init: couldn't register ", service_id

    def on_get(self, req, resp, action, service_id):
        if action == 'services':
            self.get_service_response(resp, req, service_id)
        if action == 'list':
            self.enumerate_services(resp)

    def on_post(self, req, resp, action, service_id):
        if action == 'register':
            self.register_service(resp, req, service_id)
        if action == 'services':
            self.get_service_response(resp, req, service_id)

    def on_put(self, req, resp, action, service_id):
        if action == 'services':
            self.get_service_response(resp, req, service_id)

    def on_delete(self, req, resp, action, service_id):
        if action == 'services':
            self.get_service_response(resp, req, service_id)

    def get_service_response(self, resp, req, service_id):
        if service_id in self.SERVICEMAP:
            self.SERVICEMAP[service_id].yield_response(resp)

    def register_service(self, resp, req, service_id):
        """
            A flappy service with a markov chain
        """
        try:
            raw_json = req.stream.read()
            print raw_json
            self.SERVICEMAP[service_id] = Markov(raw_json)
            resp = falcon.Response()
            resp.body = "Couldn't register"
            if len(self.SERVICEMAP[service_id].ID) > 0:
                resp.body = "Registered."
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)

    def enumerate_services(self, resp):
        services = ""
        for key,service in self.SERVICEMAP.iteritems():
            services += "ID: " + service.ID + "\n"
            services += "- PATH: /services/" + key +"\n"
        services += ""
        resp.data = services
