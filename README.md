# IoT Green Calculator
This web service provides estimates in MJ and kg for the energy and waste impacts of the devices employed in an IoT solution. 
The energy impact considers the production and utilization phase while the waste impacts is computed as the disposal of the device. 
The IoT green calculator considers each device as equipped with an solar energy harvesting solution, in addition it takes into account the impacts deriving from the maintenance. 
IoT green calculator computes a green proposal that is used as a reference solution.
It is possible to understand hoa green an IoT solution is considering how far the impacts of the solution proposed are from the impacts of the green proposal.


## Prerequisites
Python:      3.7.x

Flask:       1.1.1

Werkzeug:    0.16.0

Bootstrap4:  https://getbootstrap.com/

Chart.js:    https://www.chartjs.org/docs/latest/getting-started/installation.html

Gurobi:      https://www.gurobi.com/documentation/9.0/quickstart_mac/the_grb_python_interface_f.html

## Installing
to run the webservice it is sufficient to execute:

```python app.py``` 

open a web browser and connect to the local server. 

## How to use the calculator
The web service provides six forms to acquire the information about the user application.
It is possible to indicates information related to:

* microcontroller
* radio module
* sensors
* printed circuit boards
* solar panel
* battery
* maintenance

When all the forms are submited the service show the graphs of the impacts and the comparison between the user and the green soltuions.

## Authon
Edoardo Baldini
