cp init.py ConfigTree.py flaskserver.py hostfinder.py waitress_server.py /Users/atul.intern/Deploy/
cp init.py ConfigTree.py flaskserver.py hostfinder.py waitress_server.py ../aspy/
scp /Users/atul.intern/Deploy/* sre@stg-atul001.phonepe.nb6:/home/sre/testaerospike/
scp /Users/atul.intern/Deploy/* sre@stg-atul002.phonepe.nb6:/home/sre/testaerospike/
scp /Users/atul.intern/Deploy/* sre@stg-atul003.phonepe.nb6:/home/sre/testaerospike/