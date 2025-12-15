---
id: 2
title: Update Physical AI Constitution
stage: constitution
date: 2025-12-15
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: mubashir
command: /sp.constitution
labels: [constitution,spec-kit,physical-ai,update]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - history/prompts/constitution/002-update-physical-ai-constitution.constitution.prompt.md
tests:

---

## Prompt

update it with this new constitution # Project Constitution
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

## Response snapshot

The constitution file has been successfully updated with the new structured format. The changes include:

- Version updated from 1.0.0 to 1.1.0 (reflecting significant content changes)
- Complete replacement of the previous principles-based constitution with the new structured 9-section format
- Updated Sync Impact Report reflecting the changes
- All content now follows the specified format with sections for Purpose, Scope, Audience, Methodology, Content Rules, AI Usage Policy, Deliverables, Constraints, and Success Criteria

The updated constitution properly reflects the Spec-Kit Plus workflow requirements and the specific needs of the Physical AI & Humanoid Robotics project.

## Outcome

- ✅ Impact: Updated constitution to new structured format at .specify/memory/constitution.md
- 🧪 Tests: No tests required for constitution update
- 📁 Files: Updated constitution file and created PHR record
- 🔁 Next prompts: /sp.specify to create the feature specification
- 🧠 Reflection: Constitution now properly structured with 9 defined sections as requested

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create feature specification using /sp.specify