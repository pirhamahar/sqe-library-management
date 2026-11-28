
# Lab 11 — Automated Test Coverage

## 1. Baseline Coverage Report

Coverage was measured using pytest-cov and coverage.py with Python 3.11.9.

Command used:

```bash
py -3.11 -m pytest --cov=src --cov-branch --cov-report=term-missing --cov-report=html
```

### Baseline Results

| Metric | Result |
|---|---:|
| Tests Passed | 51 |
| Total Statements | 55 |
| Missing Statements | 0 |
| Total Branches | 26 |
| Partial Branches | 0 |
| Line Coverage | 100% |
| Branch Coverage | 100% |

## 2. Three Weakest Files

The HTML coverage report listed only one source file:

- File: `src/libraryhub/library.py`
- Line Coverage: 100%
- Branch Coverage: 100%
- Missing Lines: None
- Partial Branches: None

The report did not identify three weak files because only one source file was included in the coverage scope. No uncovered lines or branches were found.

## 3. Closing Coverage Gaps

No uncovered lines or branches were identified in the baseline report. Therefore, no additional tests were required to close coverage gaps.

## 4. Coverage vs. Test Quality

A 100% coverage result does not automatically prove that tests verify the correct behavior.

A test may execute every line of a function without checking whether the returned value or updated application state is correct.

For example, a test that only verifies that borrowing a book does not raise an exception may execute the borrowing code but fail to verify whether the available copies were correctly reduced.

A stronger test should assert the expected return value and updated available-copies count.

**Coverage trap:** Executing code without sufficiently checking its expected behavior can create a misleading impression of test quality.

## 5. Coverage Threshold

The project baseline achieved 100% line coverage and 100% branch coverage.

A minimum coverage threshold of 85% will be configured in pytest to prevent future coverage regressions.

## 6. Final Coverage Results

After strengthening the borrowing test assertions and configuring
the minimum coverage threshold, the complete test suite was executed.

| Metric | Baseline | Final |
|---|---:|---:|
| Tests Passed | 51 | 51 |
| Line Coverage | 100% | 100% |
| Branch Coverage | 100% | 100% |
| Missing Statements | 0 | 0 |
| Partial Branches | 0 | 0 |

Minimum enforced coverage threshold: 85%.

Threshold enforcement was verified by running only
tests/test_borrow_limit.py. The tests passed, but coverage
fell below 85%, causing pytest to fail as expected.

The complete test suite was then restored and all 51 tests passed.