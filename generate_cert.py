#!/usr/bin/env python
"""
Generate self-signed SSL certificates for local development.
This creates cert.pem and key.pem in the connectly_project directory.
"""
import os
import sys
from datetime import datetime, timedelta

try:
    from cryptography import x509
    from cryptography.x509.oid import NameOID
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
except ImportError:
    print("Error: cryptography module not found.")
    print("Install it with: pip install cryptography")
    sys.exit(1)

def generate_self_signed_cert(cert_dir="connectly_project"):
    """Generate a self-signed certificate for local development."""
    
    # Ensure directory exists
    if not os.path.exists(cert_dir):
        print(f"Error: Directory '{cert_dir}' not found.")
        sys.exit(1)
    
    print("Generating SSL certificate...")
    
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    
    # Generate certificate
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "State"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "City"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Connectly Dev"),
        x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
    ])
    
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.utcnow()
    ).not_valid_after(
        datetime.utcnow() + timedelta(days=365)
    ).add_extension(
        x509.SubjectAlternativeName([
            x509.DNSName("localhost"),
            x509.DNSName("127.0.0.1"),
        ]),
        critical=False,
    ).sign(private_key, hashes.SHA256())
    
    # Write private key
    key_path = os.path.join(cert_dir, "key.pem")
    with open(key_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    print(f"✓ Private key written to: {key_path}")
    
    # Write certificate
    cert_path = os.path.join(cert_dir, "cert.pem")
    with open(cert_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    print(f"✓ Certificate written to: {cert_path}")
    
    print("\nSSL certificates generated successfully!")
    print("You can now run: python manage.py runserver_plus --cert-file cert.pem --key-file key.pem")

if __name__ == "__main__":
    generate_self_signed_cert()
