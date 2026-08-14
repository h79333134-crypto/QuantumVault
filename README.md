# QuantumVault

### Post-Quantum Secure File Transfer using Hybrid Encryption

**QuantumVault** is a post-quantum secure file transfer prototype that demonstrates how conventional symmetric encryption can be combined with a standardized post-quantum key encapsulation mechanism to protect files against both present-day and future cryptographic threats.

The system uses **AES-256-GCM** for high-performance authenticated file encryption and **ML-KEM-768** for post-quantum secure key establishment. A Flask-based web interface provides a simple environment for demonstrating secure file transmission between an authorized sender and receiver while simulating an unauthorized attacker.

---

## Overview

The emergence of large-scale quantum computers presents a significant challenge to widely deployed public-key cryptographic systems such as RSA and ECC.

Algorithms based on integer factorization and discrete logarithms are vulnerable to **Shor's algorithm**, creating a long-term security concern for information that must remain confidential for many years.

QuantumVault explores a practical migration-oriented approach:

> **Use symmetric cryptography for the data and post-quantum cryptography for protecting the key material.**

Instead of attempting to encrypt an entire file using a post-quantum KEM, QuantumVault uses ML-KEM-768 to establish/protect the key material required for the symmetric encryption layer.

This provides an efficient hybrid architecture suitable for demonstrating post-quantum secure file exchange.

---

## Problem Statement

Traditional secure file-transfer systems commonly rely on RSA or elliptic-curve cryptography for key establishment.

Although these algorithms remain secure against currently available classical computers when properly implemented, sufficiently capable quantum computers could compromise their security through Shor's algorithm.

This creates a need to investigate cryptographic architectures that can remain secure in a post-quantum environment.

QuantumVault addresses this problem by combining:

* **AES-256-GCM** for authenticated bulk-data encryption
* **ML-KEM-768** for post-quantum key establishment
* **Receiver-specific key material** to restrict decryption
* **Authenticated encryption** to detect tampering and invalid ciphertext

---

## Objectives

QuantumVault was developed with the following objectives:

1. Demonstrate a practical hybrid post-quantum encryption architecture.
2. Encrypt files using AES-256-GCM.
3. Integrate ML-KEM-768 into the key-establishment process.
4. Restrict successful decryption to the intended receiver.
5. Demonstrate the failure of unauthorized decryption attempts.
6. Provide a simple browser-based interface for visualization and demonstration.
7. Illustrate the role of post-quantum cryptography in modern secure communication.

---

## Key Features

| Feature                    | Description                                               |
| -------------------------- | --------------------------------------------------------- |
| **AES-256-GCM**            | Authenticated encryption for file contents                |
| **ML-KEM-768**             | Post-quantum key encapsulation                            |
| **Hybrid Encryption**      | Combines symmetric encryption with PQC                    |
| **Receiver-Specific Keys** | Encryption is associated with the intended recipient      |
| **Integrity Protection**   | GCM authentication detects modified ciphertext            |
| **Web Interface**          | Browser-based demonstration using Flask                   |
| **Attacker Simulation**    | Demonstrates unauthorized decryption failure              |
| **Local File Handling**    | Encrypted and decrypted files can be demonstrated locally |

---

## System Architecture

```text
                         QUANTUMVAULT
                              │
                              ▼
                    ┌───────────────────┐
                    │   Flask Web App   │
                    └─────────┬─────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
       ┌─────────────┐                 ┌─────────────┐
       │    Sender   │                 │  Receiver   │
       │   (Dhruv)   │                 │   (Rahul)   │
       └──────┬──────┘                 └──────┬──────┘
              │                               │
              │ Upload File                   │ Private Key
              ▼                               │
       ┌─────────────┐                        │
       │ AES-256-GCM │                        │
       │ File Encrypt│                        │
       └──────┬──────┘                        │
              │                               │
              │ Encrypted File                │
              ▼                               │
       ┌─────────────┐                        │
       │  Key Layer  │◄───────────────────────┘
       │ ML-KEM-768  │
       └──────┬──────┘
              │
              ▼
     ┌──────────────────────┐
     │ Encrypted File       │
     │ ML-KEM Ciphertext    │
     │ Required Parameters  │
     └──────────┬───────────┘
                │
                ▼
         ┌──────────────┐
         │ Decryption   │
         │ Process      │
         └──────┬───────┘
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
   Valid Receiver     Unauthorized
        │                │
        ▼                ▼
   AES Decryption     Access Denied
        │
        ▼
   Original File
```

---

## Cryptographic Design

QuantumVault follows a **hybrid encryption model**.

### Why hybrid encryption?

Public-key and post-quantum cryptographic mechanisms are generally not intended to encrypt large files directly.

Symmetric algorithms such as AES are significantly more efficient for bulk data encryption.

Therefore, the system separates the problem into two layers:

```text
┌──────────────────────────────────────────────┐
│              FILE ENCRYPTION                 │
│                                              │
│              AES-256-GCM                     │
│                                              │
│       Efficient bulk-data encryption         │
└──────────────────────┬───────────────────────┘
                       │
                       │ AES Key
                       ▼
┌──────────────────────────────────────────────┐
│             KEY ESTABLISHMENT                │
│                                              │
│              ML-KEM-768                     │
│                                              │
│      Post-quantum secure key mechanism       │
└──────────────────────────────────────────────┘
```

This approach allows the system to benefit from the performance of symmetric encryption while introducing a post-quantum cryptographic mechanism into the key-establishment layer.

---

# Encryption and Decryption Workflow

## 1. Key Generation

The intended receiver possesses an ML-KEM-768 key pair:

```text
ML-KEM-768 Key Pair

        ┌─────────────────────┐
        │     Public Key      │
        └──────────┬──────────┘
                   │
                   │ Used by Sender
                   ▼
        ┌─────────────────────┐
        │     Encapsulation   │
        └─────────────────────┘

        ┌─────────────────────┐
        │    Private Key      │
        └──────────┬──────────┘
                   │
                   │ Used by Receiver
                   ▼
        ┌─────────────────────┐
        │     Decapsulation   │
        └─────────────────────┘
```

The receiver's private key remains associated with the receiver and is not shared with other users.

---

## 2. File Encryption

The sender selects a file through the web interface.

For example:

```text
report.pdf
```

A fresh AES-256 key is generated for the encryption operation.

The file is then encrypted using AES-256-GCM.

```text
report.pdf
     │
     ▼
AES-256-GCM
     │
     ▼
report.pdf.enc
```

AES-GCM additionally provides authentication, allowing the system to detect invalid or modified ciphertext during decryption.

---

## 3. Key Protection

The AES encryption key is protected through the ML-KEM-768 layer.

Conceptually:

```text
AES Encryption Key
        │
        ▼
ML-KEM-768 Key Establishment
        │
        ▼
Protected Key Material
```

The encrypted file and the information required for the key-recovery process are then made available to the intended receiver.

---

## 4. Authorized Decryption

When the intended receiver attempts to decrypt the file:

```text
Encrypted File
      │
      ▼
Receiver's ML-KEM Private Key
      │
      ▼
Key Recovery
      │
      ▼
AES-256-GCM Decryption
      │
      ▼
Original File
```

If the cryptographic parameters and authentication data are valid, the original file is successfully recovered.

---

## 5. Unauthorized Decryption

QuantumVault also demonstrates an attacker scenario using **Eve**.

Eve may obtain the encrypted file, but possession of the ciphertext alone does not provide the secret key required for successful decryption.

```text
Encrypted File
      │
      ▼
Eve Attempts Decryption
      │
      ▼
Invalid / Unauthorized Key
      │
      ▼
Key Recovery Fails
      │
      ▼
AES Decryption Fails
      │
      ▼
Access Denied
```

This provides a visual demonstration of receiver-specific cryptographic access control.

---

# User Roles

## Dhruv — Sender

The sender initiates the secure file transfer.

Responsibilities:

* Select a file.
* Select the intended receiver.
* Initiate encryption.
* Transfer the encrypted file.

---

## Rahul — Authorized Receiver

Rahul represents the intended recipient.

Responsibilities:

* Access the received encrypted file.
* Use the appropriate private key.
* Recover the required key material.
* Decrypt and retrieve the original file.

---

## Eve — Unauthorized Attacker

Eve represents an unauthorized party attempting to access the protected information.

Responsibilities:

* Obtain or intercept encrypted data.
* Attempt unauthorized decryption.
* Demonstrate that access cannot be obtained using incorrect key material.

---

# Project Workflow

```text
                   START
                     │
                     ▼
             Select User Role
                     │
             ┌───────┴───────┐
             │               │
             ▼               ▼
          Sender          Receiver
             │               │
             ▼               │
         Select File         │
             │               │
             ▼               │
      Generate AES Key       │
             │               │
             ▼               │
       AES-256-GCM            │
        Encryption            │
             │               │
             ▼               │
       ML-KEM-768             │
      Key Protection         │
             │               │
             ▼               │
      Encrypted Package ─────┘
                             │
                             ▼
                       Key Recovery
                             │
                             ▼
                     AES-GCM Decryption
                             │
                       ┌─────┴─────┐
                       │           │
                     Valid       Invalid
                       │           │
                       ▼           ▼
                 Original File  Access Denied
```

---

# Technology Stack

### Backend

* Python 3
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript

### Cryptography

* AES-256-GCM
* ML-KEM-768
* Python `cryptography`
* Python PQC library used by the implementation

### Development

* Git
* GitHub
* Visual Studio Code
* Python Virtual Environment (`venv`)

---

# Project Structure

```text
QuantumVault/
│
├── app.py
├── README.md
├── requirements.txt
│
├── crypto/
│   ├── aes.py
│   ├── mlkem.py
│   └── hybrid.py
│
├── utils/
│   ├── helpers.py
│   ├── key_generator.py
│   └── key_loader.py
│
├── templates/
│   ├── home.html
│   ├── dhruv.html
│   ├── rahul.html
│   ├── eve.html
│   └── unauthorized.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── uploads/
├── encrypted/
├── decrypted/
├── keys/
│
└── venv/
```

> **Note:** `venv/`, generated encryption keys, uploaded files, decrypted files, and other runtime artifacts should generally be excluded from version control using `.gitignore`.

---

# Installation

## Prerequisites

Make sure the following are installed:

* Python 3
* Git
* pip

---

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd QuantumVault
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Generate Cryptographic Keys

```bash
python -m utils.key_generator
```

This prepares the key material required by the application.

---

# Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will run locally.

Open the displayed local Flask address in a web browser, typically:

```text
http://127.0.0.1:5000
```

---

# Demonstration

QuantumVault can be demonstrated through three simulated roles.

### Sender Demonstration

1. Open the QuantumVault application.
2. Select **Dhruv**.
3. Select a file.
4. Select **Rahul** as the receiver.
5. Initiate **Encrypt & Send**.
6. The file is encrypted using the hybrid cryptographic workflow.

### Receiver Demonstration

1. Open the **Rahul** dashboard.
2. Select the received encrypted file.
3. Initiate decryption.
4. The receiver's key material is used during the recovery process.
5. The original file is restored.

### Attacker Demonstration

1. Open the **Eve** dashboard.
2. Attempt to decrypt the protected file.
3. The attacker does not possess the required receiver key material.
4. The decryption attempt fails.
5. The system displays an unauthorized-access result.

---

# Security Properties Demonstrated

QuantumVault demonstrates several important security concepts.

### Confidentiality

AES-256-GCM protects the contents of the transferred file from unauthorized parties.

### Integrity

AES-GCM authentication allows the system to detect ciphertext modification or invalid authentication data.

### Post-Quantum Key Establishment

ML-KEM-768 introduces a standardized post-quantum cryptographic mechanism into the key-establishment process.

### Key Separation

File contents and key-establishment operations are handled by separate cryptographic mechanisms.

### Receiver-Specific Access

Only the intended receiver is provided with the private key material required by the decryption process.

---

# Threat Model

The demonstration assumes an attacker may obtain access to encrypted transmission data.

For example:

```text
Attacker
   │
   ├── Encrypted File      ✓ Obtainable
   ├── Public Information  ✓ Obtainable
   │
   └── Receiver Private Key ✗ Not Available
```

The attacker therefore cannot simply decrypt the captured ciphertext without the required secret key material.

> QuantumVault is an educational prototype demonstrating cryptographic concepts. It should not be treated as a production-ready secure file-transfer service without additional security engineering, auditing, secure key storage, authentication, transport security, and operational controls.

---

# Why ML-KEM-768?

ML-KEM is a standardized post-quantum **Key Encapsulation Mechanism (KEM)** designed to provide secure key establishment in the presence of quantum-capable adversaries.

QuantumVault uses **ML-KEM-768** as its post-quantum cryptographic component.

The important distinction is:

```text
ML-KEM
   │
   └── Key Establishment
             │
             ▼
          AES Key
             │
             ▼
       AES-256-GCM
             │
             ▼
         File Data
```

ML-KEM is therefore not used as a replacement for AES-based bulk encryption. Instead, the two mechanisms perform different cryptographic roles.

---

# Why AES-256-GCM?

AES-256-GCM is used for the actual file encryption because symmetric encryption is highly efficient for large amounts of data.

GCM additionally provides authentication, meaning the system can detect whether encrypted data has been altered.

This makes AES-256-GCM well suited for the bulk-data encryption layer of a hybrid architecture.

---

# Real-World Relevance

The architecture demonstrated by QuantumVault is relevant to applications where long-term confidentiality and future cryptographic resilience are important, including:

* Government document exchange
* Enterprise file transfer
* Financial information systems
* Healthcare data exchange
* Cloud storage
* Secure messaging
* Critical infrastructure
* Long-term sensitive data protection

---

# Limitations

QuantumVault is primarily an **educational and hackathon prototype**.

The current implementation focuses on demonstrating the cryptographic workflow rather than providing a complete production-grade file-transfer platform.

Potential production requirements would include:

* Secure key storage
* Strong user authentication
* TLS-secured network communication
* Hardware-backed key protection
* Key rotation and revocation
* Secure deletion of temporary files
* Formal cryptographic review
* Comprehensive audit logging
* Database-backed access control
* Secure deployment configuration

---

# Future Enhancements

The project can be extended with:

* **ML-DSA** digital signatures
* User authentication and authorization
* Database integration
* Secure cloud storage
* Multiple-recipient encryption
* Key rotation and revocation
* Digital signatures for sender authentication
* File integrity verification
* Audit logging
* Secure key management
* Email notifications
* Drag-and-drop file upload
* Improved access-control policies
* Production-grade deployment

---

# Screenshots

The following screenshots can be added to document the application workflow:

### Home Page

```text
Add screenshot here
```

### Sender Dashboard

```text
Add screenshot here
```

### Receiver Dashboard

```text
Add screenshot here
```

### Successful Decryption

```text
Add screenshot here
```

### Unauthorized Access

```text
Add screenshot here
```

Once screenshots are available, they can be embedded directly into this section using GitHub Markdown.

---

# Research & Standards

QuantumVault is based on concepts from the following areas:

* NIST Post-Quantum Cryptography Standardization
* ML-KEM / Kyber
* Authenticated Encryption
* AES-GCM
* Hybrid Cryptographic Architectures
* Post-Quantum Cryptography

---

# Project Information

| Category                   | Details                           |
| -------------------------- | --------------------------------- |
| **Project**                | QuantumVault                      |
| **Domain**                 | Post-Quantum Cryptography         |
| **Application**            | Secure File Transfer              |
| **Cryptographic Model**    | Hybrid Encryption                 |
| **Symmetric Encryption**   | AES-256-GCM                       |
| **Post-Quantum Mechanism** | ML-KEM-768                        |
| **Backend**                | Python / Flask                    |
| **Interface**              | HTML / CSS / JavaScript           |
| **Project Type**           | Educational / Hackathon Prototype |

---

# Team

### QuantumVault

**Hackathon Track:** Post-Quantum Cryptography (PQC)

**Project Focus:** Secure file transfer using ML-KEM-768 and AES-256-GCM hybrid encryption.

---

# License

This project was developed for educational and hackathon purposes.

The implementation is intended to demonstrate the principles of post-quantum cryptography and hybrid encryption and should not be considered a production-ready cryptographic system without further security analysis and engineering.

---

## Conclusion

**QuantumVault demonstrates a practical approach to integrating post-quantum cryptography into secure file transfer.**

Rather than replacing symmetric encryption, the project combines the strengths of two cryptographic primitives:

```text
                 QUANTUMVAULT
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
    ML-KEM-768               AES-256-GCM
          │                       │
          │                       │
   Key Establishment         File Encryption
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
              Secure File Transfer
```

The result is a prototype that illustrates how **post-quantum key establishment and efficient symmetric encryption can work together** to build cryptographic systems designed with the future threat of quantum computing in mind.

---

**QuantumVault — Securing Tomorrow's Files Today.**
