import os
import subprocess

test_css_patch = """
/* COMPACT 24-WORD GRID (ZERO SCROLL, NEVER TOUCHES FOOTER) */
.vocab-words-grid.grid-6-cols {
  grid-template-columns: repeat(6, 1fr) !important;
  max-width: 860px !important;
  gap: 4px 6px !important;
}

.vocab-words-grid.grid-6-cols .vocab-word-tile {
  min-height: 48px !important;
  padding: 3px 4px 2px !important;
  border-radius: 10px !important;
  border-bottom-width: 2.5px !important;
  gap: 1px !important;
}

.vocab-words-grid.grid-6-cols .vocab-tile-em {
  font-size: 1.15rem !important;
  line-height: 1 !important;
  margin-bottom: 0 !important;
}

.vocab-words-grid.grid-6-cols .vocab-tile-ar {
  font-size: 1.05rem !important;
  font-weight: 700 !important;
  line-height: 1.15 !important;
}

.vocab-words-grid.grid-6-cols .vocab-tile-trans {
  font-size: 0.72rem !important;
  line-height: 1.1 !important;
}

.vocab-words-grid.grid-6-cols .vocab-tile-trans.ur-font {
  font-size: 0.82rem !important;
  line-height: 1.25 !important;
}

.vocab-words-grid.grid-6-cols .vocab-tile-speaker {
  display: none !important;
}

.lesson-page-card.is-vocab-table,
.lesson-page-card:has(.vocab-table-card) {
  padding: 6px 14px 8px !important;
  gap: 3px !important;
  max-width: 860px !important;
  border-bottom-width: 4px !important;
}

.vocab-table-header-box {
  padding: 3px 10px !important;
  margin-bottom: 3px !important;
}

.lesson-stage.has-vocab-card,
.lesson-stage:has(.is-vocab-table),
.lesson-stage:has(.is-letter-table) {
  overflow-y: auto !important;
  padding: 8px 16px 24px !important;
}

.lesson-stage.has-vocab-card .lesson-card-viewport,
.lesson-stage:has(.is-vocab-table) .lesson-card-viewport,
.lesson-stage:has(.is-letter-table) .lesson-card-viewport {
  margin: 0 auto !important;
}
"""

with open("scratch/patch_preview.css", "w", encoding="utf-8") as f:
    f.write(test_css_patch)

print("Created patch_preview.css")
