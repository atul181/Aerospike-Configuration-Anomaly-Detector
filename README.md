                                            Aerospike config anomaly detector (ascad)
                                            -----------------------------------------


Objective: 
----------
1. To compare aerospike.conf file of each machine with every other machine and report if there are any differences with respect to the configuration parameter values.
2. To compare aerospike.conf file of each machine with the GitLab aerospike.conf file and report if there are any differences with respect to the configuration parameter values.
3. To compare aerospike.conf file with the run time configuration of aerospike and report if there are any inconsistencies with respect to the configuration parameter values.

Note: The word "config" or "configuration" in this document , at all times ( unless specified ) refers to the Aerospike configuration.





Approach:
---------
Instead of comparing every machine's config with every other machine for synchronization of configs; we have adopted an architecture in which there is one master and all the other nodes in the clusters are slaves.The master is assumed to have the correct config at all times because it tries to make its config in sync with the GitLab configuration.The slaves can have wrong configuration.The slaves will repetitively get the master's config and try to make their own config in sync with it.This will eventually lead to all nodes in the cluster with the same configuration.Apart from that the each of the nodes also have to make sure that their aerospike runtime config also be in sync with their aerospike file configuration.

The project requires to run under a daemon to run periodically every 6 hrs or so to accomplish its results.






Project structure:
-------------------

This project has 5 files:

1. init.py : The entrypoint of the execution.It implements the master slave architecture of exchanging configurations from master to slave.In case of master, it starts a flask web server to let slave send config HTTP requests to the master; the master then replies back with the its own aerospike config file contents.In case of slave; it sends an HTTP request to the master flask web server to get the master's aerospike configuration.After getting the configuration it starts the comparison of both the configurations(the aerospike configuration that it has and the master's aerospike configuration that it got as the HTTP response).

2. ConfigTree.py : This major file is used to compare the configs.This file has a class which has certain methods that do the main comparison task.The task involves parsing the configuration,generating a tree out of its structure.Then comparing the trees of each config to determine the config parameters that are different.

3. flaskserver.py : This file is the file that is used by the master to start the web server and manage requests from slaves.

4. waitress_server.py : This file is nothing but a setup to use WSGI server with the flask server to make it deployable on a production environment so that the flask server can handle 100-1000 requests concurrently.

5. hostfinder.py : This is a file that does the work of finding the aerospike nodes in the cluster.






Master has following tasks to do:

1. Start a webserver where it serves its aerospike configuration to the slaves.
2. Retrieve and compare its own configuration with the gitlab configuration on the salt master.
3. Compare the aeropsike.conf file and the runtime config of aerospike.
4. Send an Ok/Critical event to riemann depending on if there were any differences in the configs that it tried to compare.

Slave has following tasks:

1. Retrieve and compare its own configuration with the configuration on the master.
2. Compare the aeropsike.conf file and the runtime config of aerospike.
3. Send an Ok/Critical event to riemann depending on if there were any differences in the configs that it tried to compare.


To run the script:
$ python3 init.py

Before running the script , there are certain variables whose values have to be set to an appropriate value.These variables are in the beginning of the above 5 python files.

It is advisable to run the init.py python file at a priority value that is lesser than the priority of Aerospike instance so that Aerospike doesnot suffer due to lack of resources because of the script.


