# standard imports
import os
import logging
import sys
import json
import argparse
import getpass

# external impors
import coincurve
from hexathon import strip_0x

# local imports
from funga.error import DecryptError
from funga.eth.keystore.dict import DictKeystore
#from funga.eth.signer import EIP155Signer
#from funga.eth.transaction import EIP155Transaction
from funga.eth.cli.client import RPCHTTPClient

logging.basicConfig(level=logging.WARNING)
logg = logging.getLogger()

argparser = argparse.ArgumentParser()
argparser.add_argument('-f', type=str, help='Keyfile to use for signing')
argparser.add_argument('-z', action='store_true', help='zero-length password')
argparser.add_argument('-v', action='store_true', help='be verbose')
argparser.add_argument('-0', dest='nonl', action='store_true', help='no newline at end of output')
argparser.add_argument('-a', '--signer-address', dest='signer_address', type=str, help='Ethereum address of signer')
argparser.add_argument('-i', '--chain-id', dest='chain_id', type=int, default=1, help='Ethereum address of signer')
argparser.add_argument('--value', type=int, default=0, help='Gas token unit value of transaction')
argparser.add_argument('--nonce', type=int, default=0, help='Transaction nonce')
argparser.add_argument('--fee-price', dest='fee_price', default=1, type=int, help='Gas price')
argparser.add_argument('--fee-limit', dest='fee_limit', default=21000, type=int, help='Gas limit')
argparser.add_argument('recipient_address', type=str, help='Recipient of transaction')
args = argparser.parse_args()

if args.v:
    logg.setLevel(logging.DEBUG)

rpc_signer = RPCHTTPClient()

def main():
#    passphrase = os.environ.get('WALLET_PASSPHRASE', os.environ.get('PASSPHRASE'))
#    if args.z:
#        passphrase = ''
#    if passphrase == None:
#        passphrase = getpass.getpass('decryption phrase: ')
#   
#    keystore = DictKeystore()
#    address = keystore.import_keystore_file(args.f, password=passphrase)

    tx = {
            'from': args.signer_address,
            'to': args.recipient_address,
            'value': args.value,
            'data': '0x',
            'gasPrice': args.fee_price,
            'gas': args.fee_limit,
            'chainId': args.chain_id,
            'nonce': args.nonce,
            }
    r = rpc_signer.rpc_sign_tx(tx)
    
    #tx = EIP155Transaction(tx_src, tx_src['nonce'], tx_src['chainId'])
    #print(tx)

    #signer = EIP155Signer(keystore)
    #sig = signer.sign_ethereum_message(address, args.msg.encode('utf-8').hex(), password=passphrase)
#
#    r = sig.hex()
    if not args.nonl:
        r += "\n"
    sys.stdout.write(r)


if __name__ == '__main__':
    main()
