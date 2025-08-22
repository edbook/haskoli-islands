# Proposal: Implementing sphinx-versioned-docs

## Overview

Integrate `sphinx-versioned-docs` to provide professional version management with a version selector dropdown, similar to ReadTheDocs.

## Current vs Proposed Architecture

### Current Approach
```
/ci-improvements/
├── stae205g/index.html
├── R_fra_grunni/index.html
└── [manual navigation page]
```

### Proposed Approach
```
/
├── main/                    # Latest stable docs
│   ├── stae205g/
│   └── R_fra_grunni/
├── ci-improvements/         # PR preview
│   ├── stae205g/
│   └── R_fra_grunni/
├── v25.8.22.1234/          # Tagged releases
│   ├── stae205g/
│   └── R_fra_grunni/
└── index.html               # Auto-redirect to main/
```

**Plus:** Version selector dropdown on every page!

## Key Benefits

### 1. **Professional Version Management**
- ✅ ReadTheDocs-style version selector
- ✅ Automatic branch/tag discovery
- ✅ Clean URL structure (`/main/`, `/v1.2.3/`)
- ✅ Version banners for development builds

### 2. **Enhanced User Experience**
- ✅ Easy switching between versions
- ✅ Clear indication of which version is being viewed
- ✅ Automatic redirection to latest stable
- ✅ Mobile-friendly version selector

### 3. **Better GitHub Integration**
- ✅ Works with existing GitHub Actions
- ✅ Supports PR previews and release builds
- ✅ Maintains current Calver versioning
- ✅ No changes to existing Sphinx configuration

## Implementation Plan

### Phase 1: Basic Setup
1. Add `sphinx-versioned-docs` to dependencies
2. Create new workflow for versioned builds
3. Configure branch and tag patterns
4. Test with main branch

### Phase 2: PR Integration
1. Modify PR workflow to use versioned docs
2. Add PR branch detection
3. Implement version selector for PRs
4. Test branch switching functionality

### Phase 3: Release Integration
1. Connect with Calver release workflow
2. Add tagged version support
3. Configure "latest" version handling
4. Add version archival strategy

## Technical Requirements

### Dependencies
```yaml
# Add to environment.yml
dependencies:
  - sphinx-versioned-docs>=1.4
```

### Configuration
```bash
# Basic usage
sphinx-versioned \
  --output-dir ./versioned-docs \
  --branches main,develop \
  --tags-regex '^v[0-9]+\.[0-9]+\.[0-9]+.*' \
  --greatest-tag \
  --show-banner
```

### File Structure Changes
```
├── .github/workflows/
│   ├── versioned-docs.yml     # New: Main versioned docs workflow
│   ├── pr.yml                 # Modified: Use versioned docs
│   └── release.yml            # Modified: Generate versioned releases
├── versioned-docs.yml         # New: Configuration file
└── VERSIONED_DOCS_PROPOSAL.md # This file
```

## Migration Strategy

### Option A: Gradual Migration
1. Keep existing workflows active
2. Add versioned docs as additional workflow
3. Test in parallel
4. Switch over when stable

### Option B: Full Migration
1. Replace current workflows with versioned approach
2. Migrate existing PR preview functionality
3. Add version selector immediately

**Recommendation:** Option A for safety

## Expected Outcomes

### Immediate Benefits
- Professional version selector on all pages
- Better navigation between versions
- Cleaner URL structure
- Automatic version detection

### Long-term Benefits
- Easier maintenance of documentation versions
- Better user experience for finding specific versions
- Professional appearance matching major documentation sites
- Simplified deployment workflow

## Risk Assessment

### Low Risk
- ✅ Library is actively maintained
- ✅ Compatible with existing Sphinx setup
- ✅ Works with GitHub Pages
- ✅ Non-breaking changes to content

### Considerations
- ⚠️ Additional build complexity
- ⚠️ Larger artifact sizes (multiple versions)
- ⚠️ Need to manage version retention policy

## Next Steps

1. **Approve approach**: Decide on gradual vs full migration
2. **Test implementation**: Start with basic setup
3. **Update dependencies**: Add sphinx-versioned-docs
4. **Deploy pilot**: Test with main branch only
5. **Full rollout**: Integrate PR and release workflows

## Conclusion

`sphinx-versioned-docs` would significantly enhance the documentation experience by providing professional version management with minimal changes to existing workflows. The version selector dropdown and clean URL structure would make the documentation much more user-friendly and professional.

**Recommendation:** Proceed with gradual migration starting with main branch testing.