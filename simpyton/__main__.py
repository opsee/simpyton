from wsgiref import simple_server
from simpyton.views import Services
import requests
import falcon
import os
from config import settings

app = falcon.API()
services = Services()
app.add_route('/{action}/{service_id}', services)

print "Simpyton: v" + str(os.environ.get('SIMPYTON_VERSION'))

if __name__ == '__main__':
    httpd = simple_server.make_server(settings['server']['host'], int(settings['server']['port']), app)
    httpd.serve_forever()
