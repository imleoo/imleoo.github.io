---
layout: post
title: "Why AI-Generated Code Can Give You a Heart Attack"
date: 2026-05-01 10:00:00 +0800
categories: ["AI", "Programming", "Technology"]
description: "Exploring the risks of AI-generated code through insights from Andrej Karpathy."
excerpt: "AI-generated code can be risky, as highlighted by Andrej Karpathy."
author: Leoo Bai
---

This is actually pretty interesting.  
The other day, I came across a talk by Andrej Karpathy—the former head of AI at Tesla, OpenAI founding member, and now the mastermind behind Vibe Coding. He straight-up said: "AI-generated code can sometimes give you a heart attack."  

Honestly, my first thought was: Finally, someone dares to tell the truth.  

Everyone’s hyping up how amazing AI is at writing code these days, as if programmers are about to become obsolete. But anyone who’s actually used these tools knows that AI-generated code is like a rebellious teenager—it might run, but you have no idea why; and when it doesn’t run, you’re even more clueless.  

Karpathy dropped this gem during a talk at Sequoia Capital, so the context is legit. He pointed out the reliability issues with AI code, which boils down to: "It looks pretty, but falls apart in practice." For example, if you ask AI to write a sorting algorithm, it might spit out a working version that’s slower than molasses. Or, even better, the logic might be completely nonsensical—yet somehow it still compiles.  

I’ve been there. Last month, I used an AI tool to generate some database query code, and it ran painfully slow. When I rewrote it myself, I realized the AI had used a full table scan—a disaster in production.  

The real problem is that too many people treat AI coding tools like "black-box magic." They type in a requirement, hit enter blindly, and expect perfect code. But in reality, AI might even misinterpret the word "requirement."  

Karpathy’s Vibe Coding is tackling this issue head-on. His approach: Don’t let AI write code independently. Instead, treat it like "supercharged autocomplete." Humans keep full control, while AI handles the nitty-gritty details. It’s a pragmatic take—no matter how advanced AI gets, it’s still just a high-powered assistant for now.  

Some might argue, "Just wait for the next-gen models." But I suspect reliability will remain a long-term challenge. AI learns from probabilities, but code demands certainty. That gap isn’t something brute-force computing can bridge.  

The funniest part? Karpathy is a top-tier AI expert, and even he admits AI code can be heart-attack-inducing. It’s like a Michelin-starred chef dunking on microwave meals—not exactly damaging, but brutally honest.  

So what’s the right way to use AI for coding? Here’s my take:  
1. Never let it write entire functions—break tasks into small snippets.  
2. Read every line of generated code with a critical eye.  
3. For complex logic, build the framework yourself first.  

At the end of the day, AI coding tools are like training wheels. They’ll help you stay balanced, but don’t expect them to pedal for you.  

(The End)