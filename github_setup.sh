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

# Create GitHub repository using curl
response=$(curl -s -H "Authorization: token ${github_pat}" https://api.github.com/user/repos -d '{"name":"ai_super_platform", "private":false}')

# Extract the SSH URL from the response
ssh_url=$(echo $response | grep -o '"ssh_url": "[^"]*' | cut -d'"' -f4)

if [ -z "$ssh_url" ]; then
    echo "Failed to create repository. Response:"
    echo $response
    exit 1
fi

# Add remote and push
git remote add origin $ssh_url
git branch -M main
git push -u origin main

echo "AI Super Platform successfully established on GitHub. Prepare for digital ascension!"
