# Equivalence Partitioning Analysis

## 1. Number of Books on Loan

Business Rule: A member may have between 0 and 5 books on loan simultaneously.

| Equivalence Class | Input Range | Valid/Invalid | Representative Value |
|---|---|---|---|
| Valid | 0–5 books | Valid | 3 |
| Invalid | 6+ books | Invalid | 6 |

The valid class includes members who currently have between 0 and 5 books on loan. The invalid class includes members who attempt to exceed the maximum limit of 5 books.

## 2. ISBN Field

Business Rule: ISBN must contain exactly 13 numeric digits with no letters or symbols.

| Equivalence Class | Example | Valid/Invalid | Representative Value |
|---|---|---|---|
| Valid 13-digit ISBN | 9781234567890 | Valid | 9781234567890 |
| Empty string | "" | Invalid | "" |
| Too-short string | 978123456789 | Invalid | 978123456789 |
| Contains letters | 978123456789A | Invalid | 978123456789A |
| Contains symbols | 978-1234567890 | Invalid | 978-1234567890 |

## 3. Days Overdue

Business Rule: Overdue days are mapped to fine tiers.

| Equivalence Class | Input Range | Expected Result | Representative Value |
|---|---|---|---|
| Invalid | Less than 0 | ValueError | -3 |
| Valid | 0 days | None | 0 |
| Valid | 1–7 days | Low | 4 |
| Valid | 8–14 days | Medium | 10 |
| Valid | 15–30 days | High | 20 |
| Valid | 31+ days | Severe | 45 |

## Limitation of Equivalence Partitioning

Equivalence Partitioning reduces the number of test cases by selecting representative values from each equivalence class. However, EP can miss defects at the exact boundaries between classes, such as 7/8 or 14/15. Boundary Value Analysis can be used to test these boundary conditions.
