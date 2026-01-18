# Resume Feedback System

An **intelligent, explainable AI system** that analyzes a resume against a job
description and provides structured feedback using **hybrid AI techniques**.

Developed as part of an **Artificial Intelligence Lab**, focusing on knowledge
representation, reasoning, and explainability.

---

## Features

- Skill extraction from unstructured text
- Skill normalization using canonical symbols (e.g., NLP → `nlp`)
- Hierarchical skill ontology (NLP ⊂ Machine Learning)
- Ontology-based reasoning (full / partial / missing skills)
- Semantic similarity using pretrained SentenceTransformer
- Explainable, human-readable feedback
- Coverage calculation with partial matches

---

## Approach

The system follows a **hybrid AI architecture**:

1. **Lexical Layer** – Extracts surface skill mentions
2. **Normalization Layer** – Maps skills to canonical ontology symbols
3. **Knowledge Representation Layer** – Skill ontology
4. **Reasoning Layer** – Rule-based inference
5. **Semantic Evidence Layer** – Embedding-based similarity
6. **Explanation Layer** – Transparent feedback generation

> The project emphasizes **explainable AI** rather than black-box learning.

---

## Technology Stack

- Python
- Regular Expressions
- SentenceTransformer
- Rule-based reasoning
- Knowledge representation (ontology)
- Git

---

## Project Status

- Milestone 1: Rule-based baseline
- Milestone 2: Skill normalization and suppression
- Milestone 3: Ontology-based reasoning
- Milestone 4: Hybrid semantic reasoning

**Current State:** Core AI system complete and stable.

---

## Notes

- This is **not** a pure machine learning project
- No model training is performed
- Focus is on symbolic reasoning and explainability

---

## Author

Developed as part of an academic AI lab project.
