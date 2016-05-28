Simpyton 
========
provides HTTP service models for testing monitoring software, anti-flap, and deduping stuff (like what you might do with riemann).  

Routes 
-------
* /{action}/{service\_id} (where action can be *register* or *services*)

Default service models
--------------------------------
Service models are associated with an endpoint and yield static or dynamic responses based on predefined states and transition probabilities. Several default models are listed below and can be found in data/service\_modelsj

* simpyton:8000/services/200
* simpyton:8000/services/404
* simpyton:8000/services/500
* simpyton:8000/services/flappy (responses vary between states based on random draw)
* simpyton:8000/services/json
* simpyton:8000/services/longresponse (10k character response)
* simpyton:8000/services/redirect (redirects to google)

Adding a new service model (via httpie)
----------------------------------------
``
http POST simpyton_instance:8000/register/service_id < service_model.json
``
