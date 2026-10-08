# 🚀 Raj Dixit — GitHub Profile Portfolio Preview & Guide

Welcome to your custom-crafted, premium GitHub Profile README system. This repository contains the complete visual identity, illustrated character assets, and production-ready SVG cards designed specifically for **Raj Dixit**.

---

## 📁 Repository Structure

```
Github_profile/
├── README.md                 # The main GitHub Profile README (used on your profile)
├── README_PREVIEW.md         # Documentation & deployment guide (this file)
├── preview.html              # Local browser preview simulating GitHub's renderer
├── README_PROFILE.zip        # Portable archive containing all files
├── generate_assets.py        # Python script to regenerate SVGs if needed
└── assets/
    ├── hero.svg              # 01 // Hero header with animated avatar & motif
    ├── about.svg             # 02 // Engineering philosophy & CS student mindset
    ├── projects.svg          # 03 // Currently building & focus tracks
    ├── stack.svg             # 04 // Categorized tech stack & official brand chips
    ├── stats.svg             # 05 // Development journey & cadence visualizer
    ├── connect.svg           # 06 // Connect section with right-pointing character
    ├── id.png                # High-res transparent developer portrait (1024x1024)
    └── right_pointing.png    # High-res transparent pointing character (1024x1024)
```

---

## 🎨 Visual Identity & Architecture

- **Color System:** Sophisticated light mode palette (`#FFFFFF` / `#F8FAFC` base, subtle `#EEF2FF` and `#3B82F6`/`#6366F1` gradient accents, high-contrast `#0F172A` typography).
- **Core Motif:** `BUILD` (Software & AI) ➜ `LEARN` (DSA & Core Computing) ➜ `SHIP` (Real Solutions).
- **Authentic Portrait Assets:** Generated from your photo to preserve your exact facial features, hairstyle, and smile in a modern semi-realistic developer illustration style with clean alpha transparency.
- **100% Self-Contained:** No external third-party tracker servers, no fragile image hosting, and no complex iframe dependencies. All SVGs work natively through GitHub's markdown image renderer.

---

## ⚙️ Personalization Checklist

Before pushing to GitHub, you can quickly customize the following placeholders inside [`README.md`](file:///c:/Users/rajdi/OneDrive/Desktop/Github_profile/README.md):

1. **`YOUR_GITHUB_USERNAME`** — Your exact GitHub handle (e.g. `rajdixit`).
2. **`YOUR_LINKEDIN_USERNAME`** — Your LinkedIn profile slug.
3. **`YOUR_PORTFOLIO_URL`** — Your personal portfolio website link (or omit the row if not yet deployed).
4. **`YOUR_YOUTUBE_HANDLE`** — Your YouTube handle (or omit if preferred).
5. **`YOUR_INSTAGRAM_HANDLE`** — Your Instagram profile handle (or omit if preferred).
6. **Project Cards** — Update the project names and descriptions in the `Featured Repositories` table with your actual repository links.

---

## 🚢 How to Deploy to GitHub

1. **Create Special Repository:**
   - Log in to your GitHub account.
   - Click **New repository**.
   - Set the **Repository name** to match your exact **GitHub username** (e.g., if your username is `rajdixit`, name the repo `rajdixit`).
   - GitHub will display a message: *"You found a secret! rajdixit/rajdixit is a special repository that you can use to add a README.md to your GitHub profile."*
   - Make sure the repository is set to **Public** and initialize with or without README (we will push our files).

2. **Push the Files:**
   Open terminal inside this folder and run:
   ```bash
   git init
   git add .
   git commit -m "feat: setup premium developer profile README"
   git branch -M main
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME.git
   git push -u origin main
   ```

3. **Verify:**
   - Visit `https://github.com/YOUR_GITHUB_USERNAME`.
   - Your premium profile will instantly render at the top of your profile page!
