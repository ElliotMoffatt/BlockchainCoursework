import blockcypher

#Specify the inputs and outputs below
#For convenince you can specify an address, and the backend will work out what transaction output that address has available to spend
#You do not need to list a change address, by default the transaction will be created with all change (minus the fees) going to the first input address
inputs = [{'address': 'n4KqzBMw2tgTWJeib2AQGYBc2cqH3jyUx1'}]
outputs = [{'address': 'mpamtqLA66JFVSQNDaPHZ5xMiCz6T2MeNn', 'value': 100}]
#The next line creates the transaction shell, which is as yet unsigned
unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet', api_key='8c4d64277d0f4330913059a8d80f4526')

#You can edit the transaction fields at this stage, before signing it.


#Now list the private and public keys corresponding to the inputs
private_keys=['6c51e22b3cc2c4965787463ec3057e22bcdf7fb4cdd2db928de052d0c8c1a4dc']
public_keys=['035b3a06f1425bcf38005bb54cf77f23932ce36a20ce80cb430304f0e17a21dbf2']
#Next create the signatures
tx_signatures = blockcypher.make_tx_signatures(txs_to_sign=unsigned_tx['tosign'], privkey_list=private_keys, pubkey_list=public_keys)
#Finally push the transaction and signatures onto the network
blockcypher.broadcast_signed_transaction(unsigned_tx=unsigned_tx, signatures=tx_signatures, pubkeys=public_keys, coin_symbol='btc-testnet', api_key='8c4d64277d0f4330913059a8d80f4526')
