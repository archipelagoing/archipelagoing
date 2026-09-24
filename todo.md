a file i include in most of my repos now, to make sure my repo is as organized as possible and i can maintain my context

# Repo TODO

## 1. CoalitionMind 🧠

**Goal:** Turn the small cognitive-architecture prototype into a measurable multi-agent experiment.

**Why:** The core idea is already strong: specialized internal agents negotiate over shared memory to produce behavior. The biggest opportunity is proving what interesting behavior actually emerges.

- [ ] Split prototype into `agents/`, `memory/`, `graph/`, `policy/`, `simulation/`
- [ ] Build repeated-decision simulation
- [ ] Log agent scores, weights, decisions, rewards
- [ ] Plot agent weights over time
- [ ] Run agent-ablation experiments
- [ ] Add reproducible experiment script + seeds
- [ ] Add results + plots to README

---

## 2. CognitiveRoutingDegradation 🔀

**Goal:** Turn the research premise into an experiment about how multi-agent systems compensate for failures.

**Why:** This could connect multi-agent AI, routing, interpretability, network resilience, and causal intervention in one project.

- [ ] Implement 4–6 specialist agents
- [ ] Implement task router
- [ ] Establish healthy-network baseline
- [ ] Add node/connection/memory degradation
- [ ] Measure accuracy + routing changes
- [ ] Measure specialist substitution after failures
- [ ] Visualize routing network before/after degradation
- [ ] Add results to README

---

## 3. DialogLace / LongTermMemoryLLM 🧵

**Goal:** Turn basic vector memory into an experimental structured-memory architecture.

**Why:** Embedding retrieval alone is common. Comparing vector, graph, and hybrid memory would give the project a much stronger technical contribution.

- [ ] Restore end-to-end FastAPI + ChromaDB pipeline
- [ ] Add timestamps, topics, entities, conversation IDs
- [ ] Build conversation-memory graph
- [ ] Add semantic + temporal + entity edges
- [ ] Implement hybrid vector + graph retrieval
- [ ] Create memory-recall benchmark
- [ ] Compare vector vs graph vs hybrid retrieval
- [ ] Add benchmark results to README

---

## 4. Transcript-Analyzer 📺

**Goal:** Turn the original idea into a real NLP / computational social science study.

**Why:** Children's television gives you an unusual dataset for studying how language communicates emotion, relationships, morality, and other important concepts.

- [ ] Define one concrete research question
- [ ] Collect transcripts from 2–3 children's shows
- [ ] Create standardized transcript dataset
- [ ] Compute vocabulary + lexical complexity metrics
- [ ] Define concept groups: emotion, friendship, conflict, family, morality
- [ ] Compare concepts using embeddings
- [ ] Add cross-show / cross-decade visualizations
- [ ] Rewrite README around findings

---

## 5. CAFA6 🧬

**Goal:** Turn the repository into a credible protein-function prediction ML project.

**Why:** Bioinformatics adds useful domain breadth to the portfolio, but the current README contains unrelated ecommerce material and needs to accurately reflect the implementation first.

- [ ] Remove accidental ecommerce content from README
- [ ] Document actual CAFA6 dataset + pipeline
- [ ] Implement reproducible baseline
- [ ] Add proper train/validation split
- [ ] Record baseline metrics
- [ ] Implement one improved model/representation
- [ ] Compare improved model against baseline
- [ ] Add pipeline diagram + results table

---

## 6. HTTPS-Server 🔐

**Goal:** Turn an undocumented systems project into evidence of networking and low-level engineering ability.

**Why:** Most of the portfolio is AI/data focused. A well-documented HTTPS implementation shows that you understand what happens underneath higher-level frameworks.

- [ ] Write actual README
- [ ] Document build/run instructions
- [ ] Add client → TLS → HTTP → response architecture diagram
- [ ] Add example requests/responses
- [ ] Add HTTP parsing tests
- [ ] Test malformed requests
- [ ] Document TLS/certificate handling
- [ ] Benchmark concurrent requests

---

## 7. HobokenEats 🍜

**Goal:** Turn the early API experiment into a complete local-data collection and visualization pipeline.

**Why:** The interesting part is not another restaurant dashboard. It is demonstrating API collection, geographic data cleaning, deduplication, analysis, and visualization end-to-end.

- [ ] Replace naive restaurant search with geographic collection
- [ ] Deduplicate restaurants
- [ ] Create clean CSV/JSON dataset
- [ ] Collect cuisine, rating, price, coordinates, review count
- [ ] Connect cleaned data to Power BI
- [ ] Add geographic visualization
- [ ] Document data coverage limitations

---

## 8. EvoNashMTL ⚖️

**Goal:** Determine whether evolutionary scheduling actually improves Nash-based multi-task learning.

**Why:** The method already exists. More features matter less now than strong baselines, ablations, repeated experiments, and interpretable results.

- [ ] Finish baseline experiment suite
- [ ] Run equal-weight baseline
- [ ] Run Nash-MTL baseline
- [ ] Run replicator-only baseline
- [ ] Run EvoNashMTL
- [ ] Repeat across multiple seeds
- [ ] Plot task weights over training
- [ ] Plot per-task performance
- [ ] Run scheduler ablation
- [ ] Create final comparison table

---

## 9. NormViz 🔔

**Goal:** Polish an already focused educational statistics tool.

**Why:** The project already communicates one idea clearly. Improvements should increase usability and reliability rather than broaden its scope.

- [ ] Add real-world presets
- [ ] Add statistics/edge-case tests
- [ ] Add shareable parameterized URLs
- [ ] Add expandable math explanation
- [ ] Run mobile + accessibility audit
- [ ] STOP adding unrelated features

---

## 10. PCACloud ☁️

**Goal:** Polish and maintain an already strong mathematical visualization product.

**Why:** PCACloud already has a clear identity, live demo, mathematical documentation, tests, and polished README. Protect that focus.

- [ ] Add 2–3 built-in datasets
- [ ] Add categorical point coloring
- [ ] Add original-row hover tooltips
- [ ] Add reproducible/shareable settings
- [ ] Benchmark large CSV performance
- [ ] Verify demo + tests + docs
- [ ] STOP feature creep

---

# Priority Queue

- [ ] **CoalitionMind:** prototype → experiment
- [ ] **CognitiveRoutingDegradation:** premise → prototype
- [ ] **DialogLace:** vector memory → structured memory experiment
- [ ] **Transcript-Analyzer:** idea → NLP study
- [ ] **CAFA6:** repair → credible ML experiment
- [ ] **EvoNashMTL:** prototype → validated research
- [ ] **HTTPS-Server:** implementation → documented systems project
- [ ] **HobokenEats:** exploration → complete data pipeline
- [ ] **NormViz:** polish only
- [ ] **PCACloud:** polish only

---

# Overall Portfolio Direction

## 🧅 Representation & Interpretability

**Projects:** Situationion / Onion

Study what neural models represent internally and how those representations change across layers, contexts, and interventions.

**Direction:** stronger experiments, controls, activation patching, adversarial cases, quantitative results.

---

## 🧠 Adaptive & Collective Intelligence

**Projects:** EvoNashMTL · CoalitionMind · CognitiveRoutingDegradation · DialogLace

Explore systems where intelligence emerges from interacting components: competing tasks, specialized agents, routing systems, memory structures, and adaptive decision policies.

**Direction:** simulations, ablations, controlled interventions, measurable emergent behavior.

---

## 📊 Mathematical ML Visualization

**Projects:** PCACloud · NormViz

Turn mathematical and statistical concepts into interactive systems people can understand visually.

**Direction:** polish, usability, mathematical correctness, educational clarity. Avoid feature creep.

---

## 🏠 Human-Facing AI / Software Products

**Projects:** Planoramic · Tenue

Build unusual consumer-facing products where the underlying technology serves a clear human experience.

**Direction:** deployment, integrations, UX, real users, demos, reliability.

---

## 🔐 Systems & Engineering Breadth

**Projects:** HTTPS-Server · elastic-benchmarking · networking/security work

Demonstrate engineering ability below the ML/application layer.

**Direction:** testing, benchmarking, concurrency, architecture documentation, reproducibility.

---

# Portfolio Thesis

> **Build systems that make complex intelligence, data, and mathematical structure observable, interactive, and understandable.**

Across projects, prioritize:

- [ ] Clear research/product question
- [ ] Working implementation
- [ ] Reproducible experiments
- [ ] Baselines
- [ ] Ablations
- [ ] Quantitative results
- [ ] Strong visualizations
- [ ] Tests
- [ ] Live demos when appropriate
- [ ] README that explains **problem → method → experiment → result**
- [ ] Archive/de-emphasize projects that do not support the portfolio direction
- [ ] Build depth in existing strong ideas before starting more repos
