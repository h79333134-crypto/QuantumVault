# 🔐 QuantumVault
### Securing Tomorrow's Files Today

QuantumVault is a **Post-Quantum Secure File Transfer System** developed to demonstrate how modern cryptographic techniques can protect digital communication against both classical and future quantum computing attacks.

The project implements **Hybrid Encryption**, where files are encrypted using **AES-256-GCM** while the encryption key is securely protected using **ML-KEM-768 (Kyber)**, a NIST-standardized Post-Quantum Key Encapsulation Mechanism (KEM).

Only the intended receiver can successfully decrypt the file, while any intercepted encrypted data remains inaccessible to attackers.

---

# 📌 Table of Contents

- Project Overview
- Problem Statement
- Objectives
- Features
- Technology Stack
- Project Architecture
- Folder Structure
- How the System Works
- Hybrid Encryption Workflow
- Installation
- Running the Project
- Demonstration Workflow
- Security Features
- Future Enhancements
- Screenshots
- Team

---

# 📖 Project Overview

Traditional public-key cryptography such as RSA and ECC is expected to become vulnerable once sufficiently powerful quantum computers become available.

QuantumVault demonstrates how **Post-Quantum Cryptography (PQC)** can be used for secure file transfer by combining:

- AES-256-GCM
- ML-KEM-768 (Kyber)

This hybrid approach provides:

- High-speed encryption
- Quantum-resistant key exchange
- Secure file transmission
- Protection against unauthorized access

---

# ❗ Problem Statement

Current secure communication systems depend heavily on RSA and Elliptic Curve Cryptography.

Large-scale quantum computers will eventually be capable of breaking these algorithms using Shor's Algorithm.

There is therefore a need for secure communication systems that remain secure even in the quantum era.

---

# 🎯 Objectives

The main objectives of QuantumVault are:

- Demonstrate secure file transfer using Post-Quantum Cryptography.
- Encrypt files using AES-256-GCM.
- Protect AES encryption keys using ML-KEM-768.
- Allow only the intended receiver to decrypt files.
- Prevent attackers from recovering encrypted information.
- Provide a simple web interface for demonstration purposes.

---

# ⭐ Features

- Secure File Upload
- AES-256-GCM File Encryption
- ML-KEM-768 Key Encapsulation
- Hybrid Encryption
- Receiver-specific Decryption
- Unauthorized Access Prevention
- Clean Flask Web Interface
- Lightweight Local Storage
- Hackathon Friendly Demonstration

---

# 🛠 Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript

---

## Backend

- Python 3
- Flask

---

## Cryptography

- AES-256-GCM
- ML-KEM-768 (Kyber)
- pqcrypto
- cryptography

---

## Development Tools

- Visual Studio Code
- Git
- Python Virtual Environment (venv)

---

# 📂 Project Structure

```
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

---

# 👨‍💻 System Users

## Dhruv

Acts as the sender.

Responsibilities:

- Uploads files
- Chooses the receiver
- Encrypts the file
- Sends the encrypted file

---

## Rahul

Acts as the authorized receiver.

Responsibilities:

- Receives encrypted files
- Uses private key
- Successfully decrypts files

---

## Eve

Acts as an attacker.

Responsibilities:

- Intercepts encrypted file
- Attempts unauthorized decryption
- Decryption fails

---

# 🔐 Hybrid Encryption Workflow

Instead of encrypting files directly with ML-KEM, QuantumVault uses Hybrid Encryption.

```
Original File

      │

      ▼

AES-256-GCM Encryption

      │

      ▼

Encrypted File (.enc)

      │

      ▼

AES Key Protected using ML-KEM-768

      │

      ▼

Ciphertext + Nonce Stored

      │

      ▼

Receiver Uses ML-KEM Private Key

      │

      ▼

AES Key Recovered

      │

      ▼

Original File Restored
```

---

# ⚙ Working of the Project

## Step 1

The sender uploads a file.

Example:

```
report.pdf
```

---

## Step 2

A random AES-256 key is generated.

---

## Step 3

The uploaded file is encrypted using AES-256-GCM.

Output:

```
report.pdf.enc
```

---

## Step 4

The AES key is securely protected using ML-KEM-768.

Only the intended receiver possesses the corresponding private key capable of recovering the encryption key.

---

## Step 5

The encrypted file, ML-KEM ciphertext and nonce are stored.

---

## Step 6

The receiver downloads the encrypted file.

---

## Step 7

Using the receiver's private key:

- ML-KEM recovers the shared secret (or key material).
- The AES key is derived/recovered.
- AES decrypts the encrypted file.

---

## Step 8

Original file is restored successfully.

---

## Step 9

If Eve attempts decryption:

- Wrong private key
- Shared secret recovery fails
- AES key cannot be obtained
- File cannot be decrypted

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/QuantumVault.git
```

Move into the project directory.

```bash
cd QuantumVault
```

Create virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Generate keys.

```bash
python -m utils.key_generator
```

---

# ▶ Running the Project

Start Flask.

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🎬 Demonstration Workflow

## Home

Choose one of three users.

- Dhruv
- Rahul
- Eve

---

## Sender

Upload file.

Choose Rahul.

Click

```
Encrypt & Send
```

---

## Receiver

Open Rahul Dashboard.

Click

```
Decrypt & Download
```

Original file is successfully recovered.

---

## Attacker

Open Eve Dashboard.

Click

```
Attempt Decryption
```

Output:

```
Unauthorized

Access Denied

Wrong Private Key
```

---

# 🔒 Security Features

- AES-256-GCM authenticated encryption
- ML-KEM-768 Post-Quantum KEM
- Receiver-specific private keys
- Hybrid encryption architecture
- Unauthorized access prevention
- Random nonce generation
- Fresh encryption for every upload

---

# 💡 Why Hybrid Encryption?

ML-KEM is designed to establish a shared secret securely. It is **not intended to encrypt large files directly**.

AES is significantly faster and more efficient for bulk data encryption.

Therefore:

- AES encrypts the file.
- ML-KEM protects the encryption key.

This is the standard architecture adopted in modern secure communication systems.

---

# 🌍 Real-World Applications

- Military communication
- Government document exchange
- Banking systems
- Cloud storage
- Medical records
- Enterprise file sharing
- Quantum-safe VPNs
- Secure messaging

---

# 🚀 Future Enhancements

- User Authentication
- Digital Signatures (ML-DSA)
- Database Integration
- Cloud Storage
- Multiple Recipients
- Email Notifications
- Drag-and-Drop Upload
- File Integrity Verification (SHA-256)
- Secure Key Management
- Audit Logging

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Sender Dashboard
- Receiver Dashboard
- Attacker Dashboard
- Successful Decryption
- Unauthorized Access

---

# 📚 References

- NIST Post-Quantum Cryptography Standardization
- ML-KEM (Kyber) Specification
- Python Cryptography Documentation
- Flask Documentation
- pqcrypto Library Documentation

---

# 👥 Team

Project Name:

**QuantumVault**

Hackathon Track:

**Post-Quantum Cryptography (PQC)**

Prototype:

**Secure File Transfer using ML-KEM (Kyber) Hybrid Encryption**

---

# 📜 License

This project is developed for educational and hackathon demonstration purposes.

---

# ⭐ Conclusion

QuantumVault demonstrates how Hybrid Encryption can be used to build secure, efficient and quantum-resistant file transfer systems.

By combining **AES-256-GCM** with **ML-KEM-768**, the project showcases how sensitive files can be protected against both current and future cryptographic threats while maintaining practical performance and ease of use.