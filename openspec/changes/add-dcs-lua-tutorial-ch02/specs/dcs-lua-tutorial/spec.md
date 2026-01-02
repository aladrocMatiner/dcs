## ADDED Requirements

### Requirement: Chapter 02 explains the DCS Lua workflow pipeline
Chapter 02 MUST teach an introductory, practical workflow for DCS mission scripting using Visual Studio Code, focused on how people work day-to-day (authoring, packaging, running in DCS, verifying, iterating).

#### Scenario: Reader understands the end-to-end workflow
- **GIVEN** a reader wants to start mission scripting
- **WHEN** they read Chapter 02
- **THEN** they can describe a simple pipeline from editing in VS Code to running and verifying the result in DCS
- **AND** they understand the purpose of each step (author → package → run → observe → iterate)

### Requirement: Chapter 02 clarifies what must be installed
Chapter 02 MUST clarify that DCS includes the Lua runtime used for mission execution, and that local installations are optional tooling for authoring (editor support, formatting, offline experiments).

#### Scenario: Reader does not confuse runtime vs tooling
- **GIVEN** a reader is unsure whether they must “install Lua”
- **WHEN** they read Chapter 02
- **THEN** they understand that running scripts in DCS does not require installing Lua separately
- **AND** they understand what optional local tools are for (VS Code language server, optional Lua interpreter)

### Requirement: Chapter 02 introduces common DCS Lua libraries/frameworks
Chapter 02 MUST introduce commonly used DCS Lua libraries/frameworks and what they are used for, in a conceptual and didactic way (not code-heavy), so the reader can decide what ecosystem to explore next.

#### Scenario: Reader can choose a library direction
- **GIVEN** a reader wants to build more complex missions
- **WHEN** they read Chapter 02
- **THEN** they can explain at a high level what MOOSE and MIST are used for
- **AND** they can list several example use cases that libraries enable (events/flow, state/scoring, AI activation, zones/timers)
- **AND** they understand basic trade-offs (complexity, maintenance, dependency management)
