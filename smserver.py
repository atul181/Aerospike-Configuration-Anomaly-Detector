from flask import Flask

remoteConfFileLocation="/srv/salt/base/aerospike/nb6/aspp60x/aero_config.stg_nb6-1.TEMPLATE"


def rsc(conf):
    #remove salt code.
    conf=conf.split('\n')
    i=0
    while i<len(conf)
        if "__CLUSTER__" in conf[i]:
            conf.pop(i)
            continue
        elif ("{{" in conf[i]) and ("}}" in conf[i]):
            conf[i]=conf[i].split("{{")[0]+' random'
        elif "{%"  in conf[i] and ('%}' in conf[i]):
            conf.pop(i)
            continue 
        i+=1
    return '\n'.join(conf)

    




app = Flask(__name__)

@app.route('/asrconf')
def conf():
    conf=open(remoteConfFileLocation,"r").read()
    conf=rsc(conf)
    return conf


app.run(host='0.0.0.0', port=81)