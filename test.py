from ConfigTree import ConfigTree

text1='''
Configuration:
    service {
             group root
              user root
            paxos-single-replica-limit 1 # Number of nodes where the replica count is automatically reduced to 1.
            pidfile /var/run/aerospike/asd.pid
            service-threads 24
            transaction-queues 4
            transaction-threads-per-queue 4
            proto-fd-max 15000

    }



    network {
        service {
            address any
            access-address 172.16.43.5
            port 3000
        }

        heartbeat {
            mode mesh

            port 3002 # Heartbeat port for this node.
            address 172.16.43.5
            # List one or more other nodes, one ip-address & port per line:
            # Please note that we do not have the address of the incoming node in this list
            mesh-seed-address-port 172.16.43.7  3002
            mesh-seed-address-port 172.16.43.5  3002
            # Having the node itself as a mesh seed node is allowed
            # and helps with consistent configuration files across the cluster

            interval 250
            timeout 10
        }

        fabric {
            port 3001
        }

        info {
            port 3003
        }
    }

    namespace test {
                                   # Data in memory without persistance namespace
        replication-factor 2
        memory-size 32G
        default-ttl 30d               # 30 days, use 0 to never expire/evict.
        storage-engine memory
    }
'''
text2='''
Configuration:
    service {
            user root
            group root
            paxos-single-replica-limit 1 # Number of nodes where the replica count is automatically reduced to 1.
            pidfile /var/run/aerospike/asd.pid
            service-threads 24
            transaction-queues 4
            transaction-threads-per-queue 4
            proto-fd-max 15000

    }



    network {
        service {
            address any
            access-address 172.16.43.5
            port 3000
        }

        heartbeat {
            mode mesh

            port 3002 # Heartbeat port for this node.
            address 172.16.43.5
            # List one or more other nodes, one ip-address & port per line:
            # Please note that we do not have the address of the incoming node in this list
            mesh-seed-address-port 172.16.43.7  3002
            mesh-seed-address-port 172.16.43.5  3002
            # Having the node itself as a mesh seed node is allowed
            # and helps with consistent configuration files across the cluster

            interval 250
            timeout 10
        }

        fabric {
            port 3001
        }

        info {
            port 3003
        }
    }

    namespace test {
                                   # Data in memory without persistance namespace
        replication-factor 2
        memory-size 32G
        default-ttl 30d               # 30 days, use 0 to never expire/evict.
        storage-engine memory
    }
'''

print(ConfigTree.isSame(text1,text2)[0])