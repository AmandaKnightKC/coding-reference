# 🐧 Linux Command Cheat Sheet (Linus/WSL Environment)

## 📝 Customized

Custom alias = projects in terminal to instantly take you to /home/cleavertbt/1DataProjects

Recorded in the .bashrc file

```bash
alias projects='cd ~/1DataProjects'
```

After editing `.bashrc`:

``` bash
source ~/.bashrc
```

(reloads settings without restarting terminal)

## Navigation Aliases

| Alias      | Expands To                               | What It Does                               |
| ---------- | ---------------------------------------- | ------------------------------------------ |
| `projects` | `cd ~/1DataProjects`                     | Goes to my main workspace directory        |
| `vsc`      | `cd ~/1DataProjects/vscode-config`       | Opens my VS Code backup/config respository |
| `bike`     | `cd ~/1DataProjects/bike-share-analysis` | Opens the bike-share analysis project      |
| `lead`     | `cd ~/1DataProjects/lead-scoring-mysql`  | Opens the lead-scoring database project    |
| `ref`      | `cd ~/1DataProjects/coding-reference`    | Opens my notes and reference repo          |

## File & Listing Helper Aliases

| Alias | Expands To   | What It Does                                                                         |
| ----- | ------------ | ------------------------------------------------------------------------------------ |
| `ll`  | `ls -alF`    | Full detailed directory listing (permissions, size, owner, hidden files, file types) |
| `la`  | `ls -A`      | Shows hidden files (like `.env`, `.git`, `.vscode`) without `.` and `..`             |
| `l`   | `ls -CF`     | Quick compact view of folder contents with file-type markers                         |
| `rm`  | `rm -i`      | Asks for confirmation before deleting files (safety guard)                           |
| cp    | 'cp-i'       | Asks for confirmation before copying files                                           |
| mv    | 'mv -i'      | Asks for confirmation before moving files                                            |
| \     | escape alias | Use \ to bypass alias. Example: \rm -r old_backups/                                  |

## Python Helper Aliases

| Alias      | Expands To       | What It Does                                                  |
| ---------- | ---------------- | ------------------------------------------------------------- |
| `py`       | `python3`        | Runs Python explicitly using system Python 3                  |
| `activate` | `conda activate` | Activates a conda environment without typing the full command |

## 🧭 Standard Basic Navigation

| Command      | Description                     |
| ------------ | ------------------------------- |
| `pwd`        | Show current directory          |
| `ls`         | List files in current directory |
| `ls -l`      | Long listing with sizes/dates   |
| `cd folder/` | Change into a directory         |
| `cd ..`      | Go up one level                 |
| `cd ~`       | Go to home directory            |
| `clear`      | Clear the terminal screen       |

---

## 📁 File and Directory Management

| Command                | Description                  |
| ---------------------- | ---------------------------- |
| `mkdir newfolder`      | Create a new folder          |
| `touch file.py`        | Create a new empty file      |
| `cp file1.py file2.py` | Copy a file                  |
| `mv old.py new.py`     | Rename or move a file        |
| `rm file.py`           | Delete a file                |
| `rm -r folder/`        | Delete folder and contents ⚠️ |

---
*Copy* recursively (including all subfolders/files)

```bash
cp -r /mnt/c/Users/Amanda/Documents/1DataProjects/HealthcareProject ~/1DataProjects/
```

Move one project into the current working directory

```bash
mv /mnt/c/Users/Amanda/Documents/1DataProjects/HealthcareProject ~/1DataProjects/
```

moves everything, -n skips files/folders that already exist in the target, * all contents

```bash
mv -n /mnt/c/Users/Amanda/Documents/1DataProjects/* ~/1DataProjects/

```

## 📝 Viewing Files

| Command               | Description                |
| --------------------- | -------------------------- |
| `cat file.txt`        | Show file content          |
| `less file.txt`       | Scroll through a long file |
| `head -n 10 file.txt` | Show first 10 lines        |
| `tail -n 10 file.txt` | Show last 10 lines         |
| `wc -l file.txt`      | Count number of lines      |

---

## 🔎 Searching

| Command                           | Description                                                      |
| --------------------------------- | ---------------------------------------------------------------- |
| `grep "word" file.txt`            | Find lines containing “word”                                     |
| `find . -name "*.py"`             | Find all Python files                                            |
| `history`                         | View command history                                             |
| `Ctrl + R`                        | Reverse search through history                                   |
| `ls data/raw_csv \| sort`         | list files alphabetically                                        |
| `ls data/raw_zips \| grep 202501` | lists all files with search term '202501' located in that folder |
| `find . -name "*keyword*"`        | find anything in the current dir that has the keyword. ex: *md   |
---
## 🔄 Pipes & Output Redirection

| Symbol | Example                          | What It Does                                                  |
| ------ | -------------------------------- | ------------------------------------------------------------- |
| `\|`   | `ls data/raw_csv \| sort`        | Sends output of one command into another command (processing) |
| `>`    | `ls data/raw_csv > files.txt`    | Writes command output to a file (overwrites existing file)    |
| `>>`   | `ls data/raw_csv >> files.txt`   | Appends output to the end of a file                           |
| `2>`   | `python script.py 2> errors.txt` | Saves error messages to a file instead of the screen          |
| `&>`   | `python script.py &> log.txt`    | Saves both normal output and errors to a file                 |

**Key idea:**  
Linux commands produce output.  
You can either:
- view it (screen)
- process it (pipe `|`)
- save it (redirection `>`)

Example mini-pipeline:

`ls data/raw_csv | sort > sorted_files.txt`

---

## 🐍 Python & Conda

| Command                              | Description                                          |
| ------------------------------------ | ---------------------------------------------------- |
| `conda activate env_name`            | Activate Conda environment                           |
| `conda deactivate`                   | Leave current environment                            |
| `python`                             | Launch Python REPL                                   |
| `ipython`                            | Launch enhanced Python shell                         |
| `jupyter notebook` or `jupyter lab`  | Launch Jupyter interface                             |
| `conda env list`                     | lists all available environments                     |
| `conda list`                         | lists all packages in that envir                     |
| `conda create --name give-it-a-name` | creates environment                                  |
| `conda install packagename`          | installs listed packages into activated env          |
| `code .`                             | in activated environment, use to bind env to project |

---
## 📄 Hidden Files (Dotfiles)

Files beginning with `.` are hidden:

    .env
    .git
    .gitignore
    .vscode
    .bashrc

Show them:

    ls -A

Difference:

 | Command               | Shows                            |
 | --------------------- | -------------------------------- |
 | `ls` or alias `l`     | normal files                     |
 | `ls -a`               | all files including `.` and `..` |
 | `ls -A` or alias `la` | hidden files except `.` and `..` |
---
------------------------------------------------------------------------

## 📊 Useful `ls` Options

 | Command                | Meaning          |
 | ---------------------- | ---------------- |
 | `ls -l`                | detailed listing |
 | `ls -a`                | show hidden      |
 | `ls -A` or alias `la`  | hidden (cleaner) |
 | `ls -F`                | show file type   |
 | `ls -alF`or alias `ll` | full inspection  |
 |                        |


File type markers:

 | Symbol | Meaning           |
 | ------ | ----------------- |
 | `/`    | directory         |
 | `*`    | executable script |
 | `@`    | symbolic link     |

------------------------------------------------------------------------
------------------------------------------------------------------------

## 🔐 File Permissions

Example:

    -rwxr-xr-x

Directory:

    drwxr-xr-x

Three groups:

 | Section | Who                    |
 | ------- | ---------------------- |
 | 1       | Owner (you)            |
 | 2       | Group                  |
 | 3       | Others (everyone else) |

Permission letters:

 | Letter | Meaning |
 | ------ | ------- |
 | r      | read    |
 | w      | write   |
 | x      | execute |

------------------------------------------------------------------------

## ⚙️ System Info & Utilities

| Command            | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| `top`              | Running processes overview                                 |
| `htop`             | Better process viewer (install)                            |
| `df -h`            | Disk space usage                                           |
| `du -sh folder/`   | Get folder size                                            |
| `uname -a`         | System info                                                |
| `whoami`           | Your current username                                      |
| `source ~/.bashrc` | Reloads .bashrc (controls how terminal behaves) after edit |
| `.~/.bashrc`       | Same thing as above                                        |

---

## 💡 Tips

- Use **Tab** for autocomplete (GREAT learning tool)
- Use **↑ / ↓** to cycle through previous commands
- Add `--help` to any command for usage info:  
  e.g., `ls --help`
- Chain commands:  
  `cd project && ls && python script.py`
------------------------------------------------------------------------

## ▶️ Making Scripts Executable

A script becomes runnable in **two steps**:

### 1. Add shebang (first line)

``` bash
#!/usr/bin/env bash
```

Tells Linux **which interpreter** should run the file.

### 2. Give execute permission

``` bash
chmod +x script.sh
```

Then run:

``` bash
./script.sh
```

------------------------------------------------------------------------

## 🤯 Why `./script.sh` is needed

Linux does **not search the current directory** for security reasons.

So:

 | Command       | Meaning                |
 | ------------- | ---------------------- |
 | `script.sh`   | search system programs |
 | `./script.sh` | run this file here     |
------------------------------------------------------------------------

## 🧠 Important Concepts Learned

• A script is just a text file until it has: - a shebang - execute
permission

• `rm` deletes a *name*, not immediately the disk data.

• Dotfiles control how programs behave.

• `.bashrc` is your terminal's startup configuration.

• The terminal is an interface to the filesystem and process system ---
not just a command list.

------------------------------------------------------------------------
------------------------------------------------------------------------

## ⌨️ Tab Completion

Tab completion suggests: - folders - git commands - branches - filenames

Press:

| Keys      | Result        |
| --------- | ------------- |
| `TAB`     | auto-complete |
| `TAB TAB` | show choices  |

Example:

    git che<TAB><TAB>
    checkout  cherry  cherry-pick

### Enable (if missing)

    sudo apt install bash-completion

Add to `.bashrc`:

``` bash
if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
fi
```

------------------------------------------------------------------------

## 🌳 `tree` Command Summary

| Command                      | Description                            | Example Output                         |
| ---------------------------- | -------------------------------------- | -------------------------------------- |
| `tree`                       | Shows full directory tree (all levels) | Lists all files/folders recursively    |
| `tree -L 2`                  | Limits depth to 2 levels               | Folders and files up to 2 levels deep  |
| `tree -d`                    | Show directories only                  | Hides individual files                 |
| `tree -a`                    | Includes hidden files (e.g., `.git`)   | Shows dotfiles                         |
| `tree > file.txt`            | Save output to a file                  | Creates a flat `.txt` copy of the tree |
| `tree -L 2 -I '__pycache__'` | Ignores specific files/folders         | Useful for excluding clutter           |

> 💡 Tip: Install with `sudo apt install tree` if it’s not already available in WSL.
>
------------------------------------------------------------------------

## 💾 Backing Up Your Environment

Backup your terminal setup in a private Configuration Repos:

    cp ~/.bashrc ~/1DataProjects/vscode-config/bashrc

Commit to GitHub:

    git add bashrc
    git commit -m "Update bashrc"
    git push

Restore on a new machine:

    cp bashrc ~/.bashrc
    source ~/.bashrc

------------------------------------------------------------------------
