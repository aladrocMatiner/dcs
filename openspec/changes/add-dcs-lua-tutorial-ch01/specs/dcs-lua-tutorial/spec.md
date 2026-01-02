## ADDED Requirements

### Requirement: Four-language DCS Lua tutorial structure
The project MUST provide a DCS Lua tutorial in Markdown with English, Spanish, Swedish, and Finnish versions, using consistent file naming and link-localized navigation.

#### Scenario: Language files exist and are navigable
- **GIVEN** the tutorial exists under `docs/dcs-lua/`
- **WHEN** a reader opens any language version
- **THEN** they can navigate to the other three languages via a single-line language bar
- **AND** links are relative and point to the matching language file when it exists

### Requirement: Chapter 01 teaches DCS Lua runtime basics
Chapter 01 MUST be introductory and conceptual. It MUST explain DCS mission scripting at a high level (what scripting is, why DCS uses Lua), what kinds of problems Lua scripting can solve in DCS, and where Lua runs in DCS (Mission Editor triggers) without focusing on code.

#### Scenario: Reader understands what Lua scripting enables
- **GIVEN** a user is new to DCS mission scripting
- **WHEN** they read Chapter 01
- **THEN** they understand why DCS uses Lua for mission scripting at a high level
- **AND** they understand where Lua runs in DCS (Mission Editor triggers such as `DO SCRIPT` / `DO SCRIPT FILE`)
- **AND** they can describe multiple conceptual examples of what can be scripted (events, messages, AI activation, state/flags, zones, timers)
- **AND** they understand the basic mindset for validating behavior (“did it run?”) and common mistakes to avoid

### Requirement: One OpenSpec change per tutorial chapter
Each tutorial chapter MUST be delivered as its own OpenSpec change to keep review and iteration small and incremental.

#### Scenario: Future chapter additions remain incremental
- **GIVEN** Chapter 01 exists
- **WHEN** a new chapter is added
- **THEN** it is proposed and implemented via a separate change (e.g., `add-dcs-lua-tutorial-ch02`)
- **AND** the index is updated in all four languages as part of that chapter change
