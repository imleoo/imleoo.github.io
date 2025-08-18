// Modern JavaScript for Leoo Bai's Portfolio

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  
  // Initialize animations and interactions
  initScrollAnimations();
  initSmoothScrolling();
  initSkillTags();
  initContactForm();
  initMobileMenu();
  initTypewriterEffect();
  initParallaxEffects();
});

// Scroll reveal animations
function initScrollAnimations() {
  const elements = document.querySelectorAll('.card, .stat-card, .contact-item, .blog-card');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('scroll-reveal', 'revealed');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  elements.forEach(element => {
    observer.observe(element);
  });
}

// Smooth scrolling for anchor links
function initSmoothScrolling() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// Skill tag interactions
function initSkillTags() {
  const skillTags = document.querySelectorAll('.skill-tag');
  
  skillTags.forEach(tag => {
    tag.addEventListener('mouseenter', function() {
      this.style.transform = 'scale(1.1) rotate(2deg)';
    });
    
    tag.addEventListener('mouseleave', function() {
      this.style.transform = 'scale(1) rotate(0deg)';
    });
    
    tag.addEventListener('click', function() {
      // Create ripple effect
      const ripple = document.createElement('span');
      ripple.style.position = 'absolute';
      ripple.style.width = '100%';
      ripple.style.height = '100%';
      ripple.style.background = 'rgba(255, 255, 255, 0.3)';
      ripple.style.borderRadius = '50%';
      ripple.style.transform = 'scale(0)';
      ripple.style.animation = 'ripple 0.6s ease-out';
      
      this.style.position = 'relative';
      this.style.overflow = 'hidden';
      this.appendChild(ripple);
      
      setTimeout(() => {
        ripple.remove();
      }, 600);
    });
  });
}

// Contact form interactions
function initContactForm() {
  const contactItems = document.querySelectorAll('.contact-item');
  
  contactItems.forEach(item => {
    item.addEventListener('click', function() {
      // Add click animation
      this.style.transform = 'scale(0.95)';
      setTimeout(() => {
        this.style.transform = 'scale(1)';
      }, 150);
    });
  });
}

// Mobile menu toggle
function initMobileMenu() {
  // Create mobile menu button if it doesn't exist
  if (!document.querySelector('.mobile-menu-toggle')) {
    const nav = document.querySelector('nav');
    if (nav) {
      const mobileButton = document.createElement('button');
      mobileButton.className = 'mobile-menu-toggle';
      mobileButton.innerHTML = '☰';
      mobileButton.style.cssText = `
        display: none;
        background: var(--primary-color);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1.2rem;
      `;
      
      nav.insertBefore(mobileButton, nav.firstChild);
      
      mobileButton.addEventListener('click', function() {
        const menu = nav.querySelector('ul');
        if (menu) {
          menu.style.display = menu.style.display === 'none' ? 'block' : 'none';
        }
      });
      
      // Show mobile menu button on small screens
      const checkScreenSize = () => {
        if (window.innerWidth <= 768) {
          mobileButton.style.display = 'block';
          const menu = nav.querySelector('ul');
          if (menu) menu.style.display = 'none';
        } else {
          mobileButton.style.display = 'none';
          const menu = nav.querySelector('ul');
          if (menu) menu.style.display = 'flex';
        }
      };
      
      window.addEventListener('resize', checkScreenSize);
      checkScreenSize();
    }
  }
}

// Typewriter effect for hero title
function initTypewriterEffect() {
  const heroTitle = document.querySelector('.hero-title');
  if (heroTitle) {
    const text = heroTitle.textContent;
    heroTitle.textContent = '';
    heroTitle.style.borderRight = '3px solid white';
    heroTitle.style.animation = 'blink 1s infinite';
    
    let index = 0;
    const typeWriter = () => {
      if (index < text.length) {
        heroTitle.textContent += text.charAt(index);
        index++;
        setTimeout(typeWriter, 100);
      } else {
        setTimeout(() => {
          heroTitle.style.borderRight = 'none';
          heroTitle.style.animation = 'none';
        }, 1000);
      }
    };
    
    // Start typewriter effect after a short delay
    setTimeout(typeWriter, 500);
  }
}

// Parallax scrolling effects
function initParallaxEffects() {
  const heroSection = document.querySelector('.hero-section');
  if (heroSection) {
    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      const rate = scrolled * -0.5;
      heroSection.style.transform = `translateY(${rate}px)`;
    });
  }
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
  @keyframes ripple {
    to {
      transform: scale(4);
      opacity: 0;
    }
  }
  
  @keyframes blink {
    0%, 50% { border-color: white; }
    51%, 100% { border-color: transparent; }
  }
  
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  .scroll-reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.6s ease;
  }
  
  .scroll-reveal.revealed {
    opacity: 1;
    transform: translateY(0);
  }
  
  .card:hover, .stat-card:hover, .contact-item:hover, .blog-card:hover {
    animation: bounce 0.6s ease;
  }
  
  @keyframes bounce {
    0%, 20%, 53%, 80%, 100% {
      transform: translate3d(0, 0, 0);
    }
    40%, 43% {
      transform: translate3d(0, -8px, 0);
    }
    70% {
      transform: translate3d(0, -4px, 0);
    }
    90% {
      transform: translate3d(0, -2px, 0);
    }
  }
`;
document.head.appendChild(style);

// Add loading animation
window.addEventListener('load', function() {
  document.body.style.opacity = '0';
  document.body.style.transition = 'opacity 0.5s ease';
  
  setTimeout(() => {
    document.body.style.opacity = '1';
  }, 100);
});

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Apply debounce to scroll events
window.addEventListener('scroll', debounce(() => {
  // Add any scroll-dependent animations here
}, 10));

// Add dark mode toggle
function initDarkMode() {
  const darkModeToggle = document.createElement('button');
  darkModeToggle.innerHTML = '🌙';
  darkModeToggle.className = 'dark-mode-toggle';
  darkModeToggle.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background: var(--primary-color);
    color: white;
    border: none;
    padding: 0.5rem;
    border-radius: 50%;
    cursor: pointer;
    font-size: 1.2rem;
    z-index: 1000;
    width: 40px;
    height: 40px;
  `;
  
  document.body.appendChild(darkModeToggle);
  
  darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    darkModeToggle.innerHTML = document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
  });
}

// Initialize dark mode toggle
initDarkMode();