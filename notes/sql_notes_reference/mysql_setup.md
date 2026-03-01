## Setting Up MySQL in Ubuntu (WSL) for VS Code

#### 1. Install MySQL in Ubuntu (WSL)
```bash
sudo apt update
sudo apt install mysql-server
```
#### 2. Start the MySQL Service

* To enable on boot (optional):

```bash
sudo service mysql start
```
* To enable MySQL on boot:
```bash
sudo systemctl enable mysql
```

#### 3. Secure the Installation
```bash
sudo mysql_secure_installation
```
Running sudo mysql_secure_installation is a post-install security script that helps harden your MySQL setup. It guides you through several important steps to reduce vulnerabilities.  You’ll be asked to set a root password, remove anonymous users, disallow root login remotely, etc.

####  ✅ What mysql_secure_installation Does
Here's what it typically walks you through:

| Step                                          | Purpose                                                          |
| --------------------------------------------- | ---------------------------------------------------------------- |
| **1. Set root password** (if not already set) | Prevents unauthorized access to the root account                 |
| **2. Remove anonymous users**                 | Blocks unknown users from connecting without credentials         |
| **3. Disallow root login remotely**           | Reduces the risk of external root-level attacks                  |
| **4. Remove test database**                   | Deletes a default, insecure test database that anyone can access |
| **5. Reload privilege tables**                | Applies all the changes immediately                              |



#### 4. Log in to MySQL
```bash
sudo mysql -u root -p
```

#### 5. (Optional) Create a Non-Root User
```sql
CREATE USER 'amanda'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'amanda'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

## ✅ Using MySQL in VS Code
1. Install VS Code Extension
Install MySQL or SQLTools extension from the VS Code marketplace.

2. Connect to the MySQL Server
Use:
```
Host: 127.0.0.1

Port: 3306

Username: root or amanda

Password: Your chosen password

Database: (optional or use default mysql to test)
```

### If you're using WSL:

Open VS Code in WSL:

```bash
code .
```

The MySQL service must be running inside the WSL terminal when you try to connect from VS Code (even from extensions like SQLTools).
``` bash
sudo service mysql start
```
verify it's running (optional)  
```bash
sudo service mysql status
```

✅ Troubleshooting Tips
If MySQL won’t start:
- sudo: Run as superuser (necessary to view full logs)

- journalctl: Command-line tool to view logs from the systemd journal

- -x: Show explanations for errors, when available

- -e: Jump to the end of the log (most recent events)
```bash
sudo service mysql status
sudo journalctl -xe
```

If mysql command not found:

```bash
sudo apt install mysql-client
```

## Steps to Make CMS_WSL Appear in MySQL Connections

### 🐧 Inside WSL (Ubuntu)
1. Started the MySQL service
```
sudo service mysql start
```
2. Logged into MySQL as root
```
sudo mysql -u root -p
```
3. Created the database
Inside the MySQL prompt
```sql
CREATE DATABASE CMS_WSL;
```
4. Create a user and granted privileges
```sql
CREATE USER 'amanda'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON CMS_WSL.* TO 'amanda'@'localhost';
FLUSH PRIVILEGES;
```
### 🖥️ In VS Code or SQL Client (e.g., SQLTools, MySQL Workbench)
5. Installed a MySQL extension

* Example: SQLTools + MySQL Driver
6. Created a new connection in the extension UI
```
Name: CMS_WSL (or whatever label you chose)
Host: 127.0.0.1
Port: 3306
User: amanda (or root)
Password: your_password
Default Database: CMS_WSL
```
