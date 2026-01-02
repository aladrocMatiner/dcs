## ADDED Requirements

### Requirement: Four-language DCS Lua tutorial structure
The project MUST provide a DCS Lua tutorial in Markdown with English, Spanish, Swedish, and Finnish versions, using consistent file naming and link-localized navigation.

#### Scenario: Language files exist and are navigable
- **GIVEN** the tutorial exists under `docs/dcs-lua/`
- **WHEN** a reader opens any language version
- **THEN** they can navigate to the other three languages via a single-line language bar
- **AND** links are relative and point to the matching language file when it exists

### Requirement: Chapter 01 teaches DCS Lua runtime basics
Chapter 01 MUST focus on DCS mission scripting fundamentals: where Lua runs, how to execute scripts in the Mission Editor, and how to verify execution.

#### Scenario: Reader can run and verify a minimal script
- **GIVEN** a user has a mission in the DCS Mission Editor
- **WHEN** they follow Chapter 01 to add a minimal script (e.g., `trigger.action.outText`)
- **THEN** they can verify the script executed in-mission (on-screen message) and know where to debug common errors

### Requirement: One OpenSpec change per tutorial chapter
Each tutorial chapter MUST be delivered as its own OpenSpec change to keep review and iteration small and incremental.

#### Scenario: Future chapter additions remain incremental
- **GIVEN** Chapter 01 exists
- **WHEN** a new chapter is added
- **THEN** it is proposed and implemented via a separate change (e.g., `add-dcs-lua-tutorial-ch02`)
- **AND** the index is updated in all four languages as part of that chapter change
