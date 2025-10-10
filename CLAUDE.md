# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a modern portfolio website for Leoo Bai, built with Jekyll and deployed on GitHub Pages. The site showcases professional experience, projects, and blog posts with contemporary design elements including gradients, animations, and responsive design.

## Development Commands

### Local Development
```bash
# Install Jekyll and dependencies
bundle install

# Start local development server
bundle exec jekyll serve

# Build the site for production
bundle exec jekyll build

# Clean build artifacts
bundle exec jekyll clean
```

### Alternative Local Development (if Bundler not available)
```bash
# Install Jekyll globally
gem install jekyll

# Start development server
jekyll serve

# Build site
jekyll build
```

## Architecture & Structure

### Jekyll Configuration
- **Config File**: `_config.yml` - Contains site settings, navigation, plugins, and build configuration
- **Theme**: Custom theme based on Jekyll's default theme with extensive CSS customizations
- **Plugins**: jekyll-feed, jekyll-sitemap, jekyll-seo-tag, jekyll-paginate, jekyll-include-cache

### Layout System
- **Base Layout**: `_layouts/default.html` - Contains navigation structure, SEO meta tags, and responsive design
- **Page Layouts**: `_layouts/page.html`, `_layouts/single.html`, `_layouts/post.html` - Specialized layouts for different content types
- **Home Layout**: `_layouts/home.html` - Custom homepage layout

### Content Organization
- **Main Pages**: All main pages are in the root directory (index.md, about.md, experience.md, etc.)
- **Blog Posts**: Stored in `_posts/` directory (if any exist)
- **Navigation**: Configured in `_config.yml` under the `navigation.main` array

### Assets & Styling
- **CSS**: `assets/css/main.css` - Custom CSS with CSS variables, dark mode support, and responsive design
- **JavaScript**: `assets/js/main.js` - Interactive features including scroll animations, smooth scrolling, and mobile menu
- **Images**: `assets/images/` - Contains avatar, favicon, OG image, and project screenshots
- **External Dependencies**: Google Fonts (Inter), Font Awesome icons

### Key Features
- **Responsive Navigation**: Mobile-first navigation with hamburger menu
- **Dark Mode**: Automatic dark mode support using CSS media queries
- **Scroll Animations**: Intersection Observer API for scroll-reveal effects
- **Interactive Elements**: Hover effects, smooth scrolling, typewriter effects
- **SEO Optimization**: Meta tags, Open Graph, Twitter Cards

## Styling System

### CSS Variables
The site uses CSS custom properties for consistent theming:
- `--primary-color`, `--secondary-color`, `--accent-color` - Main brand colors
- `--text-primary`, `--text-secondary` - Typography colors
- `--bg-primary`, `--bg-secondary` - Background colors
- `--gradient-1`, `--gradient-2`, `--gradient-3` - Predefined gradients

### Responsive Design
- Mobile-first approach with breakpoints at 768px
- Flexbox and CSS Grid for layout
- Sticky navigation with backdrop blur effect

## Deployment

The site is configured for GitHub Pages deployment:
- **CNAME**: Points to custom domain (if configured)
- **Base URL**: Empty string for root domain deployment
- **Automatic Deployment**: GitHub Pages automatically builds on push to main branch

## Customization Guidelines

### Navigation Updates
Update the `navigation.main` array in `_config.yml`:
```yaml
navigation:
  main:
    - title: "Page Title"
      url: /page-url/
```

### Color Scheme
Edit CSS variables in `assets/css/main.css`:
```css
:root {
  --primary-color: #009e9f;
  --secondary-color: #007b7c;
  /* ... other variables */
}
```

### Content Updates
- Edit main pages in root markdown files
- Blog posts go in `_posts/YYYY-MM-DD-title.md` format
- Project images and assets go in `assets/images/`

## Development Notes

- The site uses Jekyll 4.3+ with Ruby dependencies managed by Bundler
- No build scripts needed - Jekyll handles compilation automatically
- Custom CSS and JS are included directly in the HTML via the default layout
- The site supports both light and dark themes automatically
- All interactive features use vanilla JavaScript (no framework dependencies)