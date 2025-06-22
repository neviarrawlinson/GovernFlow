# Risk Scoring Matrix

Use this matrix to evaluate the risk level of a proposed change. Each category is scored from 1 (Low Risk) to 5 (High Risk).

---

### Scoring Categories

| Category         | 1 - Low         | 3 - Moderate           | 5 - High                  |
|------------------|------------------|-------------------------|----------------------------|
| **User Impact**  | No user impact   | Small group affected    | Major disruption expected |
| **Security Risk**| No known risk    | Moderate vulnerability  | High severity risk        |
| **Operational Risk** | Easy to reverse | Some complexity         | Irreversible or business-critical |
| **Reversibility**| Full rollback    | Partial rollback        | No rollback available     |

---

### Interpreting Total Score

| Total Score | Risk Level   | Recommendation               |
|-------------|--------------|------------------------------|
| 4–7         | Low          | Proceed with minimal oversight |
| 8–12        | Medium       | Requires manager approval and review |
| 13–20       | High         | Escalate to CAB; detailed impact review required |

---

**Tip:**  
Always document assumptions and mitigation steps if the total score is medium or high.
