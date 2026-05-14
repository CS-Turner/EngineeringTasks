# Waystar | Evaluations — Opik Demo

An interactive prototype of the [Opik](https://www.comet.com/site/products/opik/) evaluation interface, built for the **Evals for the Omnichannel Billing Agent** working session (May 2026). It demonstrates what AI evaluation looks like in practice using realistic billing agent conversations drawn from the Waystar engagement.

---

## What's in this repo

| File | Description |
|------|-------------|
| `waystar-opik-demo-v2.html` | **Main demo** — focused on Intent Detection and Cost per Interaction (use this one) |
| `waystar-opik-demo.html` | Earlier version — full Opik project overview (Datasets, Experiments, Annotation Queue) |

---

## How to open the demo

The demo is a self-contained HTML file — no server, no login, no installation required.

1. Download `waystar-opik-demo-v2.html` from this repo (click the file → **Download raw file**)
2. Double-click the downloaded file — it opens in your default browser (Chrome or Safari work best)
3. That's it

---

## What the demo shows

The demo mirrors the Opik evaluation UI for the `waystar-eval-demo` project. It has three tabs:

### 🎯 Intent Detection
Shows how the billing agent is scored on whether it correctly identified what a patient wanted before responding. Uses an **LLM-as-Judge** approach — a second AI model reads each conversation and scores how well the agent's interpretation matched the patient's actual intent.

- The table lists 9 billing conversations with their ground-truth intent, the agent's parsed intent, and a judge score out of 10
- **"Show misfires only"** filters to the cases where the agent got it wrong — the most important ones to review
- Click any row to open a detail panel showing the full conversation, the judge's reasoning, and the token cost breakdown for that interaction

The three misfires in the demo (ws-004, ws-007, ws-009) each illustrate a different failure mode: a payment dispute misread as a routine balance inquiry, a billing dispute met with an explanation instead of escalation, and a claim rejection routed to the wrong workflow.

### 💰 Cost per Interaction
Shows the unit economics of running the billing agent at scale.

- **Cost by intent** — more complex intents (payment disputes) cost more per conversation than simple ones (account balance)
- **Model comparison** — trade-off between accuracy and cost across GPT-4o, GPT-4o mini, Claude Sonnet, and Claude Haiku
- **Cost at scale** — projects monthly LLM spend from 1K to 500K conversations; at an estimated 50K/month the cost is ~$300
- Click any row in the per-conversation table for a full input/output token breakdown

### ✏️ Annotation Queue
Shows the human review workflow for conversations the automated eval flagged as uncertain. Each item in the queue is a misfire that needs a human judgment call: Acceptable, Needs Edit, or Fail. Submitting an annotation removes the item from the queue and feeds back into calibrating the LLM judge.

---

## How this connects to the session

During the **Building Custom Evals for AI Alignment** breakout, this demo is used as an orientation before participants work in the live Opik environment:

1. **Intent Detection tab** — illustrates the LLM-as-judge concept before Activity 2 (metric identification)
2. **Cost per Interaction tab** — grounds the cost metric discussion in real numbers
3. **Annotation Queue tab** — shows what the annotation exercise looks like before participants use the real Opik queue

The live Opik annotation queue for the session is at:
`https://www.comet.com/opik/waystar-eval-demo/sme?queueId=019e2448-3939-72cf-b239-cd47a287f205`

---

## Questions

Reach out to [charity.turner@fractional.ai](mailto:charity.turner@fractional.ai) or [varun@fractional.ai](mailto:varun@fractional.ai).
