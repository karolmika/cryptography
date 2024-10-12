#!./.venv/bin/python3

from Crypto.PublicKey import RSA

def generate_private_rsa_key(file_name):
    """ Generate Private RSA Key and save it to file in PEM format """
    # generate RSA private key
    key_priv = RSA.generate(2048)

    # convet RSA key to 'PEM' format
    key_priv_pem = key_priv.export_key(format='PEM', passphrase='karol')

    # save to file
    f = open(file_name, 'wb')
    f.write(key_priv_pem)
    f.close()
    return key_priv

def generate_public_rsa_key(key, file_name):
    key_pub = key.publickey()
    key_pub_pem = key_pub.export_key(format='PEM')
    f = open(file_name, 'wb')
    f.write(key_pub_pem)
    f.close()
    return key_pub

private_rsa_key = generate_private_rsa_key('private.pem')
public_rsa_keey = generate_public_rsa_key(private_rsa_key, 'public.pem')




