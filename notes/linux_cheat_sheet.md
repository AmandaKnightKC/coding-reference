# 🐧 Linux Command Cheat Sheet (WSL + Data Science Focus)

## 📝 Customized

Custom alias = dataproj in terminal to instantly take you to /home/cleavertbt/1DataProjects

Recorded in the .bashrc file

```bash
alias dataproj='cd ~/1DataProjects'

dataproj
```

## 🧭 Basic Navigation

| Command         | Description                          |
|----------------|--------------------------------------|
| `pwd`           | Show current directory               |
| `ls`            | List files in current directory      |
| `ls -l`         | Long listing with sizes/dates        |
| `cd folder/`    | Change into a directory              |
| `cd ..`         | Go up one level                      |
| `cd ~`          | Go to home directory                 |
| `clear`         | Clear the terminal screen            |

---

## 📁 File and Directory Management

| Command                  | Description                     |
|--------------------------|---------------------------------|
| `mkdir newfolder`        | Create a new folder             |
| `touch file.py`          | Create a new empty file         |
| `cp file1.py file2.py`   | Copy a file                     |
| `mv old.py new.py`       | Rename or move a file           |
| `rm file.py`             | Delete a file                   |
| `rm -r folder/`          | Delete folder and contents ⚠️   |

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

| Command                  | Description                     |
|--------------------------|---------------------------------|
| `cat file.txt`           | Show file content               |
| `less file.txt`          | Scroll through a long file      |
| `head -n 10 file.txt`    | Show first 10 lines             |
| `tail -n 10 file.txt`    | Show last 10 lines              |
| `wc -l file.txt`         | Count number of lines           |

---

## 🔎 Searching

| Command                              | Description                          |
|--------------------------------------|--------------------------------------|
| `grep "word" file.txt`               | Find lines containing “word”         |
| `find . -name "*.py"`                | Find all Python files                |
| `history`                            | View command history                 |
| `Ctrl + R`                           | Reverse search through history       |

---

## 🐍 Python & Conda

| Command                                 | Description                       |
|-----------------------------------------|-----------------------------------|
| `conda activate env_name`               | Activate Conda environment        |
| `conda deactivate`                      | Leave current environment         |
| `python`                                | Launch Python REPL                |
| `ipython`                               | Launch enhanced Python shell      |
| `jupyter notebook` or `jupyter lab`     | Launch Jupyter interface          |

---

## ⚙️ System Info & Utilities

| Command            | Description                        |
|--------------------|------------------------------------|
| `top`              | Running processes overview         |
| `htop`             | Better process viewer (install)    |
| `df -h`            | Disk space usage                   |
| `du -sh folder/`   | Get folder size                    |
| `uname -a`         | System info                        |
| `whoami`           | Your current username              |
| `source ~/.bashrc`  | Reloads a file after edit |
| `.~/.bashrc`        | Same thing as above                |

---

## 💡 Tips

- Use **Tab** for autocomplete
- Use **↑ / ↓** to cycle through previous commands
- Add `--help` to any command for usage info:  
  e.g., `ls --help`
- Chain commands:  
  `cd project && ls && python script.py`

## 🌳 `tree` Command Summary

| Command | Description | Example Output |
|---------|-------------|----------------|
| `tree` | Shows full directory tree (all levels) | Lists all files/folders recursively |
| `tree -L 2` | Limits depth to 2 levels | Folders and files up to 2 levels deep |
| `tree -d` | Show directories only | Hides individual files |
| `tree -a` | Includes hidden files (e.g., `.git`) | Shows dotfiles |
| `tree > file.txt` | Save output to a file | Creates a flat `.txt` copy of the tree |
| `tree -L 2 \| sed "1s\|.\|$(basename $PWD)\|"` | Replaces the `.` with folder name at top | Makes the structure name more readable |
| `tree -L 2 -I '__pycache__'` | Ignores specific files/folders | Useful for excluding clutter |

> 💡 Tip: Install with `sudo apt install tree` if it’s not already available in WSL.

``` tree -L 2 | sed "1s|\.|$(basename $PWD)|" > structure.txt ```

Breakdown:

- tree -L 2 generates your directory structure

- sed "1s|\.|$(basename $PWD)|":

- 1s: means “substitute on line 1 only”

- | is used as a delimiter instead of /

- . matches the dot at the top of the tree output

- $(basename $PWD) gets your current folder name

## 🛠️ sed stands for stream editor — it’s a Unix/Linux command-line tool used to

Search, find and replace, insert, or delete text

Process and transform text in files or input streams

It’s especially handy for making quick, automated edits without opening a text editor.

| Command                                    | What It Does                                             |             |     |                                                      |
| ------------------------------------------ | -------------------------------------------------------- | ----------- | --- | ---------------------------------------------------- |
| `sed 's/old/new/' file.txt`                | Replaces first instance of `old` with `new` in each line |             |     |                                                      |
| `sed 's/old/new/g' file.txt`               | Replaces **all** instances of `old` with `new` per line  |             |     |                                                      |
| `echo "hello world" \| sed 's/world/WSL/'` | Outputs: `hello WSL`                                     |             |     |                                                      |
| `sed -n '5,10p' file.txt`                  | Prints lines 5 through 10                                |             |     |                                                      |
| \`sed '1s                                  | .                                                        | ProjectName | '\` | Replaces the **first line’s** `.` with `ProjectName` |
