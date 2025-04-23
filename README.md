# 🔐 SSL Cipher Strength Checker

This Python script allows users to evaluate the strength of SSL/TLS ciphers by analyzing their names using the [ciphersuite.info](https://ciphersuite.info/) API. It's designed to support quick audits based on output from tools like Nmap SSL scans.

---

## 📌 Features

- ✅ Supports input of multiple cipher names.
- 🧹 Automatically cleans and normalizes cipher names.
- 🔎 Queries cipher strength using [ciphersuite.info](https://ciphersuite.info/).
- 🧠 Understands OpenSSL to IANA naming conversion.
- 📋 Suitable for use with output from tools like `nmap --script ssl-enum-ciphers`.

---

## 🚀 Usage

1. Ensure you have **Python 3** installed.
2. Install the required dependency:

```bash
pip install requests
```

3. Run the script:

```bash
python checkssl.py
```

4. Enter cipher names (one per line). You can copy-paste them from Nmap or any other scan output:

```
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_RSA_WITH_3DES_EDE_CBC_SHA
```

5. Press `Ctrl+D` (or enter an empty line) to finish input.

---

## 🧼 Input Cleaning

The script automatically:
- Strips extra characters like `|` or `(...)` from Nmap output.
- Normalizes names to the IANA style used by ciphersuite.info (e.g., `TLS_RSA_WITH_AES_256_CBC_SHA`).

---

## 📤 Example Output

```
Cipher: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 -> Strength: strong
Cipher: TLS_RSA_WITH_3DES_EDE_CBC_SHA -> Strength: weak
```

---

## 🌐 API Used

- [ciphersuite.info](https://ciphersuite.info/api/) — Public API for SSL/TLS cipher metadata.

---

## 🛠 Developer Notes

- This script is designed for quick interactive use.
- Can be extended to read from a file or parse raw Nmap output automatically.

---
