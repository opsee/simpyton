Simpyton 
========
 provides HTTP service models for testing monitoring software, anti-flap, and deduping stuff (like what you might do with riemann).  

Routes 
-------
* /{action}/{service\_id} (where action can be *list*, *register*, *services*)
* list regardless of {{service\_id}} will output the services in the service map

Service Models (and defaults)
--------------------------------
 Service models are associated with an endpoint and stochastically define the state of an HTTP service. Several default models are listed below and can be found in data/service\_modelsj

* 200.json accessible at simpyton:8000/services/200
* 404.json accessible at simpyton:8000/services/404
* 500.json accessible at simpyton:8000/services/500
* flappy.json accessible at simpyton:8000/services/flappy
* jsonassertion.json accessible at simpyton:8000/services/json
* etc

modeling flappy/etc services
---------------------------------
 Uses a simple model defined in post json to register a service whose state transition to one of N next states based on a markov transition matrix (in graph form).  This could be used to model flapping services and random service failures.  

Adding a new service model (via httpie)
----------------------------------------

``
http POST simpyton_instance:8000/register/service_id < service_model.json
``
