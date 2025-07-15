# 🚀 Jomeburger GitHub Pages Setup Script
# Professional deployment script for real-world production use
# Automates GitHub repository creation and HTTPS deployment

Write-Host "🍔 Jomeburger GitHub Pages Setup" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Green

# Check if git is installed
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git is not installed! Please install Git first." -ForegroundColor Red
    exit 1
}

# Check if we're in the right directory
if (!(Test-Path "main_simple.py")) {
    Write-Host "❌ Run this script from the jomeburger-telegram-bot directory!" -ForegroundColor Red
    exit 1
}

Write-Host "📋 Before proceeding, make sure you have:" -ForegroundColor Yellow
Write-Host "   1. GitHub account created" -ForegroundColor White
Write-Host "   2. Git configured with your username and email" -ForegroundColor White
Write-Host "   3. Ready to create a new repository named 'jomeburger-telegram-bot'" -ForegroundColor White
Write-Host ""

$confirm = Read-Host "Continue? (y/N)"
if ($confirm -ne "y" -and $confirm -ne "Y") {
    Write-Host "❌ Setup cancelled." -ForegroundColor Red
    exit 0
}

# Get GitHub username
$username = Read-Host "Enter your GitHub username"
if ([string]::IsNullOrWhiteSpace($username)) {
    Write-Host "❌ GitHub username is required!" -ForegroundColor Red
    exit 1
}

Write-Host "🔧 Setting up Git repository..." -ForegroundColor Blue

# Initialize git repository
try {
    git init
    Write-Host "✅ Git repository initialized" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to initialize git repository" -ForegroundColor Red
    exit 1
}

# Update README with actual username
try {
    $readmeContent = Get-Content "README.md" -Raw
    $readmeContent = $readmeContent -replace "USERNAME", $username
    Set-Content "README.md" $readmeContent
    Write-Host "✅ README updated with your username" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Warning: Could not update README with username" -ForegroundColor Yellow
}

# Create .gitignore if it doesn't exist
if (!(Test-Path ".gitignore")) {
    @"
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
venv/
env/
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Temporary files
*.tmp
*.temp

# Database
*.db
*.sqlite3
"@ | Out-File -FilePath ".gitignore" -Encoding UTF8
    Write-Host "✅ .gitignore created" -ForegroundColor Green
}

# Add all files to git
try {
    git add .
    Write-Host "✅ Files added to git" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to add files to git" -ForegroundColor Red
    exit 1
}

# Initial commit
try {
    git commit -m "🍔 Initial Jomeburger deployment - Professional food delivery platform"
    Write-Host "✅ Initial commit created" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to create initial commit" -ForegroundColor Red
    exit 1
}

# Rename branch to main
try {
    git branch -M main
    Write-Host "✅ Branch renamed to main" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Warning: Could not rename branch to main" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🎉 Local Git setup completed!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Next steps:" -ForegroundColor Yellow
Write-Host "1. Go to https://github.com/new" -ForegroundColor White
Write-Host "2. Create a new repository named: jomeburger-telegram-bot" -ForegroundColor White
Write-Host "3. Make it public (required for GitHub Pages)" -ForegroundColor White
Write-Host "4. Don't initialize with README (we already have one)" -ForegroundColor White
Write-Host "5. Run these commands:" -ForegroundColor White
Write-Host ""
Write-Host "git remote add origin https://github.com/$username/jomeburger-telegram-bot.git" -ForegroundColor Cyan
Write-Host "git push -u origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "6. Enable GitHub Pages:" -ForegroundColor White
Write-Host "   - Go to repository Settings > Pages" -ForegroundColor White
Write-Host "   - Source: Deploy from a branch" -ForegroundColor White
Write-Host "   - Branch: main" -ForegroundColor White
Write-Host "   - Folder: / (root)" -ForegroundColor White
Write-Host ""
Write-Host "🌐 Your web app will be available at:" -ForegroundColor Green
Write-Host "https://$username.github.io/jomeburger-telegram-bot/" -ForegroundColor Cyan
Write-Host ""
Write-Host "🤖 Update your bot with the HTTPS URL and you're ready!" -ForegroundColor Green

# Offer to open GitHub
$openGitHub = Read-Host "Open GitHub in browser to create repository? (y/N)"
if ($openGitHub -eq "y" -or $openGitHub -eq "Y") {
    Start-Process "https://github.com/new"
}
