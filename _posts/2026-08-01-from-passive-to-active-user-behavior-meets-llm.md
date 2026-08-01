---
layout: post
title: "From Passive to Active: When User Behavior Meets Large Language Models"
date: 2026-08-01 09:00:00 +0800
categories: ["AI", "Product", "User Behavior Analytics"]
description: "A former Sensors Data practitioner's take on what large language models actually change in user behavior analytics — and what they don't."
excerpt: "Traditional behavior analytics isn't slow because it can't run in real time. It's slow because the decisions were written into rules ahead of time."
author: Leoo Bai
---

# From Passive to Active: When User Behavior Meets Large Language Models

During my years at Sensors Data, my team and I spent our days working with events, properties, funnels, and retention.

A user opens the app, looks at a product, checks the specs, then backs out to the list. We collect these actions, string them into a behavior sequence, and dig through a pile of charts to figure out why they didn't buy. Technically, this can be done fast — Sensors Data's analytics products have long supported sub-second queries, and operations systems can already trigger actions automatically based on segments.

So calling traditional user behavior analytics "you can only check the report the next day" isn't accurate.

What's actually passive about it is that **the decisions are usually written in stone ahead of time**.

If a user keeps checking a product but doesn't buy, send a coupon. If they haven't logged in for a while, push a win-back message. If they keep browsing a certain type of content, tag them. The data can arrive in real time, and the system can run in real time — but it only ever executes rules someone drew up beforehand. The system has no idea why the user is hesitating.

Once large language models enter the picture, this is the layer worth watching.

## It doesn't read minds. It just guesses one step further.

Take that same user comparing products.

A traditional system sees a string of events: viewed A, viewed B, expanded the specs, read the negative reviews, left. A large model can put event names, product information, page content, and historical behavior together and offer a few candidate explanations: maybe they're comparing battery life, maybe they're worried about after-sales service, or maybe they're just browsing.

Notice the word "maybe."

Clicking repeatedly on a technical spec sheet doesn't mean the user is anxious. A long dwell time might just mean they stepped away to take a phone call. Behavioral data has never been a recording of someone's inner state — a large model is just better than the old tagging rules at organizing clues. If you turn that guess directly into "the system has detected the user is torn," that's still the same old AI bluster, just wearing a UBA costume this time.

The useful move is to let the model keep narrowing the question down, instead of declaring the answer on the user's behalf. Show a short comparison summary of the two products, or ask, "Are you more concerned about battery life or after-sales service?" The user's next action becomes the new evidence.

At that point, behavior analytics stops being a rearview mirror and becomes a navigation screen next to the wheel — but the person is still in the car, and you don't rip out the brakes.

## The rule canvas isn't disappearing. It's just moving.

In the old days of marketing automation, an operator would draw out the whole flow first: who qualifies, under what condition, what content gets sent, how long to wait, what happens next.

An agent can turn part of that into an on-the-spot decision. The operator no longer draws a complete route — they just give it a goal and a boundary, something like: "Help enterprise customers who are comparing plans find the information they're missing. Don't initiate discounts. Don't message unauthorized channels." The model looks at the behavior and context in the moment and chooses to look something up, generate an explanation, or do nothing at all.

That last option matters a lot.

A lot of agent demos today have a bad habit: the moment a model can call a tool, it wants to use it every single time. But the most dangerous thing an operations system can do usually isn't failing to reach out — it's reaching out wrong. A user just finished complaining about a privacy issue, and the system turns around and sends them a "you might also like" message based on their browsing history. That's not being proactive. That's rubbing salt in the wound.

So the old rules haven't gone away. They've shifted from "dictate every single step" to "dictate which roads are absolutely off-limits." Permissions, frequency caps, privacy consent, pricing policy, and human approval should all sit outside the model, guarding it. You can't let a large model come up with the idea and approve its own execution at the same time.

## Raw tracking data can't feed a smart agent

Another problem that's easy to overlook is data semantics.

`click_btn_01` is just as unfriendly to a model as it is to a new analyst. Even if you rename the event to `compare_product`, if the model doesn't know which two products were being compared, what the page was showing at the time, whether the user was logged in, or whether the data even belongs to the same person, it's still just guessing.

Dumping all your logs into the context window doesn't help. A large model needs a layer that explains the business: who, in what scenario, acting on what object, doing what, with what result. The Event + User model that Sensors Data has always emphasized hasn't gone stale here — if anything, it's become the foundation for whether an agent can understand behavior at all.

But the foundation alone isn't enough. On top of it you still need product, content, order, entitlement, and policy context, plus identity resolution, data freshness, and permissions. If the tracking was implemented wrong, the model can't cast a spell to fix it. When definitions conflict, it might even pick whichever wrong answer looks most convincing.

## Dashboards aren't going anywhere, and A/B testing won't turn into automated gambling

The original piece I was reacting to made two tempting claims: dashboards will turn into agent plugins, and A/B testing will turn into a model auto-eliminating hundreds of strategies every millisecond.

The first one is plausible. The second one — let's not get ahead of ourselves.

Agents really can call analytics tools, drilling down, querying segments, and explaining metrics in natural language. A manager doesn't have to click through every filter by hand anymore. But the charts aren't going to disappear because of that. When the model says "the drop in conversion might be related to page latency," a person still needs to look at the trend, the sample size, the segmentation, and the raw data to make sure it isn't mistaking correlation for causation.

The same goes for A/B testing. Large models are good at generating candidate copy and page variants; the experimentation platform is responsible for traffic allocation, metrics, and significance testing. Letting a model see a bit of real-time noise and immediately change strategy is a good way to mistake randomness for a signal — you end up chasing every little wobble.

I trust a less exciting version of this: the model's job is to come up with more candidate ideas, and the job of humans plus the experiment system is to keep the bad ones from running wild.

## From Sense to Action, there's now something in the middle that reasons

Sensors Data's public materials describe a `Sense → Decision → Action → Feedback` loop: sense the data, make a decision, execute an action, then use the feedback to correct the next round.

In the past, the Decision step in that loop was mostly done by analysts and operators, while the system just fed the data up and executed whatever strategy had already been written. The opportunity for large models is to step into that Decision layer, and even help orchestrate part of the Action.

But it hasn't brought data "to life," and it hasn't ended behavior analytics. It's just given a new way to implement the work that used to sit between the dashboard and the marketing canvas, done in someone's head.

What user behavior systems will actually be competing on next probably isn't who has one more chart or one more agent button. It's three things: giving the model accurate enough context, keeping its guesses clearly separated from facts, and keeping its actions locked inside a reliable permission boundary.

Miss one of those, and "being proactive" turns into "acting out."

References:

- [Sensors Data: Event Model and User Behavior Analytics](https://manual.sensorsdata.cn/sa/docs/access_prepare/v0204)
- [Sensors Data: User Behavior Sequence](https://manual.sensorsdata.cn/sa/docs/guide_analytics_users_sequence/v0300)
- [Sensors Data: Sense, Decision, Action, Feedback](https://sensorsdata.cn/uploads/bac0bfdd49e38c9c941fc556170ec20f/%E9%93%B6%E8%A1%8C_4.0_%E6%95%B0%E5%AD%97%E5%8C%96%E8%BF%90%E8%90%A5%E4%BD%93%E7%B3%BB%E6%9E%84%E5%BB%BA%E7%9A%84%E6%96%B9%E6%B3%95%E4%B8%8E%E5%AE%9E%E8%B7%B5.pdf)
