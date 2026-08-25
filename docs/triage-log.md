# Triage Meeting Log

## Sprint Triage Decision

The five reported defects were reviewed based on severity, priority, user impact, data integrity, and the risk of incorrect library operations. The following order represents the recommended fix order for the current sprint.

## Fix Ranking

### 1. Duplicate student roll numbers allowed

* Severity: High
* Priority: High
* Decision: Fix this sprint
* Reason: Duplicate roll numbers can create incorrect student records and cause confusion when identifying students. This affects data integrity and should be addressed immediately.

### 2. Already issued book can be issued again

* Severity: High
* Priority: High
* Decision: Fix this sprint
* Reason: The defect can allow the same book to be issued to multiple students at the same time. This directly affects the core borrowing functionality of the library system.

### 3. Book availability status is incorrectly updated

* Severity: High
* Priority: High
* Decision: Fix this sprint
* Reason: Incorrect availability information can cause users to see wrong book status and can contribute to incorrect issue and return operations.

### 4. Non-existent book can be returned

* Severity: Medium
* Priority: High
* Decision: Fix this sprint
* Reason: Although the severity is medium, the priority is high because the defect affects the reliability of return operations and should be corrected to prevent invalid transactions.

### 5. Invalid or negative book ID is accepted

* Severity: Medium
* Priority: Medium
* Decision: Do not fix this sprint
* Reason: This is an input-validation problem with lower immediate impact than the higher-priority library transaction defects. It should be scheduled for a future sprint.

## Severity vs Priority Trade-offs

### Trade-off 1: Non-existent book return

This issue has medium severity but high priority. Its severity is medium because it does not directly cause the same level of damage as a major data-integrity failure. However, its priority is high because return operations are an important part of the library workflow and invalid transactions should be prevented.

### Trade-off 2: Invalid or negative book ID

This issue has medium severity and medium priority. The defect should eventually be fixed because invalid input can create unreliable records. However, higher-severity and higher-priority issues affecting book issuing, availability, and student data should be handled first. Therefore, this issue is deferred to a future sprint.

## Sprint Decision

The sprint will focus on defects that have the greatest impact on core library operations and data integrity. The two issues selected as not being fixed in this sprint are:

1. Non-existent book return
2. Invalid or negative book ID

These issues are deferred because the sprint has limited capacity and the team will prioritize the highest-impact defects first.
