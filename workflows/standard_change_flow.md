# Standard Change Workflow

This workflow applies to low-risk, repeatable changes that have already been pre-approved by governance or CAB.

---

### 🔄 Standard Change Flow

1. **Initiator identifies standard change**  
   - Examples: password policy update, patch deployment, adding new users

2. **Change is logged in tracker**  
   - Use the [Change Log Tracker](/templates/change_log_tracker.md)

3. **Pre-approval is verified**
   - Confirm the change type is on the approved standard change list
   - No additional approvals are required

4. **Change is scheduled and implemented**
   - Notify stakeholders via standard comms (Slack, email, etc.)
   - Perform change in production or staging as applicable

5. **Post-implementation check**
   - Validate success
   - Document any deviations or notes

6. **Close the change record**
   - Mark as complete in change tracker
   - No CAB review required unless issues occurred

---

### ✅ Requirements
- No business downtime
- Fully documented rollback plan (if applicable)
- No cross-system or compliance impact

---

### 📌 Notes
- If the change impacts external users, it may need to be reclassified as Normal
- Standard changes can be automated once repeatable and risk is validated
