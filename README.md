# Python Ethereum Networks Automation Demo 🚀

## Introduction 📖

Welcome to the Python Ethereum Networks Automation Demo repository! This resource is designed to showcase how you can interact with Ethereum smart contracts using the `web3.js` package. Whether you're a developer, student, or blockchain enthusiast, this demo will provide you with a practical understanding of smart contract interactions.

**Please note:** This repository is intended for educational purposes and is not suited for production use.

## Table of Contents 📚

- [Python Ethereum Networks Automation Demo 🚀](#python-ethereum-networks-automation-demo-)
  - [Introduction 📖](#introduction-)
  - [Table of Contents 📚](#table-of-contents-)
  - [Setup Instructions 🛠️](#setup-instructions-️)
  - [License 📄](#license-)

## Setup Instructions 🛠️

To get started with this demo, follow these steps to set up your environment:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kingsmai/py-eth-automation.git
   cd py-eth-automation
   ```

2. **Create and Activate Virtual Environment**
   Create a virtual environment to manage your project's dependencies.
   ```bash
   virtualenv venv
   source ./venv/bin/activate
   ```
   Remember to activate the virtual environment every time you start a new terminal session.

3. **Install Dependencies**
   Install the necessary Python packages using the provided `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Rewrite Configuration Files**
   Duplicate `config.json.dist` by using this command.
   ```bash
   cp config.json{dist,}
   ```
   Then edit the content to match with your situations. The content of `config.json` Shown as below
   | Last Edited: 11 Apr 16:30
   ```json
   {
        "RPC_LIST_HTTPS": [
            "The list of RPC List, can be founded from chainlist.org"
        ],
        "SEPOLIA_RPC_LIST_HTTPS": [
            "The list of Sepolia RPC List"
        ],
        "RPC_LIST_WSS": [
            "The list of Web socket Sepolia RPC List, haven't use yet."
        ],
        "SEPOLIA_RPC_LIST_WSS": [
            "The list of Web socket RPC List, haven't use yet."
        ],
        "ACCOUNT_LIST_PRIVATE_KEY": [
            "Your account private key"
        ]
    }
   ```
   <mark>BEWARE: Don't commit your account private key or you will make your crypto account in risk!</mark>

<!-- 
## Getting Started 🌟

[Instructions on how to use the demo, execute scripts, etc.]

## Contributing 🤝

[Guidelines for contributing to the repository]
-->

## License 📄

Please refer to the `LICENSE` document
