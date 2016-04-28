from wsgiref import simple_server
from simpyton.views import Services
import requests
import falcon
import os

app = falcon.API()
services = Services()
app.add_route('/{action}/{service_id}', services)

print "Simpyton: " + os.environ['SIMPYTON_VERSION']
# Useful for debugging problems in your API; works with pdb.set_trace()
if __name__ == '__main__':
    httpd = simple_server.make_server(os.environ['SIMPYTON_HOST'], int(os.environ['SIMPYTON_PORT']), app)
    httpd.serve_forever()
