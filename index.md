---
layout: home
---

<!-- Hero Section -->
<div class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">白德鑫 Leoo Bai</h1>
    <p class="hero-subtitle">Senior Technology Executive & AI Specialist</p>
    <p class="hero-description">Founder of AiSEO.icu | 10+ years in AI, Big Data & Cloud Computing</p>
    <div class="hero-buttons">
      <a href="#contact" class="btn-primary">Get In Touch</a>
      <a href="#experience" class="btn-secondary">View Experience</a>
    </div>
  </div>
</div>

<!-- Skills Section -->
<div class="container" style="padding: 4rem 2rem;">
  <div class="text-center mb-5">
    <h2 class="section-title">Core Expertise</h2>
    <p class="section-subtitle">Specialized in cutting-edge technology domains</p>
  </div>
  
  <div class="skills-container">
    <div class="skill-tag">🤖 AI & Machine Learning</div>
    <div class="skill-tag">📊 Big Data Analytics</div>
    <div class="skill-tag">☁️ Cloud Architecture</div>
    <div class="skill-tag">🎥 Video Streaming</div>
    <div class="skill-tag">🛡️ Risk Management</div>
    <div class="skill-tag">⚡ Real-time Processing</div>
    <div class="skill-tag">🔍 Predictive Analytics</div>
    <div class="skill-tag">🌐 CDN Technology</div>
  </div>
</div>

<!-- Stats Section -->
<div class="container" style="padding: 2rem 2rem;">
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-number">130M+</div>
      <div class="stat-label">Users Supported</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">180+</div>
      <div class="stat-label">Engineers Led</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">10+</div>
      <div class="stat-label">Years Experience</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">95%+</div>
      <div class="stat-label">Model Accuracy</div>
    </div>
  </div>
</div>

<!-- Current Focus -->
<div class="container" style="padding: 4rem 2rem;">
  <div class="text-center mb-5">
    <h2 class="section-title">Current Focus</h2>
    <p class="section-subtitle">Leading innovation in AI-powered solutions</p>
  </div>
  
  <div class="row">
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          <div class="card-icon">🚀</div>
          <h3 class="card-title">AiSEO.icu</h3>
        </div>
        <p><strong>Founder & CEO</strong> | 2025 - Present</p>
        <p>Building next-generation AI-powered SEO and digital marketing infrastructure for global businesses.</p>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          <div class="card-icon">🎯</div>
          <h3 class="card-title">Technical Excellence</h3>
        </div>
        <p>Focusing on scalable AI solutions, cloud architecture optimization, and cutting-edge machine learning applications.</p>
      </div>
    </div>
  </div>
</div>

<!-- Recent Achievements -->
<div class="container" style="padding: 4rem 2rem; background: var(--bg-secondary);">
  <div class="text-center mb-5">
    <h2 class="section-title">Recent Achievements</h2>
    <p class="section-subtitle">Delivering impactful technical solutions</p>
  </div>
  
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-header">
          <div class="card-icon">🏛️</div>
          <h3 class="card-title">Cross-border Trade Compliance</h3>
        </div>
        <ul>
          <li>95%+ compliance risk identification accuracy</li>
          <li>Transformer & LSTM algorithms implementation</li>
          <li>99.93% HS code classification accuracy</li>
        </ul>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="card">
        <div class="card-header">
          <div class="card-icon">💰</div>
          <h3 class="card-title">Financial Risk Modeling</h3>
        </div>
        <ul>
          <li>Trade finance risk models for banking</li>
          <li>Fraud detection & anti-money laundering</li>
          <li>Customs data integration for loans</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- Latest Blog Posts -->
<div class="container" style="padding: 4rem 2rem;">
  <div class="text-center mb-5">
    <h2 class="section-title">Latest Insights</h2>
    <p class="section-subtitle">Sharing knowledge and experiences</p>
  </div>
  
  <div class="blog-grid">
    {% for post in site.posts limit: 3 %}
    <div class="blog-card">
      <div class="blog-card-image">
        <span>📝</span>
      </div>
      <div class="blog-card-content">
        <h3 class="blog-card-title">{{ post.title }}</h3>
        <p class="blog-card-date">{{ post.date | date: "%B %d, %Y" }}</p>
        <p class="blog-card-excerpt">{{ post.excerpt | strip_html | truncatewords: 20 }}</p>
        <a href="{{ post.url }}" class="btn-primary" style="margin-top: 1rem;">Read More</a>
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<!-- Contact Section -->
<div id="contact" class="container" style="padding: 4rem 2rem;">
  <div class="text-center mb-5">
    <h2 class="section-title">Let's Connect</h2>
    <p class="section-subtitle">Open to collaboration and opportunities</p>
  </div>
  
  <div class="contact-grid">
    <div class="contact-item">
      <div class="contact-icon">💼</div>
      <h3>LinkedIn</h3>
      <a href="https://linkedin.com/in/leoo-bai" target="_blank">linkedin.com/in/leoo-bai</a>
    </div>
    <div class="contact-item">
      <div class="contact-icon">💻</div>
      <h3>GitHub</h3>
      <a href="https://github.com/imleoo" target="_blank">github.com/imleoo</a>
    </div>
    <div class="contact-item">
      <div class="contact-icon">🌐</div>
      <h3>Website</h3>
      <a href="https://aiseo.icu" target="_blank">aiseo.icu</a>
    </div>
    <div class="contact-item">
      <div class="contact-icon">📧</div>
      <h3>Email</h3>
      <a href="mailto:baidexin@outlook.com">baidexin@outlook.com</a>
    </div>
  </div>
</div>

<!-- Custom Styles -->
<style>
.container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 1rem;
}

.section-subtitle {
  font-size: 1.2rem;
  color: var(--text-secondary);
  margin-bottom: 3rem;
}

.hero-description {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.skills-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  margin: 2rem 0;
}

.row {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}

.col-md-6, .col-lg-6 {
  flex: 1;
  min-width: 300px;
}

@media (max-width: 768px) {
  .hero-buttons {
    flex-direction: column;
    align-items: center;
  }
  
  .btn-primary, .btn-secondary {
    width: 200px;
  }
}
</style>