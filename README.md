# Enterprise-Grade Stateful AI Terminal with Context Memory

An optimized, lightweight Python implementation that transforms a natively stateless Large Language Model (LLM) into a stateful, interactive conversational terminal. This architecture implements a client-side in-memory state loop, an input validation guard rail, and a first-in-first-out (FIFO) sliding window memory manager using the modern Google GenAI SDK.

## 🚀 Key Architectural Pillars

This framework segregates execution from inference, enforcing strict data isolation and reliability through three engineered core layers:

1. **Structural Input Validation Gate:** An explicit programmatic conditional guard evaluating all incoming data. It blocks empty strings or whitespace-only payloads before network dispatch, systematically eliminating downstream `HTTP 400 Bad Request` API transaction crashes.
2. **Stateful In-Memory Ingestion Layer:** Manages conversation continuity independently of the stateless API endpoint. Every interaction is mapped dynamically to a serialized array of role-content schemas matching strict Pydantic structural expectations.
3. **Sliding Window Memory Manager (FIFO Pruning):** Mitigates the physical constraints of token exhaustion and context window overflow. The algorithm monitors in-memory array thresholds and applies rolling truncation to discard the oldest message pairs, safeguarding the token budget during extended runtimes.

---

## 🛠️ Technical Stack & Frameworks

* **Core Runtime:** Python 3.11+
* **Orchestration Client:** Google GenAI SDK (`google-genai`)
* **Frontier Model Engine:** `gemini-2.5-flash`

---

## 💻 Code Structure & Implementation

The repository contains a unified executable pipeline (`chatbot.py`) implementing the following execution flow:

* **Ingest & Validate:** CLI ingestion coupled with whitespace sanitization.
* **Append & Prune:** Local state array processing using custom FIFO truncation limits.
* **Transmit & Record:** Asynchronous-ready transaction processing wrapped inside resilient exception-handling blocks (`try-except`) with safe-state rollbacks upon network dropouts.

---

## ⚙️ Quick Start Guide

### 1. Prerequisites
Ensure you have the latest packages installed via your package manager:
```bash
pip install google-genai
```

### 2. Environment Configuration
To safeguard against hardcoded credential leakage, replace the placeholder token or export your credentials:
```python
API_KEY = "YOUR_API_KEY_HERE"
```

### 3. Execution
Run the conversational terminal shell:
```bash
python chatbot.py
```

### 4. Verification Framework (The Memory Exam)
To audit the integrity of the sliding window state mechanism, execute this 3-phase test sequence:
1. **State Initialization:** Provoke acknowledgment (`"My name is Fazeel"`).
2. **Context Distraction:** Trigger high-volume generation (`"Write a poem about coding"`) to stress-test token buffers.
3. **State Extraction:** Evaluate historical recall (`"What is my name?"`). The model will successfully query the sliding matrix to return the exact identity state.

---
*Developed under the Generative AI Core Track Architecture Framework - Batch 2026 | Powered by DecodeLabs.*
