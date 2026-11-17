# OTP for Printouts 🔐

## Project Overview
OTP for Printouts is a web-based application designed to make document printing more secure and convenient. It allows customers to upload documents and retrieve them at a printing shop using a unique six-digit One-Time Password (OTP).

## Problem Statement
Customers often need to share personal documents with printing shops. This can create privacy and security concerns. This project aims to reduce unnecessary exposure of customer documents through OTP-based access.

## Key Features
- Secure document uploading.
- Automatic six-digit OTP generation.
- OTP-based document retrieval.
- Validation of correct and incorrect OTPs.
- Document downloading for printing.
- Local file deletion after printing confirmation.
- Server-side file deletion.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- Requests

## System Workflow
1. Customer opens the website.
2. Customer uploads a document.
3. The system generates a unique six-digit OTP.
4. Customer shares the OTP with the shopkeeper.
5. Shopkeeper enters the OTP in the shopkeeper application.
6. The document is downloaded and opened for printing.
7. After printing, the shopkeeper confirms completion.
8. The downloaded local file and server copy are deleted.

## Project Links
- **Live Website:** https://otp-for-prints.onrender.com
- **GitHub Repository:** https://github.com/rutvikhirid-glitch/otp-for-prints

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/rutvikhirid-glitch/otp-for-prints.git
cd otp-for-prints
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask application
```bash
python app.py
```

### 4. Run the Shopkeeper Application
On the shopkeeper's Windows computer, run:
```bash
python shopkeeper.py
```

The shopkeeper application requires Python and the Requests package.

## Future Scope
- Automatic detection of print completion.
- Improved document security.
- Automatic cleanup of expired documents.
- Improved shopkeeper interface.

## Conclusion
OTP for Printouts provides a simple approach to privacy-conscious document printing through OTP-based document retrieval and file deletion after printing confirmation.
