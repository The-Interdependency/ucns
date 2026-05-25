import re
import unittest
from pathlib import Path

# Files excluded from the scan because they define (not violate) the boundary.
# The bridge checklist quotes forbidden phrases as illustrative examples.
EXCLUDED_DOC_FILES = {
    'edcm-edcmbone-bridge-checklist.md',
}

DOC_FILES = [
    Path('README.md'),
    *[p for p in Path('docs').glob('*.md') if p.name not in EXCLUDED_DOC_FILES],
]

# Explicit overclaim patterns that should never appear in documentation copy.
FORBIDDEN_PATTERNS = [
    re.compile(r"\bUCNS\s+proves\s+EDCM\b", re.IGNORECASE),
    re.compile(r"\bTheorem\s*N\s+proves\s+EDCM\b", re.IGNORECASE),
    re.compile(r"\bTheorem\s*N\s+validates\s+EDCM\b", re.IGNORECASE),
    re.compile(r"\bUCNS-G\s+is\s+proven\b", re.IGNORECASE),
    re.compile(r"\bEDCM\s+is\s+theorem-validated\s+by\s+UCNS\b", re.IGNORECASE),
]


class TestDocsClaimGuardrail(unittest.TestCase):
    def test_no_overclaim_phrases(self) -> None:
        violations = []
        for path in DOC_FILES:
            text = path.read_text(encoding='utf-8')
            for pattern in FORBIDDEN_PATTERNS:
                for m in pattern.finditer(text):
                    start = max(0, m.start() - 60)
                    end = min(len(text), m.end() + 60)
                    excerpt = text[start:end].replace("\n", " ")
                    violations.append(
                        f"{path}: pattern={pattern.pattern!r}; excerpt={excerpt!r}"
                    )

        self.assertEqual(
            violations,
            [],
            "\n".join([
                "Documentation claim boundary violation(s) detected.",
                "See docs/edcm-edcmbone-bridge-checklist.md non-transfer rule.",
                *violations,
            ]),
        )


if __name__ == '__main__':
    unittest.main()
