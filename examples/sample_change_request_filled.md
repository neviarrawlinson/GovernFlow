# Sample Change Request (Filled)

---

### Request Details

- **Change Title:** Enable SSO Login via Okta
- **Submitted By:** Brianna James
- **Date Submitted:** 2024-07-15
- **Planned Implementation Date:** 2024-07-18

---

### Description of Change

We are enabling Single Sign-On (SSO) via Okta for internal admin dashboards. This will improve login security and simplify access management.

---

### Change Type

- [ ] Standard  
- [x] Normal  
- [ ] Emergency

---

### Impact Assessment

- **Systems Affected:** Internal admin portal, user profile system  
- **User Impact:** Brief login outage (under 5 minutes)  
- **Downtime Expected:** Yes (planned at 8:00 PM ET)  
- **Backout Plan:** Revert SSO config in Okta and restore legacy credentials

---

### Risk Scoring

| Category         | Score (1–5) | Notes                            |
|------------------|-------------|----------------------------------|
| User Impact      | 2           | Login briefly unavailable        |
| Security Risk    | 1           | Improves posture                 |
| Operational Risk | 2           | Minimal config risk              |
| Reversibility    | 1           | Easy to roll back in Okta        |

**Total Score:** 6 → Low Risk (Normal Change Path)

---

### Approvals

- **Manager Name & Signature:** Jonathan Lee  
- **Date Approved:** 2024-07-16  
- **Additional Approvers:** None

---

### Implementation Summary (Post-Change)

- **Was the change successful?** Yes  
- **Issues Encountered:** None  
- **Lessons Learned:** Users appreciated the updated login method. No login tickets were created.
