# 🚀 Git & GitHub Learning Log  
_A comprehensive recap of everything I learned about Git and GitHub collaboration_
## 📦 Repository Basics
- **Create a Repository:**
  1. Go to GitHub ➝ Click on **New Repository**
  2. Give it a name, description, and choose visibility (Public/Private)
  3. Initialize with a README (optional, but helpful!)
- **Git Commands:**
  ```bash
  git init              # Initialize local repo
  git clone <url>       # Clone existing repo
  git remote add origin <url>   # Connect local repo to GitHub
  git push -u origin main       # Push initial code
## 🌱 Branching & Collaboration
- **Create and Switch Branch:**
  ```bash
  git add branch -m "branchname"
  git switch branchname
- **Push Branch:**
  git push -u origin new-feature
- **Merge Branch:**
  1. Go to Pull Requests tab on GitHub
  2. Compare & create pull request
  3. merge to the main branch
## 🤝 Collaborating with Others
- **Steps for Team Collaboration:**
  1. Fork the repository (if external contributor)
  2. Clone the fork
  3. Create a new branch for your work
  4. Commit & push changes
  5. Open a Pull Request
- **Important Git Commands for Collaboration:**
  ```bash
  git pull origin main       # Update local with remote changes
  git fetch --all            # Get branches and commits from all remotes
  git merge origin/main      # Merge fetched changes into current branch
## 🧠 Git Essentials
- **Commit Changes:**
  ```bash
  git add .                  # Stage all changes
  git commit -m "Your message here"
- **View History:**
  ```bash
  git log
- **Undo Changes:**
  ```bash
  git checkout <file>         # Discard changes in a file
  git reset --hard HEAD       # Reset to last commit
## What I Learned
- Git is local version control; GitHub is cloud-based collaboration for Git repos.
- Branching is like sketching design variations—safe, reversible, and great for teamwork.
- Pull requests work like design critiques—reviewed before merging.
- Commit messages = documentation of thought process X
