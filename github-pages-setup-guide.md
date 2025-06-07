# Complete Guide to Setting Up GitHub Pages for the First Time

## Table of Contents
1. [What is GitHub Pages?](#what-is-github-pages)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Setup Guide](#step-by-step-setup-guide)
4. [Common Pitfalls and How to Avoid Them](#common-pitfalls)
5. [Free Tier Features and Limitations](#free-tier-features-and-limitations)
6. [Troubleshooting Guide](#troubleshooting-guide)
7. [Best Practices](#best-practices)

## What is GitHub Pages?

GitHub Pages is a static site hosting service that takes HTML, CSS, and JavaScript files straight from a repository on GitHub and publishes them as a website. It's completely free for public repositories and perfect for hosting project documentation, personal websites, portfolios, and blogs.

## Prerequisites

Before starting, ensure you have:
- A GitHub account (free at github.com)
- Basic understanding of Git and GitHub
- A text editor (VS Code, Sublime Text, etc.)
- Basic HTML knowledge (for custom sites)

## Step-by-Step Setup Guide

### Method 1: Creating a User/Organization Site

User sites are published at `https://[username].github.io`

#### Step 1: Create a New Repository
1. **Navigate to GitHub** and click the "+" icon in the top-right corner
   - *Screenshot description: GitHub homepage with the plus icon highlighted in the navigation bar*

2. **Select "New repository"**
   - *Screenshot description: Dropdown menu showing "New repository" option*

3. **Name your repository** exactly as `[username].github.io`
   - Replace `[username]` with your actual GitHub username
   - Example: If your username is "johndoe", name it `johndoe.github.io`
   - **IMPORTANT**: The repository name must match this pattern exactly
   - *Screenshot description: New repository form with repository name field filled*

4. **Set repository to Public** (required for free GitHub Pages)
   - *Screenshot description: Repository visibility options with "Public" selected*

5. **Initialize with README** (optional but recommended)
   - *Screenshot description: Checkbox for "Add a README file" checked*

6. **Click "Create repository"**

#### Step 2: Enable GitHub Pages
1. **Go to Settings** in your repository
   - *Screenshot description: Repository navigation tabs with "Settings" highlighted*

2. **Scroll down to "Pages"** in the left sidebar
   - *Screenshot description: Settings sidebar with "Pages" section visible*

3. **Under "Source"**, select "Deploy from a branch"
   - *Screenshot description: GitHub Pages settings showing source dropdown*

4. **Select your branch** (usually "main" or "master")
   - *Screenshot description: Branch selection dropdown*

5. **Select folder** (choose "/ (root)" or "/docs")
   - *Screenshot description: Folder selection dropdown*

6. **Click "Save"**
   - GitHub will display a message: "Your site is ready to be published at https://[username].github.io"

#### Step 3: Add Content
1. **Create an index.html file** in your repository
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>My GitHub Pages Site</title>
   </head>
   <body>
       <h1>Welcome to My GitHub Pages Site</h1>
       <p>This is my first GitHub Pages website!</p>
   </body>
   </html>
   ```

2. **Commit the file** to your repository
   - *Screenshot description: GitHub file editor with commit message fields*

3. **Wait 10-20 minutes** for the site to deploy
   - You can check deployment status in the Actions tab
   - *Screenshot description: Actions tab showing deployment workflow*

### Method 2: Creating a Project Site

Project sites are published at `https://[username].github.io/[repository-name]`

#### Step 1: Use Any Existing Repository
1. **Navigate to any repository** you own
2. **Follow the same "Enable GitHub Pages" steps** from Method 1
3. Your site will be available at `https://[username].github.io/[repository-name]`

### Method 3: Using a Theme

#### Step 1: Choose a Jekyll Theme
1. **Go to Settings > Pages**
2. **Click "Choose a theme"**
   - *Screenshot description: Theme chooser button in Pages settings*
3. **Browse available themes** and click on one you like
   - *Screenshot description: Grid of available Jekyll themes*
4. **Click "Select theme"**

## Common Pitfalls and How to Avoid Them

### 1. Repository Naming Issues
**Problem**: Site not accessible at expected URL
**Solution**: 
- For user sites: Repository must be named exactly `[username].github.io`
- Case sensitivity matters! `JohnDoe.github.io` ≠ `johndoe.github.io`

### 2. 404 Errors After Setup
**Problem**: Getting 404 error when visiting your site
**Solutions**:
- Wait up to 20 minutes for initial deployment
- Check if GitHub Pages is enabled in Settings
- Ensure you have an `index.html` file in the root or specified folder
- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)

### 3. Changes Not Appearing
**Problem**: Updated content not showing on live site
**Solutions**:
- Check Actions tab for deployment status
- Wait 5-10 minutes for changes to propagate
- Hard refresh your browser
- Check if you're on the correct branch

### 4. HTTPS/SSL Issues
**Problem**: "Not Secure" warning in browser
**Solutions**:
- GitHub Pages automatically provides HTTPS
- If using custom domain, enable "Enforce HTTPS" in settings
- Wait up to 24 hours for SSL certificate generation

### 5. Build Failures
**Problem**: Jekyll build errors
**Solutions**:
- Check Actions tab for error messages
- Validate YAML front matter in markdown files
- Ensure no syntax errors in Liquid templates
- Use `jekyll serve` locally to test

## Free Tier Features and Limitations

### ✅ What's Included (Free)

1. **Hosting**
   - Unlimited public repositories can use GitHub Pages
   - Automatic HTTPS/SSL certificates
   - Built-in CDN (Content Delivery Network)

2. **Domains**
   - Free subdomain: `[username].github.io`
   - Custom domain support (you provide the domain)
   - Subdomain support (www, blog, etc.)

3. **Features**
   - Jekyll static site generator built-in
   - Automatic builds on push
   - GitHub Actions integration
   - Mobile-responsive themes

4. **Storage & Bandwidth**
   - 1GB storage limit per repository
   - 100GB monthly bandwidth (soft limit)
   - No hard visitor limits

### ❌ Limitations

1. **Repository Requirements**
   - Must be public (private repos require GitHub Pro)
   - Cannot exceed 1GB in size
   - Individual files limited to 100MB

2. **Content Restrictions**
   - Static sites only (no server-side code)
   - No databases
   - No dynamic content generation
   - No e-commerce or payment processing

3. **Build Limitations**
   - 10 builds per hour
   - Build timeout: 10 minutes
   - Jekyll plugins limited to approved list

4. **Usage Restrictions**
   - Not for commercial use
   - No excessive bandwidth usage
   - Must follow GitHub Terms of Service
   - No password protection (all content is public)

5. **Technical Limitations**
   - No .htaccess or server configuration
   - No PHP, Python, Ruby, etc.
   - No custom Jekyll plugins (unless using Actions)
   - Limited to Jekyll 3.9.0 (unless using Actions)

## Troubleshooting Guide

### Site Not Loading
1. **Check repository name** matches pattern
2. **Verify Pages is enabled** in Settings
3. **Check Actions tab** for build errors
4. **Wait 20 minutes** for initial deployment
5. **Try incognito/private browsing** mode

### Custom Domain Issues
1. **Verify DNS settings**:
   - A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - CNAME record: `[username].github.io`
2. **Add CNAME file** to repository root
3. **Enable "Enforce HTTPS"** after DNS propagation

### Build Errors
1. **Check Jekyll syntax** in _config.yml
2. **Validate front matter** in Markdown files
3. **Remove unsupported plugins**
4. **Check file encoding** (UTF-8 required)

## Best Practices

### 1. Local Development
```bash
# Install Jekyll locally
gem install bundler jekyll

# Create Gemfile
bundle init
bundle add jekyll

# Serve locally
bundle exec jekyll serve

# Visit http://localhost:4000
```

### 2. Repository Structure
```
├── index.html          # Homepage
├── _config.yml         # Jekyll configuration
├── _layouts/           # Page templates
├── _includes/          # Reusable components
├── assets/             # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── images/
├── _posts/             # Blog posts (if using blog)
├── about.html          # About page
└── CNAME              # Custom domain (if using)
```

### 3. Performance Optimization
- **Optimize images** (use WebP, compress JPEGs)
- **Minify CSS/JS** files
- **Use Jekyll's built-in Sass** processing
- **Leverage browser caching** with proper headers
- **Limit external resources**

### 4. SEO Best Practices
- Add **meta descriptions** to all pages
- Use **semantic HTML** structure
- Create a **sitemap.xml**
- Add **robots.txt** file
- Use **descriptive URLs**

### 5. Security Considerations
- **Never commit sensitive data** (API keys, passwords)
- **Use environment variables** in GitHub Actions
- **Validate user input** in JavaScript
- **Keep dependencies updated**
- **Review third-party scripts**

## Quick Reference

### Useful Commands
```bash
# Clone your repository
git clone https://github.com/[username]/[username].github.io.git

# Add all files
git add .

# Commit changes
git commit -m "Update site content"

# Push to GitHub
git push origin main

# Check site status
curl -I https://[username].github.io
```

### Important URLs
- Your site: `https://[username].github.io`
- Pages settings: `https://github.com/[username]/[username].github.io/settings/pages`
- Actions/Deployments: `https://github.com/[username]/[username].github.io/actions`
- GitHub Status: `https://www.githubstatus.com/`

### File Size Limits
- Repository: 1GB total
- Individual files: 100MB
- GitHub LFS not supported for Pages

### Supported File Types
- HTML, CSS, JavaScript
- Markdown (.md, .markdown)
- Images (JPEG, PNG, GIF, SVG, WebP)
- Fonts (TTF, OTF, WOFF, WOFF2)
- Data files (JSON, XML, CSV)

## Conclusion

GitHub Pages is an excellent free solution for hosting static websites. While it has limitations, it's perfect for:
- Personal portfolios
- Project documentation
- Blogs (using Jekyll)
- Landing pages
- Online resumes

Remember to always check the [official GitHub Pages documentation](https://docs.github.com/en/pages) for the most up-to-date information and features.

Happy publishing! 🚀