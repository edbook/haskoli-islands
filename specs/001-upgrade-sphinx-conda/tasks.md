# Tasks: Upgrade Sphinx and Conda to Latest Versions

**Input**: Design documents from `/specs/001-upgrade-sphinx-conda/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, quickstart.md

**Tests**: No automated tests requested. Validation is via manual Sphinx builds and CI pipeline runs.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Repository root**: `environment.yml` (primary change target)
- **Projects**: `projects/*/conf.py` (potential fixes)
- **CI workflows**: `.github/workflows/` (updated: Python version, conda upgrade step, Sphinx `-D` flags)

---

## Phase 1: Setup (Baseline Recording)

**Purpose**: Capture current state metrics before making any changes

- [x] T001 Record current Conda environment solve time by running `time mamba env create -f environment.yml --dry-run` — SKIPPED: conda not available in shell; CI will validate
- [x] T002 Record current CI build time from most recent successful workflow run on main branch via GitHub Actions UI — **Baseline: Build=2m41s, Deploy=2m18s, Total=~5m32s** (run ID 21955715737)
- [x] T003 Build `projects/forsida` with current Sphinx 6.x as baseline reference: `sphinx-build -b html projects/forsida _build/baseline-forsida` — SKIPPED: conda not available in shell

---

## Phase 2: Foundational (Version Pin Updates)

**Purpose**: Update `environment.yml` with new version pins — MUST be complete before any build testing

**CRITICAL**: No build testing can begin until this phase is complete

- [x] T004 Update Python version pin from `3.10.*` to `3.13.*` in `environment.yml`
- [x] T005 Update Sphinx version pin from `6.*` to `8.*` in `environment.yml`
- [x] T006 Update sphinx-rtd-theme version pin from `1.2.*` to `3.*` in `environment.yml`
- [x] T007 Update sphinx-autobuild from `2021.3.14` to unpinned (remove version pin) in `environment.yml`
- [x] T008 Update sphinx-copybutton from `0.5.1` to `0.5.2` in `environment.yml` (pip section)
- [x] T009 Update pip version pin from `23.*` to unpinned (remove version pin) in `environment.yml`
- [ ] T010 Remove and recreate Conda environment from updated `environment.yml`: `conda env remove -n edbook && mamba env create -f environment.yml` — MANUAL: requires local conda/mamba
- [ ] T011 Verify environment resolves without dependency conflicts and record new Conda solve time — MANUAL: requires local conda/mamba

**Checkpoint**: Fresh Conda environment created with Sphinx 8.x, Python 3.13, and all updated packages

---

## Phase 3: User Story 1 - Maintainer Upgrades Build Environment (Priority: P1) MVP

**Goal**: All 18 project directories build successfully with upgraded Sphinx and Python

**Independent Test**: Run `sphinx-build` on every project directory and verify zero build errors

### Implementation for User Story 1

- [ ] T012 [US1] Smoke test: build `projects/forsida` with upgraded Sphinx: `sphinx-build -b html -j auto projects/forsida _build/forsida` — DEFERRED TO CI: no local conda
- [ ] T013 [US1] Build all 18 project directories and capture output: `for p in projects/*/; do sphinx-build -b html -j auto -q "$p" "_build/$(basename $p)" 2>&1; done` — DEFERRED TO CI: no local conda
- [x] T014 [US1] Review build output and categorize any warnings as breaking/cosmetic/informational — Proactive scan of all conf.py files for Sphinx 8 deprecation patterns
- [x] T015 [US1] Fix any breaking deprecation warnings in `projects/*/conf.py` files — Fixed: `master_doc`→`root_doc` in settings.py, python/conf.py, rei201g/conf.py; `intersphinx_mapping` format in python/conf.py, rei201g/conf.py; cleaned merge conflict marker in python/conf.py
- [ ] T016 [US1] Re-run full build of all 18 projects to confirm zero errors after fixes — DEFERRED TO CI: no local conda
- [ ] T017 [US1] Verify `sphinx-autobuild` works for local development: `sphinx-autobuild projects/forsida _build/forsida-live` — DEFERRED TO CI: no local conda

**Checkpoint**: All 18 projects build successfully locally. Local development workflow (autobuild) confirmed working.

---

## Phase 4: User Story 2 - CI Pipeline Continues Working (Priority: P1)

**Goal**: PR and push CI workflows complete successfully with upgraded dependencies

**Independent Test**: Open a PR and verify the GitHub Actions workflow completes with green status

**Dependency**: Requires US1 completion (local builds must pass before CI testing)

### Implementation for User Story 2

- [x] T018 [US2] Commit updated `environment.yml` (and any `conf.py` fixes) with conventional commit message — cb13511
- [x] T019 [US2] Push `001-upgrade-sphinx-conda` branch to remote and open a pull request — PR #225
- [ ] T020 [US2] Verify PR workflow (`build-docs-optimized.yml`) completes successfully in GitHub Actions
- [ ] T021 [US2] Verify preview deployment renders correctly at the PR preview URL
- [ ] T022 [US2] Compare CI build time against baseline recorded in T002 — must be within 125% of baseline (SC-002)
- [ ] T023 [US2] Compare Conda solve time in CI against baseline — must be within 150% of baseline (SC-004)

**Checkpoint**: CI pipeline fully green. Build times within acceptable range.

---

## Phase 5: User Story 3 - Sphinx Extensions Remain Compatible (Priority: P2)

**Goal**: All custom and third-party Sphinx extensions produce correct output with upgraded Sphinx

**Independent Test**: Build projects that use specific extensions and verify HTML output contains expected elements

**Dependency**: Requires US1 completion (projects must build before output can be inspected)

### Implementation for User Story 3

- [ ] T024 [P] [US3] Verify `sphinxcontrib-katex` math rendering: build a project using katex (e.g., `projects/stae104g`) and check HTML output contains rendered math elements
- [ ] T025 [P] [US3] Verify `sphinxcontrib-questionnaire` interactive elements: build a project using questionnaire and check HTML output contains questionnaire widgets
- [ ] T026 [P] [US3] Verify `sphinxcontrib-geogebra` embeds: build a project using geogebra and check HTML output contains GeoGebra applet elements
- [ ] T027 [P] [US3] Verify `sphinxcontrib-sagecell` interactive code: build a project using sagecell and check HTML output contains SageCell elements
- [ ] T028 [P] [US3] Verify `sphinxcontrib-youtube` video embeds: build a project using youtube extension and check HTML output contains video embed elements
- [ ] T029 [US3] Verify `sphinx-rtd-theme` 3.x visual rendering: compare `_build/forsida/index.html` against baseline from T003 — check navigation, sidebar, footer, responsive layout
- [ ] T030 [US3] Verify `sphinx-versioned-docs` multi-version build still works: run `sphinx-versioned-docs build projects/forsida _build/forsida-versioned` and confirm the output contains a version selector dropdown in the HTML

**Checkpoint**: All extensions confirmed working. Theme renders correctly. No visual regressions.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup across all user stories

- [ ] T031 Run quickstart.md validation: follow all steps in `specs/001-upgrade-sphinx-conda/quickstart.md` on a fresh environment to confirm instructions are accurate
- [ ] T032 Document any visual differences from sphinx-rtd-theme upgrade in the PR description
- [ ] T033 Verify all 9 custom edbook extensions load without deprecation warnings: build `projects/stae104g` (uses most extensions) with `sphinx-build -b html projects/stae104g _build/stae104g 2>&1 | grep -i 'deprecated\|WARNING'` and confirm no extension-related warnings
- [ ] T034 Final review: confirm all success criteria (SC-001 through SC-005) are met

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: No dependency on Phase 1 output (baseline metrics are informational), but logically follows it
- **US1 (Phase 3)**: Depends on Foundational (Phase 2) — needs updated environment
- **US2 (Phase 4)**: Depends on US1 (Phase 3) — local builds must pass before CI testing
- **US3 (Phase 5)**: Depends on US1 (Phase 3) — needs successful builds to inspect output. Can run in parallel with US2.
- **Polish (Phase 6)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) — no dependencies on other stories
- **User Story 2 (P1)**: Depends on US1 — cannot test CI if local builds fail
- **User Story 3 (P2)**: Depends on US1 — can run in parallel with US2

### Parallel Opportunities

- **Phase 1**: T001, T002, T003 can run in parallel (independent baseline measurements)
- **Phase 2**: T004–T009 are all edits to the same file (`environment.yml`) — must be sequential or batched as a single edit
- **Phase 3**: T012 must precede T013 (smoke test before full build)
- **Phase 5**: T024–T028 can ALL run in parallel (different extensions, different project outputs)
- **Phase 4 and Phase 5**: Can run in parallel after US1 completes

---

## Parallel Example: User Story 3

```bash
# Launch all extension verifications together (after US1 builds complete):
Task: "Verify sphinxcontrib-katex math rendering in projects/stae104g output"
Task: "Verify sphinxcontrib-questionnaire widgets in project output"
Task: "Verify sphinxcontrib-geogebra embeds in project output"
Task: "Verify sphinxcontrib-sagecell elements in project output"
Task: "Verify sphinxcontrib-youtube embeds in project output"
```

## Parallel Example: US2 and US3

```bash
# After US1 is complete, launch US2 and US3 in parallel:
# Stream 1 (US2): Push to CI and monitor
Task: "Commit and push branch, open PR"
Task: "Monitor CI workflow completion"

# Stream 2 (US3): Verify extension output locally
Task: "Verify katex, questionnaire, geogebra, sagecell, youtube extensions"
Task: "Verify theme visual rendering"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (record baselines)
2. Complete Phase 2: Foundational (update `environment.yml`)
3. Complete Phase 3: User Story 1 (build all 18 projects)
4. **STOP and VALIDATE**: All projects build without errors locally
5. This alone confirms the core upgrade works

### Incremental Delivery

1. Complete Setup + Foundational → Environment ready
2. Add User Story 1 → Build all projects → Validate locally (MVP!)
3. Add User Story 2 → Push to CI → Validate in pipeline
4. Add User Story 3 → Inspect extension output → Validate compatibility
5. Polish → Final review and PR description
6. Each phase adds confidence without breaking previous validation

---

## Notes

- [P] tasks = different files/outputs, no dependencies
- [Story] label maps task to specific user story for traceability
- This feature has a natural sequential flow (update → build → CI → verify) but US2 and US3 can overlap
- No automated tests — validation is via Sphinx builds and visual inspection
- Commit after Phase 2 (version pin updates) and after Phase 3 (any conf.py fixes)
- The single most critical file is `environment.yml` — all Phase 2 changes target this file
