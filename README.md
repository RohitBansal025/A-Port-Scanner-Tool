# A Port Scanner Tool using Python

A simple and efficient port scanner written in Python. This tool scans a target IP address for open ports and lists them, prioritizing common ports before scanning the rest.

## Description

Port Scanner is a tool designed to help you quickly identify open ports on a target machine or site. It scans the most common ports first, providing immediate feedback on the most likely points of entry. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Installation
**Note**: Ensure you have the GitHub CLI installed and authenticated. You can follow the instructions [here](https://cli.github.com/manual/installation) to set it up.



1. **Clone the repository**:
   ```bash
    gh repo clone RohitBansal025/A-Port-Scanner-Tool

2. **Navigate to the project diretory**:
     cd A-Port-Scanner-Tool

3. **Ensure you have Python 3 installed. You can check by running**:
     python3 --version

## Usage:

1.  **Open you Terminal**
2.  **Run the script with the target domain name or IP address as an argument**:
        python3 scanner.py <target_ip or target website>
        for example: python3 Scanner.py 192.168.1.1
                               or like
                     python3 Scanner.py google.com
4.  **During the scan, you will be prompted to enter the range of ports you want to scan:**
        Enter start port for full scan: <1000>
        Enter end port for full scan: <2000>
## Features
    Scans common ports first for quicker results.
    Allows specifying a custom range of ports for comprehensive scanning.
    Provides clear output and handles errors gracefully.
## License
    This project is licensed under the MIT License - see the [LICENSE] file for details.
        MIT License

    Copyright (c) 2024 RohitBansal025

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
