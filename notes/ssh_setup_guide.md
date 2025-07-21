# GitHub SSH Setup Guide 🔐

This guide explains how to generate an SSH key, add it to GitHub, use it with your local repo, and switch a repo from HTTPS to SSH.

---

## 1. Generate a New SSH Key

Open your terminal and run:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept the default file location (~/.ssh/id_ed25519)

You can optionally add a passphrase (for extra security)

This creates:

~/.ssh/id_ed25519 (private key — keep it secret)

~/.ssh/id_ed25519.pub (public key — you’ll share this with GitHub)

## 2. Add Your SSH Key to GitHub

Copy your public key (display the key with cat):

```bash
cat ~/.ssh/id_ed25519.pub
```

Go to: <https://github.com/settings/keys>

Click “New SSH Key”

Paste your key, give it a name like Ubuntu WSL, and click "Add SSH Key"

## 3. Test the SSH Connection

```bash
ssh -T git@github.com
```

If successful, you'll see:

```bash
Hi your-username! You've successfully authenticated...
```

## 4. Change an Existing Repo from HTTPS to SSH

First, check your current remote:

```bash
git remote -v
```

If it shows HTTPS like:

```bash
If it shows HTTPS like:
```bash
https://github.com/your-username/repo-name.git
```

Then change it to SSH:

```bash
git remote set-url origin git@github.com:your-username/repo-name.git
```

confirm:

```bash
git remote -v
```

It should now show:

```bash
git@github.com:your-username/repo-name.git
```

## 5. Push Using SSH

You’re now ready to push and pull using SSH:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

## Notes

Your SSH keys are stored in ~/.ssh/

Never share your private key (id_ed25519)

You can use ssh-add ~/.ssh/id_ed25519 to load the key into your session

If needed, start the agent with:

```bash
eval "$(ssh-agent -s)"
```
