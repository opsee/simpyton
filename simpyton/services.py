from simpyton.util import *
import falcon
import requests
import json
import os
import random

__all__ = ['Http','Markov']

class Http(object):
    def __init__(self,service_description):
        self.JSONDescription = json.loads(service_description)
        self.Description = byteify(self.JSONDescription)
        self.ID = self.Description['service']

    def yield_response(self, resp):
        resp.body = 'Not implemented'

    def get_content_type(self, headers):
        for i in headers:
            if i[0].lower() == 'content-type':
                return i[1]
        return 'text/html'


    def decode_status_code(self, code):
        """
            returns falcon status code type from integer code
            TODO(dan) add the ones that are missing
        """
        x = {
                100:falcon.HTTP_100,
                101:falcon.HTTP_101,
                200:falcon.HTTP_200,
                201:falcon.HTTP_201,
                204:falcon.HTTP_204,
                300:falcon.HTTP_300,
                301:falcon.HTTP_301,
                304:falcon.HTTP_304,
                400:falcon.HTTP_401,
                401:falcon.HTTP_401,
                403:falcon.HTTP_403,
                404:falcon.HTTP_404,
                405:falcon.HTTP_404,
                500:falcon.HTTP_500,
                501:falcon.HTTP_501,
                504:falcon.HTTP_504,

            }

        if code in x:
            return x[code]
        return falcon.HTTP_799 # end of the world (you didn't include a status code in the service model)

    def decode_as_string(self, content_type, content):
        if content_type.lower() == 'application/json':
            return json.dumps(content)
        else:
            return str(content)

    def decode_response(self, jsonresponse, resp):
        response = json.loads(jsonresponse)

        content_type = 'text/html'
        headers = []
        if 'headers' in response:
            headers = [(str(i[0]), str(i[1])) for i in response['headers']]
            content_type = self.get_content_type(response['headers'])
        resp.set_headers(headers)

        body=""
        if 'body' in response:
            body = self.decode_as_string(content_type, response['body'])
        resp.data = body

        status_code=falcon.HTTP_200
        if 'status_code' in response:
            status_code=self.decode_status_code(response['status_code'])
        resp.status=status_code
        return resp


class Markov(Http):
    def __init__(self, service_description):
        """
        takes a json description of a service
        adds that service to /services/
        """

        super(Markov,self).__init__(service_description)
        chain = self.Description

        # {'state':[response(what to send back), next(transition probabilities)],...}
        self.states = dict()
        self.STATE = None

        for state in chain['states']:
            bag = [j for j in range(0,len(state['next'])) for l in range(0, int(state['next'][j][1]*100))]
            self.states[state['id']] = {'id':state['id'], 'response':state['response'], 'next':state['next'], 'bag':bag}
            if self.STATE is None:
                self.STATE=state['id']

    def yield_response(self, resp):
        """ XXX bag simple implementation make better """
        state = self.states[self.STATE]
        # return an index into the 'next' array from random bag choice
        self.STATE = state['next'][random.choice(state['bag'])][0]
        return self.decode_response(json.dumps(self.states[self.STATE]['response']), resp)

