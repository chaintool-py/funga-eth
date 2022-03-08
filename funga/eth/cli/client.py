# standard imports
import urllib.request
import json

# external imports
import jsonrpc_std.interface


class RPCHTTPClient:

    def __init__(self, host='localhost', port=8000):
        self.host = host
        self.port = port
        self.url = 'http://{}:{}'.format(host, port)


    def rpc_sign_tx(self, tx, request_id=None, passphrase=''):
        data_src = jsonrpc_std.interface.jsonrpc_request('personal_signTransaction', request_id=request_id)
        data_src['params'].append(tx)
        data_src['params'].append(passphrase)
        data = json.dumps(data_src)
        req = urllib.request.Request(self.url, data=data.encode('utf-8'))
        req.add_header('Accept', 'application/json')
        req.add_header('Content-Type', 'application/json')
        r = urllib.request.urlopen(req)
        v = r.read()
        return v.decode('utf-8')
