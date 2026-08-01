---
layout: page
title: "Blog"
permalink: /blog/
description: "Explore Leoo Bai's blog on AI-assisted coding, Claude Code, agentic engineering, and the security and technical debt implications of AI-generated software."
---

# Blog

## Latest Articles

{% for post in site.posts %}
<div class="post-item">
  <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
  <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}{% if post.categories %} in {% for category in post.categories %}<span class="category">{{ category }}</span>{% endfor %}{% endif %}</p>
  <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
  <a href="{{ post.url }}" class="read-more">Read More →</a>
</div>
{% endfor %}

## Topics I Cover

- **AI Coding & Agentic Engineering** — Claude Code, OpenClaw, and how AI-assisted development is reshaping the programmer's role
- **AI Security & Technical Debt** — the risks and governance gaps that come with AI-generated code
- **Industry Analysis** — AI infrastructure, developer tooling, and where the ecosystem is heading

### Guest Posts & Collaborations

Open to guest posts, co-authored articles, and expert interviews in the AI/software development space. Reach out via [email](mailto:imleoo@gmail.com).

### Follow Along

**[Twitter](https://twitter.com/leoobai)**

<style>
.post-item {
  margin-bottom: 2rem;
  padding: 1.5rem;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background: #fff;
}

.post-item h3 {
  margin: 0 0 0.5rem 0;
  color: #333;
}

.post-item h3 a {
  color: #333;
  text-decoration: none;
}

.post-item h3 a:hover {
  color: #007bff;
}

.post-meta {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.category {
  background: #009e9f;
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  margin-left: 0.3rem;
}

.post-excerpt {
  color: #555;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.read-more {
  color: #009e9f;
  text-decoration: none;
  font-weight: 500;
}

.read-more:hover {
  text-decoration: underline;
}
</style>