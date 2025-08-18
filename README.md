# Leoo Bai - Modern Portfolio Website

A modern, responsive portfolio website built with Jekyll and featuring contemporary design elements.

## Features

### 🎨 Modern Design
- **Gradient Hero Section**: Eye-catching gradient background with smooth animations
- **Card-based Layout**: Clean, modern card design for content organization
- **Skill Tags**: Interactive skill badges with hover effects
- **Stats Section**: Animated statistics display
- **Timeline Layout**: Professional timeline for experience display

### 📱 Responsive Design
- **Mobile-first**: Optimized for all screen sizes
- **Touch-friendly**: Interactive elements work well on touch devices
- **Adaptive Navigation**: Responsive navigation menu with mobile toggle

### 🚀 Interactive Elements
- **Smooth Scrolling**: Smooth anchor link scrolling
- **Scroll Animations**: Elements animate as they come into view
- **Hover Effects**: Interactive hover states on all clickable elements
- **Dark Mode**: Toggle between light and dark themes
- **Typewriter Effect**: Animated text in hero section

### 🎯 Performance Optimized
- **Lazy Loading**: Images load only when needed
- **Optimized Animations**: Hardware-accelerated CSS animations
- **Minimal JavaScript**: Lightweight, efficient code
- **SEO Friendly**: Optimized meta tags and structured data

## Technical Stack

- **Jekyll**: Static site generator
- **Custom CSS**: Modern CSS with CSS Grid and Flexbox
- **Vanilla JavaScript**: No framework dependencies
- **Google Fonts**: Inter font family
- **Font Awesome**: Icon library

## Customization

### Colors
Edit the CSS variables in `assets/css/main.css`:
```css
:root {
  --primary-color: #2563eb;
  --secondary-color: #7c3aed;
  --accent-color: #06b6d4;
  /* ... more variables */
}
```

### Content
Update the main content in `index.md` and individual page files.

### Navigation
Modify the navigation menu in `_config.yml`:
```yaml
navigation:
  main:
    - title: "🏠 Home"
      url: /
    # ... more items
```

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Deployment

This site is designed to work seamlessly with GitHub Pages. Simply push to your repository and GitHub will automatically build and deploy the site.

## License

MIT License - feel free to use this as a template for your own portfolio!
