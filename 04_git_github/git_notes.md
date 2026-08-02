# Git & GitHub Complete Guide

A beginner-friendly guide to Git and GitHub covering installation, configuration, commonly used commands, branching, merging, and daily workflow.

---

# Git vs GitHub

| Git | GitHub |
|------|---------|
| Git is a distributed Version Control System (VCS). | GitHub is a cloud platform that hosts Git repositories. |
| Tracks source code changes locally. | Stores repositories online. |
| Works without an internet connection. | Internet connection is required for remote operations. |
| Developed by Linus Torvalds (2005). | Owned by Microsoft (since 2018). |
| Installed on your local machine. | Accessed through a web browser or Git clients. |
| Manages versions and history. | Provides collaboration, pull requests, issues, and CI/CD. |

### Git Workflow with GitHub

```
Developer
     │
     ▼
 Local Repository (Git)
     │
 git push
     ▼
 GitHub Repository
     ▲
 git pull
     │
Other Developers
```

---

# What is Git?

Git is a Distributed Version Control System (DVCS) used to track changes in source code during software development.

### Features

- Distributed Version Control
- Fast and Lightweight
- Branching & Merging
- Tracks Complete History
- Supports Team Collaboration
- Open Source

---

# What is GitHub?

GitHub is a cloud-based platform used to host Git repositories.

### Features

- Repository Hosting
- Collaboration
- Pull Requests
- Issues
- GitHub Actions
- Project Management
- Release Management

---

# Git Architecture

```
Working Directory
        │
        ▼
 Staging Area
        │
        ▼
 Local Repository
        │
        ▼
 Remote Repository (GitHub)
```

---

# Install Git

Download Git:

https://git-scm.com/downloads

Verify installation:

```bash
git --version
```

---

# Git Configuration

Set username

```bash
git config --global user.name "Your Name"
```

Set email

```bash
git config --global user.email "your@email.com"
```

Check configuration

```bash
git config --list
```

---

# Initialize Repository

Create a Git repository.

```bash
git init
```

Check status

```bash
git status
```

---

# Staging Files

Stage a specific file

```bash
git add README.md
```

Stage all files

```bash
git add .
```

---

# Commit Changes

Create a commit

```bash
git commit -m "Initial Commit"
```

Example

```bash
git commit -m "Added Login Module"
```

---

# Repository Status

Check repository status

```bash
git status
```

Possible states

- Untracked
- Modified
- Staged
- Committed

---

# View Changes

View unstaged changes

```bash
git diff
```

View staged changes

```bash
git diff --staged
```

---

# Commit History

View complete history

```bash
git log
```

View last 3 commits

```bash
git log -p -3
```

Compact log

```bash
git log --oneline
```

---

# Restore Changes

Discard local changes

```bash
git restore README.md
```

Restore all changes

```bash
git restore .
```

---

# Unstage Files

Remove staged file

```bash
git restore --staged README.md
```

Alternative

```bash
git reset README.md
```

---

# Connect GitHub Repository

Add remote

```bash
git remote add origin https://github.com/username/repository.git
```

Verify remote

```bash
git remote -v
```

---

# Push Code to GitHub

Push first time

```bash
git push -u origin main
```

Push later

```bash
git push
```

---

# Clone Repository

Clone existing repository

```bash
git clone https://github.com/username/repository.git
```

---

# Pull Latest Changes

Download and merge changes

```bash
git pull
```

Download only

```bash
git fetch
```

---

# Branching

Create branch

```bash
git branch developer
```

List branches

```bash
git branch
```

Rename branch

```bash
git branch -M main
```

Delete branch

```bash
git branch -d developer
```

---

# Switch Branch

Switch to another branch

```bash
git checkout developer
```

Create and switch

```bash
git checkout -b feature-login
```

Using switch command

```bash
git switch developer
```

---

# Merge Branch

Merge developer into main

```bash
git checkout main
git merge developer
```

---

# Merge Conflict

Pull latest changes

```bash
git pull
```

Resolve conflicts manually.

Then execute

```bash
git add .
git commit -m "Resolved merge conflict"
git push origin main
```

---

# Remove Repository Remote

Remove remote

```bash
git remote remove origin
```

---

# Rename Remote

```bash
git remote rename origin github
```

---

# Delete File from Git

Delete file

```bash
git rm filename
```

Commit

```bash
git commit -m "Deleted file"
```

---

# Git Ignore

Create

```
.gitignore
```

Example

```
node_modules/
.env
*.log
dist/
__pycache__/
```

---

# Complete Git Workflow

```
Create Project
      │
      ▼
git init
      │
      ▼
git add .
      │
      ▼
git commit
      │
      ▼
git branch -M main
      │
      ▼
git remote add origin
      │
      ▼
git push
      │
      ▼
Modify Files
      │
      ▼
git add .
      │
      ▼
git commit
      │
      ▼
git push
      │
      ▼
Create Branch
      │
      ▼
git checkout -b feature
      │
      ▼
Develop Feature
      │
      ▼
git commit
      │
      ▼
git checkout main
      │
      ▼
git merge feature
      │
      ▼
git push
```

---

# Most Frequently Used Commands

| Command | Purpose |
|----------|---------|
| `git init` | Initialize repository |
| `git status` | Check status |
| `git add .` | Stage all files |
| `git commit -m` | Create commit |
| `git log` | View history |
| `git diff` | View changes |
| `git restore` | Restore file |
| `git reset` | Unstage file |
| `git branch` | List/Create branches |
| `git checkout` | Switch branch |
| `git merge` | Merge branches |
| `git clone` | Clone repository |
| `git remote -v` | View remote |
| `git pull` | Fetch & merge |
| `git fetch` | Download changes |
| `git push` | Upload commits |

---

# Best Practices

- Commit frequently with meaningful messages.
- Pull before pushing.
- Use feature branches.
- Keep `.gitignore` updated.
- Review changes before committing.
- Never commit sensitive information (API keys, passwords).
- Use descriptive branch names.

---

# Resources

- Git Documentation: https://git-scm.com/doc
- GitHub Documentation: https://docs.github.com
- GitHub Learning Lab: https://skills.github.com

---

# License

This guide is intended for learning Git and GitHub fundamentals.
