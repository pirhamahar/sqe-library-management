# Boundary Value Analysis

## 1. Fine Tier Boundaries

The `fine_tier()` function uses the following boundaries:
0, 1, 8, 15, 31.

| Boundary | Value - 1 | Expected | Boundary Value | Expected | Value + 1 | Expected |
|---|---:|---|---:|---|---:|---|
| 0 | -1 | ValueError | 0 | None | 1 | Low |
| 1 | 0 | None | 1 | Low | 2 | Low |
| 8 | 7 | Low | 8 | Medium | 9 | Medium |
| 15 | 14 | Medium | 15 | High | 16 | High |
| 31 | 30 | High | 31 | Severe | 32 | Severe |

## 2. Borrow Limit Boundaries

The `Library.borrow_book()` function allows a member to have a maximum of 5 books on loan.

| Boundary | Current Books | Attempt | Expected Result |
|---|---:|---|---|
| Below maximum | 4 | Borrow 1 more | Valid |
| Maximum | 5 | Borrow 1 more | ValueError |
| Above maximum | 6 | Borrow 1 more | Invalid / ValueError |

## 3. ISBN Length Boundaries

The `validate_isbn()` function requires exactly 13 numeric digits.

| Boundary | ISBN Length | Expected Result |
|---|---:|---|
| Below boundary | 11 | ValueError |
| Below boundary | 12 | ValueError |
| Exact boundary | 13 | Valid |
| Above boundary | 14 | ValueError |
| Above boundary | 15 | ValueError |

## 4. Boundary Value Analysis Limitation

Boundary Value Analysis focuses on values at and immediately around the boundaries. It is effective for detecting off-by-one errors, but it does not test every possible value in an input domain. Equivalence Partitioning and Boundary Value Analysis should therefore be combined for efficient test coverage.


## 4. Pytest Execution Summary

The complete pytest suite was executed after implementing the Boundary Value Analysis tests.

Test results:

- `tests/test_borrow_limit.py` — 4 passed
- `tests/test_fine_tier.py` — 6 passed
- `tests/test_fine_tier_bva.py` — 13 passed
- `tests/test_validate_isbn.py` — 10 passed

**Total: 33 passed in 0.08s**

All implemented EP and BVA test cases passed successfully.
