## ✅ What Is a .env File?
A .env (environment) file is used to store configuration variables like database credentials, API keys, or secret tokens outside of your source code.

| Benefit                  | Why It Matters                             |
| ------------------------ | ------------------------------------------ |
| **Security**             | Keeps sensitive info out of your codebase  |
| **Separation of config** | Environment settings can differ per device |
| **Reusability**          | Works across dev/staging/production        |
| **Simplicity**           | Easy to load into Python, Node, etc.       |

### 1. Create the .env File
In the root folder of your project:
```bash
touch .env
```
### 2. Add Key-Value Pairs
Use the KEY=value format:
```
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=amanda
MYSQL_PASSWORD=your_secure_password
MYSQL_DB=my_database
```
❗ No quotes around values unless the value has spaces
❗ Do not include this file in GitHub. Add it to .gitignore

### 3. Load .env File in Python
Install python-dotenv
load in script
```python
from dotenv import load_dotenv
import os

load_dotenv()  # looks for a .env file in the current directory

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
db = os.getenv("MYSQL_DB")
```
### 🧪 Best Practices
| Tip                                   | Why It Helps                                                            |
| ------------------------------------- | ----------------------------------------------------------------------- |
| Use `.env.example`                    | Share default structure with collaborators (but leave out real secrets) |
| Use `.gitignore`                      | Prevent leaking secrets in GitHub                                       |
| Keep it at project root               | So it’s easily discoverable by tools like `dotenv` or `docker-compose`  |
| Use environment-specific `.env` files | Like `.env.dev`, `.env.prod` (but manage loading them yourself)         |

###  Example Project Structure
```
my_project/
├── .env
├── app.py
├── requirements.txt
├── db/
│   └── schema.sql
```
### 🐍 Python + MySQL + .env Example
#### Install Required Packages
```
conda install python-dotenv mysql-connector-python
```
### ✅ Python Script: connect_mysql.py
```python
import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read variables from environment
db_config = {
    "host":     os.getenv("MYSQL_HOST"),
    "port":     int(os.getenv("MYSQL_PORT", 3306)),
    "user":     os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DB")
}

try:
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Sample query
    cursor.execute("SELECT DATABASE();")
    db = cursor.fetchone()
    print(f"Connected to database: {db[0]}")

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
```
