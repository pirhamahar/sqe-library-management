# LibraryHub Code Review Checklist

## 1. Correctness

- Does the code produce the expected result for normal inputs?
- Are edge cases and invalid inputs handled correctly?

## 2. Tests

- Are meaningful tests provided for the new or changed functionality?
- Do the tests cover important edge cases and failure conditions?

## 3. Readability

- Are variable and function names clear and meaningful?
- Is the code easy to read, with unnecessary duplication avoided?

## 4. Design

- Does the change fit the existing LibraryHub architecture?
- Does the implementation avoid unnecessary complexity or duplicated logic?

## 5. Risk

- Could the change introduce security or data-validation problems?
- Could the change break existing functionality or create performance issues?

## 6. Documentation

- Is the function documented with a clear docstring?
- Are assumptions and expected inputs explained?
- Is the function's return value clearly described?


## 7. Lessons Learned

### Most Valuable Checklist Item
- Are meaningful tests provided for the new or changed functionality?

This checklist item helped identify issues in the borrow_percentile function. Testing helped verify the percentile calculation, empty library handling, unknown members, and single-member library scenarios.

### Additional Checklist Item for Next Time
- Are boundary conditions and unusual input scenarios tested before approving a pull request?

This will help reviewers identify edge-case bugs before merging code.
