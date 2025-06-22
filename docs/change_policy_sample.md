# Sample Change Management Policy

This policy outlines how changes to systems, infrastructure, and services are proposed, evaluated, approved, and tracked.

---

### 1. Purpose

The purpose of this policy is to ensure that changes are implemented in a controlled and predictable manner that minimizes risk to operations, security, and customer experience.

---

### 2. Scope

This policy applies to:
- All production-facing systems and services
- Internal tools with cross-departmental usage
- Configuration changes that may affect performance or access
- Infrastructure, codebase, and data-handling platforms

---

### 3. Change Types

| Change Type | Description | Approval Required |
|-------------|-------------|-------------------|
| Standard    | Low-risk, repeatable change | Pre-approved |
| Normal      | Planned change with moderate impact | Manager + CAB (if needed) |
| Emergency   | Urgent fix to avoid outage or security breach | Manager (verbal) + CAB review after |

---

### 4. Responsibilities

- **Change Owner**: Submits request and ensures implementation plan is complete
- **Manager or Technical Lead**: Reviews request and approves low to medium risk changes
- **CAB**: Reviews high-risk, cross-functional, or compliance-sensitive changes
- **GRC Team**: Maintains documentation and audits adherence to process

---

### 5. Risk Scoring

All changes must be evaluated using the [Risk Scoring Matrix](/templates/risk_scoring_matrix.md). Scores help determine the approval path and review requirements.

---

### 6. Documentation Requirements

All changes must be:
- Logged in the [Change Log Tracker](/templates/change_log_tracker.md)
- Documented using the [Change Request Template](/templates/change_request_template.md)
- Reviewed post-implementation when applicable

---

### 7. Policy Review

This policy will be reviewed annually by the governance team and updated as needed.

---

### Effective Date:  
_Last updated: July 2024_
