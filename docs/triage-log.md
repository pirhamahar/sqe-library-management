# Triage Meeting Log

## Sprint Triage Decision

The five reported defects were reviewed based on severity, priority, user impact, data integrity, and the risk of incorrect library operations. The following order represents the recommended fix order for the current sprint.

## Fix Ranking

### 1. Duplicate student roll numbers allowed

* Severity: High
* Priority: High
* Decision: Fix this sprint
* Reason: Duplicate roll numbers can create incorrect student records and affect data integrity. This issue should be addressed immediately.

### 2. Already issued book can be issued again

* Severity: High
* Priority: High
* Decision: Fix this sprint
* Reason: The defect can allow the same book to be issued to multiple students at the same time. This directly affects the core borrowing functionality of the library system.

### 3. Book availability status is incorrectly updated

* Severity: High
* Priority: High
* Decision: Fix this sprint
* Reason: This high-severity and high-priority issue affects the accuracy of book availability information and should be addressed during the sprint.
  
### 4. Non-existent book can be returned

* Severity: Medium
* Priority: High
* Decision: Do not fix this sprint
* Reason: The issue has high priority because it affects return operations, but its medium severity makes it possible to defer it when sprint capacity is limited. It will be scheduled for a future sprint.

### 5. Invalid or negative book ID is accepted

* Severity: Medium
* Priority: Medium
* Decision: Do not fix this sprint
* Reason: This is an input-validation problem with lower immediate impact than the higher-priority library transaction defects. It should be scheduled for a future sprint.

## Severity vs Priority Trade-offs

### Trade-off 1: Non-existent book return

This issue has medium severity but high priority. Its severity is medium because it does not directly cause the same level of damage as a major data-integrity failure. However, its priority is high because return operations are an important part of the library workflow and invalid transactions should be prevented. Due to limited sprint capacity, the team will defer this issue.

### Trade-off 2: Invalid or negative book ID

This issue has medium severity and medium priority. The defect should eventually be fixed because invalid input can create unreliable records. However, higher-impact defects affecting core library operations should be handled first. Therefore, this issue is deferred to a future sprint.

## Sprint Decision

The sprint will focus on defects with the greatest immediate impact on core library operations and data integrity.

The two issues selected as not being fixed in this sprint are:

1. Non-existent book can be returned
2. Invalid or negative book ID is accepted



However, only two issues are marked with the `status:wontfix` label as required by the task:

* Non-existent book can be returned
* Invalid or negative book ID is accepted

The book availability issue remains a high-severity and high-priority issue and should be addressed in the next sprint.
