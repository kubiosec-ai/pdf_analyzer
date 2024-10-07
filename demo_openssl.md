# Setting Up Signed and Encrypted Email with OpenSSL (Part 1)

*Author: Philippe Bogaerts, aka xxradar*  
*Published on: 20-09-2003*  
*Version: 1.0*  
*[Original publication URL (archived as of 2023) ↗](http://www.radarhack.com)  
*Contact: xxradar@radarhack.com*

## Overview

This document provides a detailed guide on setting up a Certificate Authority (CA) using OpenSSL for the purpose of generating certificates that can be used for signing and encrypting emails, specifically for use with Microsoft Outlook. As of the original writing in 2003, this guide was tailored for a Windows environment. It offers a hands-on approach to Public Key Infrastructure (PKI) through a command-line interface using OpenSSL, bypassing graphical user interfaces (GUIs).

## Introduction

After extensive study of PKI and certificates, I chose OpenSSL for hands-on implementation rather than relying on GUI tools. I found numerous conflicting resources and decided to document what worked for me. This document describes installing OpenSSL, configuring it to act as a CA, and generating certificates.

## 1. Installing OpenSSL

### For Windows

1. **Download OpenSSL:**
   - Search for "OpenSSL for Windows" for the latest distributions or visit [OpenSSL's official page](https://www.openssl.org) for references to trusted sources.
   - You can find both a simple ZIP file version and a more user-friendly installer.

2. **Installation Steps:**
   - If using the ZIP file, extract it to a directory such as `C:\openssl`.
   - Ensure that the necessary DLL files are copied to the `%systemroot%\system32` directory.

3. **Directory Setup:**
   - Create a directory to work as your CA, for instance: `C:\openssl\my_ca`.
   - Inside `my_ca`, create the following subdirectories:
     ```
     certs
     crl
     csr
     newcerts
     private
     ```
   - Create an empty file `index.txt` in `C:\openssl\my_ca\`.
   - Create a `serial` file containing `01` in `C:\openssl\my_ca\`:
     ```bash
     echo 01 > serial
     ```

4. **OpenSSL Configuration:**
   - Edit or create `openssl.cnf` in `C:\openssl` to match your setup. Below is a minimal configuration you might start with:

```ini
[ ca ]
default_ca = CA_default

[ CA_default ]
dir = ./my_ca
certs = $dir/certs
crl_dir = $dir/crl
database = $dir/index.txt
new_certs_dir = $dir/newcerts
certificate = $dir/certs/ca.crt
serial = $dir/serial
crl = $dir/crl.pem
private_key = $dir/private/cakey.key
RANDFILE = $dir/private/private.rnd
x509_extensions = x509v3_extensions
default_days = 365
default_crl_days = 30
default_md = md5
preserve = no
policy = policy_match

[ policy_match ]
countryName = optional
stateOrProvinceName = optional
organizationName = optional
organizationalUnitName = optional
commonName = supplied
emailAddress = optional

[ req ]
default_bits = 1024
default_keyfile = privkey.pem
distinguished_name = req_distinguished_name
attributes = req_attributes

[ req_distinguished_name ]
countryName = Country Name (2 letter code)
countryName_min = 2
countryName_max = 2
stateOrProvinceName = State or Province Name (full name)
localityName = Locality Name (eg, city)
organizationName = Organization Name (eg, company)
organizationalUnitName = Organizational Unit Name (eg, section)
commonName = Common Name (eg, your website's domain name)
commonName_max = 64
emailAddress = Email Address
emailAddress_max = 40

[ req_attributes ]
challengePassword = A challenge password
challengePassword_min = 4
challengePassword_max = 20

[ x509v3_extensions ]
```

### Additional Notes
- Make sure only one version of OpenSSL is available in your system’s PATH to prevent configuration conflicts.
- Use the [official OpenSSL releases](https://www.openssl.org/source/) to avoid security risks associated with unofficial versions.

## 2. Create a CA Certificate and Keys

### Generate RSA Keys for the CA

```bash
C:\openssl>openssl genrsa -des3 -out ./my_ca/private/cakey.key 2048
```

- **Output Message**: You'll be prompted to set a passphrase to secure the private key.

### Create the CA Certificate

```bash
C:\openssl>openssl req -new -x509 -days 365 -key ./my_ca/private/cakey.key -out ./my_ca/certs/ca.crt
```

- You will be asked to provide details such as Country, State, Organization, etc., to populate the certificate's Distinguished Name (DN).

### Distribution of CA Certificate

The resulting `ca.crt` file is the root certificate for your CA. To ensure security:
- *Securely distribute the certificate* to users who need to trust emails signed by this CA.
- *Install the CA certificate* on client machines: Double-click `ca.crt` and follow the prompts to add it to the Trusted Root Certification Authorities in Windows.

## 3. Create Certificates for Users

### Generate a User Key

```bash
C:\openssl>openssl genrsa -des3 -out .\my_ca\private\user1.key 2048
```

### Generate a Certificate Signing Request (CSR)

```bash
C:\openssl>openssl req -new -key .\my_ca\private\user1.key -out .\my_ca\csr\user1.csr
```

### Sign the Certificate with the CA

```bash
C:\openssl>openssl ca -config .\openssl.cnf -policy policy_anything -out .\my_ca\newcerts\user1.pem -infiles .\my_ca\csr\user1.csr
```

### Convert Certificate to PKCS#12 Format (for Importing to Outlook)

```bash
C:\openssl>openssl pkcs12 -export -in ./my_ca/newcerts/user1.pem -inkey ./my_ca/private/user1.key -out ./my_ca/newcerts/user1.p12
```

- *Provide an export password* when prompted. This will secure the PKCS#12 file.

### User Certificate Installation

Double-click `user1.p12` to install the certificate for use with Outlook’s email encryption/signing features. Verify the certificate through Internet Explorer via:  
`Tools -> Internet Options -> Content -> Certificates`

### Repeat for Additional Users (e.g., user2)

Follow the same steps to create and distribute certificates to any additional users.

## Conclusion

This guide provided a step-by-step process to set up a CA and generate certificates for email encryption and signing using OpenSSL. Following these instructions will give you a basic understanding of PKI and how to manage certificates on a Windows machine.

For continuous updates and more in-depth knowledge, keep checking the [OpenSSL documentation](https://www.openssl.org/docs/) and additional cryptography best practices.

---

*Note to readers*: Public Key Infrastructure and cryptographic practices evolve. Always ensure that you use the latest versions of tools and follow up-to-date security recommendations.
