# 🏦 SHG Loan Ledger System

A dynamic, event-driven micro-banking ledger application built using **Python**, **Pandas**, and **Streamlit**. This system digitizes and automates financial tracking for Self-Help Groups (SHGs) by enforcing standardized accounting principles like the reducing-balance method and strict interest-first debt recovery.

---

## Overview
In many grassroots microfinance groups, tracking loans in physical paper registers leads to compounding errors, interest calculation discrepancies, and layout confusion over time. This application solves that problem by replacing flat-rate assumptions with a dynamic accounting engine. 

Every time a collection is submitted, the engine isolates the opening state of that cycle, computes interest dynamically, filters cash using **Rule A (Interest-First Recovery)**, and updates the remaining ledger balance seamlessly.

---

##  Flow
Unlike basic calculators that multiply static values across a flat timeline, this application treats every transaction as an event that reshapes the rules for the following month. 

### The Split-Table Engine Logic:
1. **The Demand Table:** Before accepting any cash, the system calculates the baseline for the month based strictly on the current outstanding balance ($Principal \times Monthly\ Interest\ Rate$).
2. **The Collection Table:** When cash is received, **Rule A** filters the funds:
    * **Interest Paid:** Siphons off incoming money until the month's calculated interest demand is completely satisfied.
    * **Principal Paid:** Only the leftover spillover cash is applied to reduce the actual loan principal.


---

##  Codebase 

The project implements a clean separation of concerns across two primary modules:

* **`loan_manage.py` (The Mathematical Core):** Houses the `MemberLoan` and `SHG` classes. It maintains transactional states inside lists, converts histories into clean dataframes via `demand_df()` and `collection_df()`, and hosts the sequenced mathematical logic that safely wraps balance updates.
* **`app.py` (The Streamlit Dashboard):** Implements a sidebar-driven multi-page graphical interface. It handles state preservation across runs using `st.session_state` and provides clear forms for user registrations, collections input, and viewing relational dataframes side-by-side.

---

## 📂 Repository Layout


```text
├── app.py              # Front-end dashboard interface
├── loan_manage.py       # Core object-oriented accounting logic
└──  requirements.txt    # Application dependencies

