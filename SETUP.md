# Repository Setup for GitHub Pages

## Directory Structure

```
latvian-names/
├── .github/
│   └── workflows/
│       └── pages.yml          # GitHub Actions for automatic deployment
├── data/                      # Raw CSV data files (gitignored)
│   ├── .gitkeep
│   ├── name_days.csv
│   ├── traditional_name_days.csv
│   ├── gender_data.csv
│   └── [popularity CSV files]
├── docs/                      # Web app (served by GitHub Pages)
│   ├── index.html             # Redirects to name_rating_app.html
│   ├── name_rating_app.html   # Main web application
│   ├── name_days_processed.json
│   └── README.md              # App usage documentation
├── scripts/                   # Data processing scripts
│   ├── download_data.py
│   ├── process_name_days.py
│   ├── requirements.txt
│   └── README.md
├── .gitignore
└── README.md                  # Main project documentation
```

## Initial Setup

1. **Install dependencies**:
   ```bash
   pip install -r scripts/requirements.txt
   ```

2. **Download data**:
   ```bash
   python3 scripts/download_data.py
   ```

3. **Process data**:
   ```bash
   python3 scripts/process_name_days.py
   ```

4. **Commit and push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

## GitHub Pages Configuration

The repository is configured to use the `/docs` folder for GitHub Pages.

### Automatic Deployment (Recommended)

The `.github/workflows/pages.yml` file will automatically deploy when you push to the main branch.

### Manual Configuration

1. Go to repository Settings → Pages
2. Source: "Deploy from a branch"
3. Branch: `main` or `master`
4. Folder: `/docs`
5. Save

## Accessing the App

After deployment, the app will be available at:
- `https://[username].github.io/[repository-name]/name_rating_app.html`
- Or via index.html redirect: `https://[username].github.io/[repository-name]/`
