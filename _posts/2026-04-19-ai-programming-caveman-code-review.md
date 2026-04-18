---
layout: post
title: "Why AI Programming Needs Caveman-Style Code Review"
date: 2026-04-19 10:00:00 +0800
categories: ["AI", "Programming", "Code Review"]
description: "Exploring why AI programming benefits from simple, caveman-style code review practices."
excerpt: "AI programming needs straightforward, caveman-style code review to avoid messy codebases."
author: Leoo Bai
---

This is quite amusing. I recently came across an article about "Vibe Coding," and honestly, it made me laugh—tech media loves to hype up "disruptive revolutions," but few dare to admit that this stuff might turn a company's codebase into a landfill.  

The article’s title went straight for the jugular: *The Hidden Risks of Vibe Coding* (pretend there’s a link here). Every team using AI for coding should give it a read. The world is raving about how "natural language programming is a game-changer," but let’s be real—would you actually trust a chatbot with your production environment?  

First, the scariest part. The article mentions a case where a company’s AI-generated backend code looked sleek, but an audit revealed three critical security vulnerabilities. The kicker? No one on the team noticed because nobody actually bothered to read the "magic code." Think about that—if an AI plants a backdoor in the code, do we award it "Best Spy of the Year"?  

The article outlines four protective steps, and the most practical one is the third: enforce old-school code reviews for AI-generated code. Counterintuitive, right? In the age of AI, we’re still manually reviewing? But consider this: AI assistants today are like overly flattering interns, nodding along with "Yes, boss!" while leading you straight into a ditch. Our team now mandates that all AI-generated code must be reviewed line-by-line by two actual humans, caveman-style.  

Another overlooked risk? Technical debt will explode. AI writes code fast, but it often relies on hacky shortcuts. Six months later, when you’re maintaining it, you might find the entire block held together like duct-taped Legos—it runs, but nobody dares touch it. The article suggests setting aside weekly time to clean up AI-generated tech debt. We tried it, and it’s more effective than caffeine.  

What really struck me is the state of the industry. Funding announcements are all about "AI coding platforms doubling in valuation," but few discuss how these tools might turn engineers into "code illiterates." A VC friend told me they now ask startups: "Does anyone on your team still write SQL by hand?" Sounds like a joke, but it’s a wake-up call.  

Don’t get me wrong—I’m not against using AI for coding. We use it too, and it’s undeniably efficient. But here’s the thing: treat it like a kitchen blender. Great for chopping veggies, but never let it decide what’s for dinner. The article’s analogy is perfect: AI should be the copilot, not the autopilot.  

Finally, a rant. Some teams, in their rush to meet deadlines, treat AI as their lead developer. The wildest example? A PM used ChatGPT to write an entire API, bragged about it on social media, and then watched the database crash on launch day—because the AI stored passwords in plaintext. Moral of the story: flex all you want, just don’t do it in production.  

(The End)