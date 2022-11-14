# Funga - Ethereum implementation

See https://git.defalsify.org/funga for more details.

## Tools

When installed with pip/setuptools, this package provides a Unix socket IPC server as `funga-ethd` implementing the following web3 json-rpc methods:

* web3.eth.personal.newAccount
* web3.eth.personal.signTransaction
* web3.eth.signTransaction

## Funga interface implementations

- **ReferenceKeystore**: Implements the `Keystore` interface, with a postgresql backend expecting sql schema as defined in `ReferenceKeystore.schema`
- **ReferenceSigner** Implements `Signer`, accepting a single argument of type `Keystore` interface. 
- **EIP155Transaction**: Creates transaction serializations appropriate for EIP155 replay protected signatures. Accepts a web3 format transaction dict as constructor argument together with nonce and optional chainId.
