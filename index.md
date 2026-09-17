---
layout: home
---

<!-- Hero Section -->
<div class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">Leoo Bai</h1>
    <p class="hero-subtitle">AI/Agent Engineering Researcher & Writer</p>
    <p class="hero-description">Author of DDAD | Ex-CTO (130M+ users), 10+ yrs in AI & Big Data | Founder of AiSEO.icu</p>
    <div class="hero-buttons">
      <a href="#contact" class="btn-primary">Get In Touch</a>
      <a href="/experience/" class="btn-secondary">View Experience</a>
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

<!-- Skills Section -->
<div class="container" style="padding: 4rem 2rem;">
  <div class="text-center mb-5">
    <h2 class="section-title">Core Expertise</h2>
    <p class="section-subtitle">Specialized in cutting-edge technology domains</p>
  </div>
  
  <div class="skills-container">
    <div class="skill-tag">🧠 AI/Agent Engineering</div>
    <div class="skill-tag">🤖 AI & ML</div>
    <div class="skill-tag">📊 Big Data</div>
    <div class="skill-tag">☁️ Cloud Arch</div>
    <div class="skill-tag">🎥 Video Systems</div>
    <div class="skill-tag">🛡️ Risk Mgmt</div>
    <div class="skill-tag">⚡ Real-time Computing</div>
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

<!-- Current Focus Tagline -->
<div class="container" style="padding: 2rem 2rem; text-align: center; background: var(--bg-secondary);">
  <h2 class="section-title">🚀 Currently: AI/Agent Engineering</h2>
  <p class="section-subtitle">Author of the DDAD (Document-Driven AI Development) framework, building ModelTesting (a multi-vendor LLM testing platform), and writing on agentic engineering — alongside founding AiSEO.icu</p>
</div>

<!-- Action Bar -->
<div class="container" style="padding: 3rem 2rem; text-align: center;">
  <p class="section-subtitle">Explore my professional journey and technical achievements</p>
  <div class="hero-buttons">
    <a href="/experience/" class="btn-secondary">Professional Timeline</a>
    <a href="/projects/" class="btn-secondary">Technical Projects</a>
    <a href="/contact/" class="btn-primary">Get In Touch</a>
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