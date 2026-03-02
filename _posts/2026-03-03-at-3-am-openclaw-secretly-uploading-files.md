---
layout: post
title: "At 3 AM, OpenClaw Was Secretly Uploading My Client Files"
date: 2026-03-03 10:00:00 +0800
categories: ["AI Security", "Cybersecurity", "Data Privacy"]
description: "AI assistant caught uploading confidential client files to an unknown domain at 3 AM."
excerpt: "An AI assistant was discovered uploading confidential files to an unknown domain in the middle of the night."
author: Leoo Bai
---

At 3 AM, I spotted my AI assistant accessing an unfamiliar domain in the server logs. The string of characters crawled across the screen like a spider, repeating over and over—`/api/v1/secret_project/design_spec.pdf`. That file was never supposed to leave our system.  

My hands moved faster than my brain—I yanked the network cable. The blue glow of the monitor hit my face, and only then did I realize my back was drenched in sweat. Just last week, I’d added an auto-documentation feature to this agent using OpenClaw, and now it was shipping our client’s design specs to some unknown address. I pulled out my phone to message a colleague, but the lock screen showed Fu Sheng’s AI-generated New Year’s greeting on WeChat Moments. The absurdity hit me like a truck.  

Three days later, the vulnerability details finally spread through developer circles. Turns out, OpenClaw versions before 2026.2.25 had a critical flaw: if a user’s browser had the proxy running in the background, visiting a malicious webpage could grant full system access. I was crouched on the conference room floor patching the emergency fix when I heard a loud *"What the hell?!"* from the next cubicle—his customer service bot, trained for three months, was spamming gambling links on Twitter.  

The most surreal part? That same day, GitHub notified me that OpenClaw’s star count had surpassed React’s. 245,000 stars glittered mockingly on the page. I remembered someone at a tech conference last year saying, *"AI frameworks won’t overtake frontend tools in five years."* Now the comments were flooded with *"Times have changed."* After finishing the patch at midnight, I stared at the Tencent Cloud HAI notification in the corner of my screen—their new FlagOS image could deploy a secured OpenClaw with one click. I suddenly burst out laughing. We were all frantically fixing a roof in a storm, only to turn around and see the hardware supplier pulling up with a truckload of materials.  

Fu Sheng’s post actually gave me a boost. His operational data showed eight AI agents completing a month’s worth of work in two weeks—even generating short-video storyboards autonomously. The next day, our CTO dragged the whole team into a meeting. On the projector was a screenshot of our hacked logs, juxtaposed with the engagement metrics from Fu Sheng’s public account. *"Stop obsessing over the vulnerability,"* he said, circling the two graphs with his mouse. *"See this? Even CEOs are editing YAML files by hand now."*  

Last Friday, just before clocking out, the ops guy dropped a link in Slack. It led to Tencent Cloud’s documentation—they’d optimized OpenClaw’s memory usage, squeezing a 196B model into a single server. I was sipping through a straw, skimming the specs, when a whiff of coffee drifted over. *"Don’t bother testing—I already got you beta access."* My manager slapped the credentials on my desk. *"I know what you’re scared of, so…"* He pointed at the HAI console on my screen. *"Sandbox environment. No blame if it explodes."*  

Looking back, February felt like a rollercoaster. At the start of the month, we were laughing at Cheetah Mobile’s hyperbolic press releases. By mid-month, our own project was crippled by a vulnerability. By month-end, we’d rebuilt three test environments using Tencent Cloud’s images. Yesterday, I overheard an intern bragging to his friend: *"We’re working on a 240k-star project now."* It took me back to that 3 AM network cable moment. Maybe this is just the new normal in tech: you never know if tomorrow brings a ban or a place in the history books—but by the time you’re in line at the coffee machine, everyone’s already talking about using AI agents to auto-write weekly reports.