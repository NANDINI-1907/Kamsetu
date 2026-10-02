# 🛠️ KaamSetu — Connecting Skills with Opportunities

KaamSetu is a skilled-worker discovery and connection platform. Its core idea:
**every skilled worker gets a trusted, LinkedIn-style professional profile** —
not just a one-line listing — so customers can hire with confidence.

## Quick Start

```bash
# 1. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`. A SQLite database is created
automatically at `database/kaamsetu.db` on first run — no manual setup needed.

## First-Time Setup

There are **no default logins**. To get started:

1. Open the app and click **Register**.
2. The first time only, an **"Admin (first-time setup)"** option appears in the
   registration role picker — use it once to create your admin account. It
   disappears after the first admin is created.
3. Register normal **Customer** and **Worker** accounts the same way.
4. Log in with whichever role you registered as (email or phone + password).

## Demo Flow

**Customer:** Register → Login → Customer Dashboard → Find a Worker / Smart Matching →
View Professional Profile → Book Worker → Track status in "My Requests" →
Rate & Review once completed. Notifications and Settings (change password) are
also available from the dashboard nav.

**Worker:** Register → Login → Worker Dashboard → Build Profile (about, category, rate) →
Add Skills / Experience → Upload Certificates → Add Portfolio Projects → Submit
for Verification → Receive & manage Work Requests (Accept → In Progress →
Completed). Notifications and Settings (account info, change password) are
also available from the dashboard nav.

**Admin:** Login → Overview (charts) → Review pending Verifications
(Approve/Reject) → Manage Customers/Workers → Monitor Work Requests →
Moderate Reviews → Manage Categories.

## Key Design Notes

- **Refundable ₹200 Security Deposit** (`modules/deposits.py`): a one-time,
  per-user deposit — required on a customer's first booking and a worker's
  first accepted project. Payment is simulated (no real gateway). It is
  refunded in full the moment the linked booking/project reaches a final
  status (Completed, Rejected, or Cancelled) — deliberately no penalty math,
  no partial deductions, and no automated judgment about whether a
  cancellation was "genuine." Visible on the Customer/Worker "My
  Requests"/"Work Requests" card it's tied to, in each dashboard's Settings
  tab, and in a dedicated Admin → Deposits view.

- **Navigation** is routed through a single `st.session_state["page"]` value
  in `app.py`, with each dashboard owning its own sub-page key
  (`customer_page` / `worker_page` / `admin_page`). Every button that changes
  page has a unique, stable `key=`, and every router has a fallback branch so
  an unexpected page value never renders blank.
- **Language switching** uses a selectbox bound to a stable widget key with
  an `on_change` callback that updates `st.session_state["lang"]` immediately
  and independently of the current page, so changing language never resets
  navigation and the whole UI (nav, dashboards, Smart Matching, forms, empty
  states) re-renders in the newly selected language right away.
- **Smart Matching** (Customer Dashboard → Smart Matching) is a transparent,
  rule-based scoring engine — not machine learning — using skill/category
  match (30%), location (20%), experience (15%), availability (15%),
  rating (10%), completed projects (5%), and budget compatibility (5%), with
  verification status as a small bonus. Each result shows *why* it matched.
  If no worker is a genuine category match, the UI shows "No exact match
  found" with suggestions instead of a blank or broken page.
- **Verification** is an internal KaamSetu document-review process performed
  by admins — it is not a government or third-party background check, and the
  app does not claim otherwise.
- **KaamSetu Trusted Worker badge** is only granted once a worker is Verified
  AND meets a configurable minimum completed-project / rating threshold (see
  `TRUSTED_WORKER_MIN_COMPLETED_PROJECTS` / `..._MIN_RATING` in `config.py`).
- **Location matching** uses Geopy (Nominatim) opportunistically — if
  geocoding fails or is unavailable (e.g., no internet), the app degrades
  gracefully and location just isn't used to rank/filter that turn.
- **Multi-language** (English / Telugu / Hindi) is centralized in
  `config.py`'s `TRANSLATIONS` dict and the `t()` helper — add a new language
  by adding a new key to each entry and to `LANGUAGES`.

## Project Structure

```
KaamSetu/
├── app.py                  # Entry point: landing page, auth, routing
├── database.py             # SQLite schema + connection helpers
├── auth.py                 # Registration & login
├── config.py                # Categories, languages/translations, constants
├── requirements.txt
├── modules/
│   ├── customer.py         # Customer dashboard, search, request flow
│   ├── worker.py            # Worker dashboard: profile/skills/portfolio/requests
│   ├── admin.py              # Admin dashboard: stats, moderation, management
│   ├── profile.py            # Worker professional-profile data + rendering
│   ├── matching.py           # Rule-based smart matching engine
│   ├── requests.py           # Work request booking workflow
│   ├── reviews.py            # Ratings & reviews
│   └── verification.py       # Worker verification workflow
├── utils/
│   ├── validation.py         # Input validation
│   ├── security.py           # Password hashing, role guards
│   └── helpers.py            # File uploads, geocoding, formatting
├── assets/css/style.css      # Theming
├── uploads/                  # Profile photos, certs, project media (gitignored contents)
└── database/kaamsetu.db      # SQLite database (auto-created)
```

## Notes for Evaluators / Hackathon Demo

- All buttons are functional — no "Coming Soon" placeholders.
- All data is persisted in SQLite; restarting the app does not lose data.
- Passwords are bcrypt-hashed; never stored in plain text.
- File uploads are validated for type and size, and stored with unique names.
- Only the customer of a *Completed* request can leave a review, and only once.
- Workers cannot self-approve their own verification status — only Admin can.
