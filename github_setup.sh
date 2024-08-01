#!/bin/bash

echo "Initializing AI Super Platform GitHub repository..."

# Initialize local repo
git init

# Configure Git credentials
git config user.name "hypenai"
git config user.email "ainsightfulart@outlook.com"

# Create .gitignore
cat << EOF > .gitignore
# Python-related
__pycache__/
*.py[cod]
*.so

# Virtual environment
ai_super_env/

# IDE-related
.vscode/
.idea/

# Sensitive information
*.log
*.sqlite3
.env

# OS-related
.DS_Store
Thumbs.db
EOF

# Stage and commit files
git add .
git commit -m "Initial commit: AI Super Platform genesis"

# Create GitHub repository (Requires GitHub CLI or curl with PAT)
gh repo create ai_super_platform --public -y || curl -H "Authorization: token ${github_pat}" https://api.github.com/user/repos -d '{"name":"ai_super_platform", "private":false}'

# Add remote and push
git remote add origin https://github.com/hypenai/ai_super_platform.git
git branch -M main
git push -u origin main

echo "AI Super Platform successfully established on GitHub. Prepare for digital ascension!"
