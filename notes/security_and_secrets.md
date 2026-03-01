# 🔐 Handling Secrets Safely (While Backing Up Configurations)

When backing up development environments to GitHub, you must separate:

**configuration** → safe to share  
**credentials (secrets)** → never committed

If a password, token, or private key is pushed to a repository, it should be considered compromised.

---

## What Counts as a Secret?

A secret is anything that allows access to a system without a login prompt.

Common examples:

| Type          | Examples                                |
| ------------- | --------------------------------------- |
| Database      | MySQL, PostgreSQL credentials           |
| APIs          | API tokens, Bearer tokens               |
| Cloud         | AWS keys, Azure keys                    |
| File transfer | SFTP passwords                          |
| Automation    | service accounts, scheduler credentials |

---

## Files You Must NEVER Commit

These files often contain secrets and should always be ignored by Git:

| File               | Why                                        |
| ------------------ | ------------------------------------------ |
| `.env`             | stores environment variables and passwords |
| `.my.cnf`          | MySQL auto-login credentials               |
| `id_rsa`           | SSH private key                            |
| `credentials.json` | Google Cloud / API authentication          |
| `.aws/credentials` | AWS account keys                           |
| `.pypirc`          | Python package publishing credentials      |

Add them to `.gitignore`:
```
.env
.my.cnf
id_rsa
credentials.json
.aws/
```


---

## The Correct Pattern (Very Important)

Never store real credentials in a repo.

Instead use:

**Template files**.

| Real file | Template file     |
| --------- | ----------------- |
| `.env`    | `.env.example`    |
| `.my.cnf` | `.my.cnf.example` |

The template shows required fields but contains fake values.

---

## Example: `.env.example`
```
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
```

Each computer creates its own real `.env`:

```
cp .env.example .env
```


---

## Example: `.my.cnf.example`
```
[client]
user=your_username
password=your_password
host=localhost
database=your_database
[mysql]
pager=less
show-warnings
```

Then locally:
```
cp .my.cnf.example ~/.my.cnf
nano ~/.my.cnf
chmod 600 ~/.my.cnf
```

`chmod 600` ensures only *you* can read the password.

---

## Why This Matters

Git does not forget.

Even if you delete a password later:

• it still exists in commit history  
• it may exist in forks  
• it may exist in local clones  

If a secret is committed → rotate (change) the password immediately.

---

## How to Safely Back Up a Project

Safe to commit:

| OK to Back Up           | Why                          |
| ----------------------- | ---------------------------- |
| `.vscode/settings.json` | editor configuration         |
| `requirements.txt`      | dependency list              |
| `environment.yml`       | conda environment definition |
| `README.md`             | documentation                |
| scripts                 | logic, not credentials       |

Not safe:

| Do NOT Back Up        | Why                 |
| --------------------- | ------------------- |
| `.env`                | passwords           |
| `.my.cnf`             | database login      |
| log files             | may contain tokens  |
| `.ipynb_checkpoints/` | can leak data paths |

---

## Real-World Example You Will Encounter

You may work with:

- vendor data feeds
- SFTP transfers
- scheduled ETL jobs
- API integrations

Those systems often use:
- service account passwords
- SSH keys
- API tokens

These must **never be hardcoded** inside scripts.

Bad:
```python
password = "MyPassword123"
```
Correct:
```
password = os.getenv("DB_PASSWORD")
```
## Quick Checklist Before Every git push

Ask:

Does this file contain a password?

Does it contain a token or key?

Does it auto-login to a system?

Could it access a database?

If yes → add it to .gitignore.
## Why This Is Important for Data Roles

Data jobs frequently connect to:

- databases
- vendors
- internal systems

Security mistakes in these areas are one of the most common real production incidents.

Protecting secrets is part of being trusted with data access.

You are not just backing up files — you are managing access.

---
## Why add example in backup repos ?
This is worth having in your repo because in about 6–12 months you will:
- forget what `.my.cnf` was for
- move to a new machine
- clone your repo
- be *very* glad past-you documented it.

Also — writing documentation like this actually *signals professionalism* if someone ever looks at your GitHub. It shows you understand operational data work, not just coding.