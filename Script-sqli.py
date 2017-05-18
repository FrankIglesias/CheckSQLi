import sys
import urllib
import urllib.request

for carg in sys.argv:
        if carg == "-w":
            argnum = sys.argv.index(carg)
            argnum+=1
            fullurl = sys.argv[argnum]
            resp = urllib.request.urlopen(fullurl + "%20and%20persona%20=%20%27enrique%27")
            body = resp.read()
            fullbody= body.decode('utf-8')
            if  "SQL syntax" in fullbody or "column" in fullbody:
                print ("La pagina es bulnerable a SQL injection")
            else:
                print("La pagina es segura de SQL injection")
