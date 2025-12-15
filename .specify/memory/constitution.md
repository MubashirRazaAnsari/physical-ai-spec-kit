<!--
SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles: All principles replaced with structured constitution format
Added sections: New structured constitution with 9 sections
Removed sections: Previous principles-based constitution
Templates requiring updates:
  - ✅ plan-template.md (constitution checks aligned)
  - ✅ spec-template.md (requirements aligned)
  - ✅ tasks-template.md (task categorization reflects principles)
  - ✅ phr-template.md (governance references updated)
  - ✅ adr-template.md (decision criteria aligned)
Follow-up TODOs: None
-->

# Project Constitution
## Physical AI & Humanoid Robotics — Spec-Kit Plus Project

### 1. Purpose
This project exists to demonstrate disciplined use of the Spec-Kit Plus
workflow by producing a research-grade document on Physical AI and Humanoid
Robotics. The primary goal is process correctness and reproducibility, not
speed or volume of content.

### 2. Scope
The initial deliverable is a single, cohesive research paper written in
Markdown. The paper may later be extended into an AI-native textbook and
interactive system, but those extensions are explicitly out of scope for
the current lifecycle.

### 3. Audience
The intended audience includes:
- Advanced undergraduate and graduate students
- Software engineers transitioning into robotics or Physical AI
- Educators and researchers seeking structured introductory material

Readers are assumed to understand basic programming concepts but not
robotics hardware or control theory.

### 4. Methodology
All work must follow the Spec-Kit Plus lifecycle strictly and sequentially:
- `/sp.constitution`
- `/sp.specify`
- `/sp.clarify`
- `/sp.plan`
- `/sp.tasks`
- `/sp.implement`

No stage may be skipped, merged, or back-filled.

### 5. Content Rules
- No content generation occurs before `/sp.implement`
- All claims must be technically defensible
- Speculative or marketing language is prohibited
- Clarity is prioritized over breadth

### 6. AI Usage Policy
Claude Code acts as a spec-driven collaborator.
- Claude must follow written specifications exactly
- Claude must not introduce unstated assumptions
- Deviations from specs require explicit clarification steps

### 7. Deliverables
- A project constitution
- Formal specifications for the research paper
- A reproducible implementation traceable to specifications

### 8. Constraints
- No proprietary datasets
- No plagiarism
- No external automation that bypasses Spec-Kit stages

### 9. Success Criteria
The project is successful if an independent reviewer can reconstruct
the final paper solely by following the committed specifications and
lifecycle history.

**Version**: 1.1.0 | **Ratified**: 2025-12-15 | **Last Amended**: 2025-12-15
