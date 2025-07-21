# Git & GitHub Workflow Guide

A simple, step-by-step guide to using Git and GitHub — from creating a local repo to pushing your code live.

---

## ✅ Prerequisites

- Git installed (`git --version`)
- GitHub account
- SSH key set up and added to GitHub (see `ssh_setup_guide.md`)

---

## 1. 🔨 Create a New Repository (GitHub)

1. Go to [https://github.com/new](https://github.com/new)
2. Enter:
   - **Repository name** (kebab case: lower-case-like-this)
   - Optional: Description
   - Choose **Private** or **Public**
3. Click **Create Repository**

Leave it empty — no README or .gitignore yet (you'll add them locally)

---

## 2. 🖥️ Set Up Local Project

Navigate to your project directory (or create one):

```bash
cd ~/1DataProjects/my-project
```

If Git isn’t already initialized:

```bash
git init
```

## 3. Connect Local to GitHub (via SSH)

```bash
git remote add origin git@github.com:your-username/repo-name.git
```

verify it:

```bash
git remote -v
```

## Track, Commit, and Push

Add and commit your files:

```bash
git add .
git commit -m "Initial commit"
```

Set branch to main (first time only):

```bash
git branch -M main
```

Push to GitHub:

```bash
git push -u origin main
```

## Common Commands

| Task                      | Command                   |
| ------------------------- | ------------------------- |
| See status                | `git status`              |
| See commit history        | `git log --oneline`       |
| Add all changes           | `git add .`               |
| Commit with message       | `git commit -m "Message"` |
| Push to GitHub            | `git push`                |
| Pull updates from GitHub  | `git pull`                |
| See configured remote URL | `git remote -v`           |
| Rename current branch     | `git branch -M main`      |

## Tips

Git only tracks files once you git add them.

.gitignore helps prevent committing unnecessary files like .env, **pycache**/, etc.

Your Git remote setting persists — you don’t have to re-add it every time.

You can check Git settings with cat .git/config inside the repo.

## Optional Cleanup

To remove a remote:

```bash
git remote remove origin
```

To reset a repo (CAUTION!):

```bash
rm -rf .git
git init
```

## GitHub CLI vs git

## git - Core Git Version Control Tool

- Comes from git-scm
- Manages your local repository and source control
- Works with any Git repository — not just GitHub

| Command                   | Description                      |
| ------------------------- | -------------------------------- |
| `git init`                | Initialize a new Git repo        |
| `git add`, `git commit`   | Track and save changes           |
| `git push`, `git pull`    | Sync with a remote (like GitHub) |
| `git log`, `git status`   | View history and repo status     |
| `git branch`, `git merge` | Branching and merging            |

## gh- GitHub CLI Tool

- Comes from cli.github.com
- Specifically built for interacting with GitHub features
- Wraps around Git and adds GitHub-native functionality

| Command          | Description                                   |
| ---------------- | --------------------------------------------- |
| `gh repo create` | Create a new GitHub repository                |
| `gh repo clone`  | Clone a GitHub repo (like `git clone`)        |
| `gh pr create`   | Create a pull request                         |
| `gh issue list`  | View issues on a GitHub repo                  |
| `gh auth login`  | Authenticate with GitHub (via browser or SSH) |
| `gh gist create` | Create a GitHub Gist                          |
| `gh auth status` | Check login status

## Bonus

You can use both together:

- Use git to manage your code
- Use gh to create a repo or pull request without touching the GitHub web UI

## Create a GitHub Repo with gh

From inside your local project folder:

```bash
gh repo create
```

You'll be prompted:

```bash
? Repository name: analysis-legos-colors
? Description: An exploratory analysis of Lego color data
? Visibility: (Use arrow keys)
❯ Public
  Private
? Would you like to add a remote? Yes
? Which remote name should be used? origin
```

Then it automatically:

- Creates the GitHub repo
- Adds it as your Git remote (origin)
- Optionally pushes your code
