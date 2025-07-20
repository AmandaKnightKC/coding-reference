## 🧾 Summary: WSL Project Setup and Environment Cleanup

### 📁 1. Moving Project to WSL File System

Reason: VS Code warns about performance when working in /mnt/c/... (Windows file system).

Target Location: Moved to /home/cleavertbt/1DataProjects/HealthcareProject.

Command Used:

cp -r /mnt/c/Users/Amanda/Documents/1DataProjects/HealthcareProject ~/1DataProjects/

### 🔍 2. Navigating and Accessing Files

Confirmed project location using:

cd ~/1DataProjects/HealthcareProject
ls

Opened in VS Code with:

code .

### 📂 3. Accessing WSL Files from Windows

Path: \wsl$\Ubuntu\home\cleavertbt\1DataProjects\HealthcareProject

Opened via Windows File Explorer.

### 🖥️ 4. Bash Configuration Fix

Issue: .bashrc had a syntax error due to a missing newline:

__mamba_setup="$(...)"if [ $? -eq 0 ]; then

Fix:

__mamba_setup="$(...)"
if [ $? -eq 0 ]; then

Cleaned up duplicate alias lines:

alias dataproj='cd ~/1DataProjects'

Saved with nano, then reloaded:

source ~/.bashrc

### 🧠 7. Commenting Multiple Lines

Shortcut: Ctrl + / (Windows) or Cmd + / (Mac) in VS Code and Jupyter.

Manual: Add # at the start of each line.