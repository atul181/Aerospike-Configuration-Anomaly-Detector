from ConfigTree import ConfigTree

text1='''
security {
    enable-security true
}

service {
        cluster-name as4xx
        paxos-single-replica-limit 1 # Number of nodes where the replica count is automatically reduced to 1.
        proto-fd-max 15000
        log-local-time true
        
        node-id 82f40f6fcf76e981
        feature-key-file /etc/aerospike/features.conf
}


network {
	tls phonepeaerospike {
		cert-file /etc/aerospike/ssl/server.crt
		key-file /etc/aerospike/ssl/server.key
		ca-path /etc/aerospike/ssl/
	}

        service {
                tls-port 4333
                tls-address 10.57.12.89
                tls-authenticate-client false
                tls-name phonepeaerospike
        }

    	heartbeat {
            	mode mesh
            	port 3002
		mesh-seed-address-port 10.57.12.84 3002
		mesh-seed-address-port 10.57.12.89 3002
		mesh-seed-address-port 10.57.12.90 3002
		
		address 10.57.12.89

            	interval 150
            	timeout 10
    	}
        fabric {
		tls-address 10.57.12.89
                tls-port 3011
                tls-name phonepeaerospike
        }
        info {
           port 3003
        }
}

logging {
	file /var/log/aerospike/aerospike.log {
		context any info
		context migrate debug
	}
}

namespace payments-router {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/payments-router.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace payments {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/payments.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace olympusim {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/olympusim.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace mercator {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/mercator.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace checkout {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
	high-water-memory-pct 70
        high-water-disk-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/checkout.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace switch-oracle {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/switch-oracle.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace switch-discovery {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/switch-discovery.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace precium {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/precium.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace user {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/user.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace user_audience {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/user_audience.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace dsp_user_sync {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/dsp_user_sync.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace postimp_events {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/postimp_events.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace external_data {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/external_data.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace yakshaprashna {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/yakshaprashna.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace chimera-pz {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
	high-water-memory-pct 70
        high-water-disk-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/chimera-pz.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace profilestore {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/profilestore.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace gandalf {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
	high-water-memory-pct 70
        high-water-disk-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/gandalf.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace khata {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
	high-water-memory-pct 70
	stop-writes-pct 90
        nsup-period 120
        high-water-disk-pct 70
	storage-engine device {
		file /var/lib/aerospike/khata.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace mercury {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
        high-water-disk-pct 70
	high-water-memory-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/mercury.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}
namespace mutual_fund {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
        high-water-disk-pct 70
	high-water-memory-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/mutual_fund.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace offers {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        high-water-disk-pct 70
        storage-engine device {
                file /var/lib/aerospike/offers.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace apphub {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        high-water-disk-pct 70
        storage-engine device {
                file /var/lib/aerospike/apphub.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace users {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        high-water-disk-pct 70
        storage-engine device {
                file /var/lib/aerospike/users.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace sentinel {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/sentinel.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace zencast {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/zencast.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace hawkeye {
        enable-xdr false
        memory-size 16G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/hawkeye.dat
                filesize 32G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace anomaly_detection {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/anomaly_detection.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace atlas {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/atlas.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace ablaze {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/ablaze.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}


namespace pgtransport {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/pgtransport.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace upi {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/upi.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

xdr {
        enable-xdr false
        forward-xdr-writes true
        xdr-digestlog-path /var/lib/aerospike/xdr/digestlog 50G

        datacenter NB649X {
                #tls-node <ip> phonepeaerospike 4333
                tls-name phonepeaerospike
                #dc-security-config-file /etc/aerospike/security-credentials_NB1.txt
        }

}


'''
text2='''
security {
    enable-security true
}

service {
        cluster-name as4xx
        paxos-single-replica-limit 1 # Number of nodes where the replica count is automatically reduced to 1.
        proto-fd-max 15000
        log-local-time true
        
        node-id 0000f74faf229f15
        feature-key-file /etc/aerospike/features.conf
}


network {
	tls phonepeaerospike {
		cert-file /etc/aerospike/ssl/server.crt
		key-file /etc/aerospike/ssl/server.key
		ca-path /etc/aerospike/ssl/
	}

        service {
                tls-port 4333
                tls-address 10.57.12.90
                tls-authenticate-client false
                tls-name phonepeaerospike
        }

    	heartbeat {
            	mode mesh
            	port 3002
		mesh-seed-address-port 10.57.12.84 3002
		mesh-seed-address-port 10.57.12.89 3002
		mesh-seed-address-port 10.57.12.90 3002
		
		address 10.57.12.90

            	interval 150
            	timeout 10
    	}
        fabric {
		tls-address 10.57.12.90
                tls-port 3011
                tls-name phonepeaerospike
        }
        info {
           port 3003
        }
}

logging {
	file /var/log/aerospike/aerospike.log {
		context any info
		context migrate debug
	}
}

namespace payments-router {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/payments-router.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace payments {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/payments.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace olympusim {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-memory-pct 70
        high-water-disk-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/olympusim.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace mercator {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/mercator.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace checkout {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
        high-water-disk-pct 70
	high-water-memory-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/checkout.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace switch-oracle {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/switch-oracle.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace switch-discovery {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/switch-discovery.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace precium {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/precium.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace user {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/user.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace user_audience {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/user_audience.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace dsp_user_sync {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/dsp_user_sync.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace postimp_events {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/postimp_events.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace external_data {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/external_data.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace yakshaprashna {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/yakshaprashna.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace chimera-pz {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
        high-water-disk-pct 70
	high-water-memory-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/chimera-pz.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace profilestore {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/profilestore.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace gandalf {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
        high-water-disk-pct 70
	high-water-memory-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/gandalf.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace khata {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
        high-water-disk-pct 70
	high-water-memory-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/khata.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace mercury {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
        high-water-disk-pct 70
	high-water-memory-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/mercury.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}
namespace mutual_fund {
        enable-xdr false
	memory-size 1G
	replication-factor 2
	default-ttl 0
        high-water-disk-pct 70
	high-water-memory-pct 70
	stop-writes-pct 90
        nsup-period 120
	storage-engine device {
		file /var/lib/aerospike/mutual_fund.dat
		filesize 2G
		data-in-memory true
		write-block-size 128K
		defrag-lwm-pct 50
		defrag-startup-minimum 10
	}
}

namespace offers {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/offers.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace apphub {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/apphub.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace users {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/users.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace sentinel {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/sentinel.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace zencast {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/zencast.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace hawkeye {
        enable-xdr false
        memory-size 16G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/hawkeye.dat
                filesize 32G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace anomaly_detection {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/anomaly_detection.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace atlas {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/atlas.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace ablaze {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/ablaze.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}


namespace pgtransport {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/pgtransport.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

namespace upi {
        enable-xdr false
        memory-size 1G
        replication-factor 2
        default-ttl 0
        high-water-disk-pct 70
        high-water-memory-pct 70
        stop-writes-pct 90
        nsup-period 120
        storage-engine device {
                file /var/lib/aerospike/upi.dat
                filesize 2G
                data-in-memory true
                write-block-size 128K
                defrag-lwm-pct 50
                defrag-startup-minimum 10
        }
}

xdr {
        enable-xdr false
        forward-xdr-writes true
        xdr-digestlog-path /var/lib/aerospike/xdr/digestlog 50G

        datacenter NB649X {
                #tls-node <ip> phonepeaerospike 4333
                tls-name phonepeaerospike
                #dc-security-config-file /etc/aerospike/security-credentials_NB1.txt
        }

}

'''

a,b,d=ConfigTree.isSame(text1,text2)
#print(a)
c=ConfigTree.makeCorrectConfig(b,d)
#print(ConfigTree.genPaths(c))
ConfigTree.stringify(c,-2)
print(''.join(ConfigTree.config))
