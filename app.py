"""
KaamSetu - Main Application Entry Point
"Connecting Skills with Opportunities."
"""

import streamlit as st

from database import init_db, any_admin_exists
from config import LANGUAGES, t, DEFAULT_CATEGORIES, CATEGORY_ICONS, DEFAULT_ICON, BASE_DIR
from auth import register_user, login_user, logout
from utils.security import is_logged_in
from modules.customer import render_customer_dashboard
from modules.worker import render_worker_dashboard
from modules.admin import render_admin_dashboard

import os

st.set_page_config(page_title="KaamSetu | Connecting Skills with Opportunities",
                    page_icon="🛠️", layout="wide", initial_sidebar_state="collapsed")

init_db()


def load_css():
    css_path = os.path.join(BASE_DIR, "assets", "css", "style.css")
    try:
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except Exception:
        pass


load_css()

# ---------------------------------------------------------------------------
# SESSION STATE DEFAULTS
# (Set only once per session - never reset on rerun, so login/page/lang all
#  survive navigation.)
# ---------------------------------------------------------------------------
st.session_state.setdefault("page", "landing")
st.session_state.setdefault("lang", "en")
st.session_state.setdefault("user", None)


def lang_code():
    return st.session_state.get("lang", "en")


def go_to(page_name):
    """Navigate to a top-level page while explicitly preserving everything else
    already in session_state (login, language, sub-page selections, etc.)."""
    st.session_state["page"] = page_name
    st.rerun()


def go_to_register(role_hint=None):
    """Navigate straight to registration, optionally pre-selecting Worker or
    Customer so a dedicated 'Worker Registration' / 'Customer Registration'
    button lands the user directly on the right registration form."""
    if role_hint:
        st.session_state["register_role_hint"] = role_hint
    st.session_state["page"] = "register"
    st.rerun()


def _on_language_change():
    """Callback bound to the language selectbox's on_change event.
    Runs BEFORE the rest of the script re-executes, so by the time any
    page content renders below, st.session_state['lang'] already reflects
    the newly chosen language. This intentionally does NOT touch
    st.session_state['page'], so the user stays on the same page."""
    chosen_display_name = st.session_state.get("lang_selector")
    if chosen_display_name in LANGUAGES:
        st.session_state["lang"] = LANGUAGES[chosen_display_name]


# ---------------------------------------------------------------------------
# TOP NAVIGATION BAR
# ---------------------------------------------------------------------------
def render_top_nav():
    lang = lang_code()
    cols = st.columns([3, 1.4, 1, 1, 1])
    with cols[0]:
        st.markdown(f"### 🛠️ {t('app_name', lang)}")
    with cols[1]:
        # The selectbox's value is derived from st.session_state['lang'] via
        # `index`, and any user change is applied immediately by the on_change
        # callback (which runs BEFORE this script re-renders the current page,
        # per Streamlit's callback semantics). Using a stable widget key +
        # on_change avoids any race between the widget's own persisted state
        # and the index computed here on each rerun.
        display_names = list(LANGUAGES.keys())
        codes = list(LANGUAGES.values())
        current_index = codes.index(lang) if lang in codes else 0
        st.selectbox(
            "🌐", display_names,
            index=current_index,
            label_visibility="collapsed",
            key="lang_selector",
            on_change=_on_language_change,
        )

    user = st.session_state.get("user")
    if user:
        with cols[2]:
            st.caption(f"👤 {user['name']} ({t(user['role'], lang)})")
        with cols[3]:
            if st.button(f"🏠 {t('dashboard', lang)}", use_container_width=True, key="nav_dashboard_btn"):
                go_to("dashboard")
        with cols[4]:
            if st.button(f"🚪 {t('logout', lang)}", use_container_width=True, key="nav_logout_btn"):
                logout()
                st.rerun()
    else:
        with cols[3]:
            if st.button(t("login", lang), use_container_width=True, key="nav_login_btn"):
                go_to("login")
        with cols[4]:
            if st.button(t("register", lang), use_container_width=True, type="primary", key="nav_register_btn"):
                go_to("register")

    st.markdown("---")


# ---------------------------------------------------------------------------
# LANDING PAGE
# ---------------------------------------------------------------------------
def render_landing_page():
    lang = lang_code()
    st.markdown(f"""
    <div class="ks-hero">
        <h1>🛠️ {t('app_name', lang)}</h1>
        <div class="tagline">{t('tagline', lang)}</div>
        <div class="subheading">{t('subheading', lang)}</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(f"📝 {t('register', lang)}", use_container_width=True, type="primary", key="hero_register"):
            go_to("register")
    with c2:
        if st.button(f"🔑 {t('login', lang)}", use_container_width=True, key="hero_login"):
            go_to("login")
    with c3:
        if st.button(f"🔍 {t('explore_workers', lang)}", use_container_width=True, key="hero_explore"):
            go_to("explore")

    # Dedicated shortcuts straight into each registration flow (in addition to
    # the generic Register button above), so "Worker Registration" and
    # "Customer Registration" each land the user on the right form directly.
    c4, c5 = st.columns(2)
    with c4:
        if st.button(f"👷 {t('worker', lang)} {t('register', lang)}", use_container_width=True,
                     key="hero_register_worker"):
            go_to_register("worker")
    with c5:
        if st.button(f"🧑‍💼 {t('customer', lang)} {t('register', lang)}", use_container_width=True,
                     key="hero_register_customer"):
            go_to_register("customer")

    st.markdown(f'<div class="ks-section-title">📖 {t("about_kaamsetu", lang)}</div>', unsafe_allow_html=True)
    st.write(t("about_kaamsetu_body", lang))

    st.markdown(f'<div class="ks-section-title">⚙️ {t("how_it_works", lang)}</div>', unsafe_allow_html=True)
    hcols = st.columns(4)
    steps = [
        ("1️⃣", t("step_discover_title", lang), t("step_discover_desc", lang)),
        ("2️⃣", t("step_portfolio_title", lang), t("step_portfolio_desc", lang)),
        ("3️⃣", t("step_request_title", lang), t("step_request_desc", lang)),
        ("4️⃣", t("step_review_title", lang), t("step_review_desc", lang)),
    ]
    for col, (num, title, desc) in zip(hcols, steps):
        with col:
            with st.container(border=True):
                st.markdown(f"### {num} {title}")
                st.caption(desc)

    st.markdown(f'<div class="ks-section-title">🗂️ {t("worker_categories", lang)}</div>', unsafe_allow_html=True)
    cat_cols = st.columns(6)
    for i, cat in enumerate(DEFAULT_CATEGORIES[:18]):
        icon = CATEGORY_ICONS.get(cat, DEFAULT_ICON)
        with cat_cols[i % 6]:
            st.markdown(f"""<div class="ks-cat-chip"><div class="icon">{icon}</div>
                        <div class="label">{cat}</div></div>""", unsafe_allow_html=True)
    st.caption(f"+ {len(DEFAULT_CATEGORIES) - 18} more categories including "
               + ", ".join(DEFAULT_CATEGORIES[18:]))

    st.markdown(f'<div class="ks-section-title">🛡️ {t("trust_verification", lang)}</div>', unsafe_allow_html=True)
    tcols = st.columns(3)
    trust_points = [
        (t("trust1_title", lang), t("trust1_desc", lang)),
        (t("trust2_title", lang), t("trust2_desc", lang)),
        (t("trust3_title", lang), t("trust3_desc", lang)),
    ]
    for col, (title, desc) in zip(tcols, trust_points):
        with col:
            st.markdown(f'<div class="ks-trust-item"><b>{title}</b><br><span style="font-size:0.85rem">{desc}</span></div>',
                        unsafe_allow_html=True)

    st.markdown(f"""<div class="ks-footer">© 2026 {t('app_name', lang)} · {t('tagline', lang)} ·
                Built with Python &amp; Streamlit</div>""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# EXPLORE WORKERS (public, no login required)
# ---------------------------------------------------------------------------
def render_explore_page():
    from modules.customer import search_workers
    from modules.profile import render_worker_card

    lang = lang_code()
    st.markdown(f"## 🔍 {t('explore_workers', lang)}")
    st.caption(t("browse_workers_hint", lang))

    results = search_workers()
    st.markdown(f"**{len(results)} {t('workers_available', lang)}**")
    if not results:
        st.info(t("no_workers_found", lang))
    for w in results[:30]:
        render_worker_card(w, lang, key_prefix="explore_")
        if not is_logged_in():
            st.caption(f"👆 {t('login_or_register_hint', lang)}")


# ---------------------------------------------------------------------------
# LOGIN PAGE
# ---------------------------------------------------------------------------
def render_login_page():
    lang = lang_code()
    st.markdown(f"## 🔑 {t('login', lang)}")
    role_options = [t("customer", lang), t("worker", lang), t("admin", lang)]
    role_tab = st.radio(t("i_am_a", lang), role_options, horizontal=True, key="login_role_radio")
    role_map = {t("customer", lang): "customer", t("worker", lang): "worker", t("admin", lang): "admin"}

    with st.form("login_form"):
        identifier = st.text_input(t("email_or_phone", lang), key="login_identifier_input")
        password = st.text_input(t("password", lang), type="password", key="login_password_input")
        submitted = st.form_submit_button(t("login", lang), type="primary", use_container_width=True,
                                           key="login_submit_btn")

        if submitted:
            ok, result = login_user(identifier, password, expected_role=role_map[role_tab])
            if ok:
                st.session_state["user"] = result
                st.session_state["page"] = "dashboard"
                st.success(f"{t('welcome_back', lang)}, {result['name']}!")
                st.rerun()
            else:
                st.error(result)

    st.caption(t("dont_have_account", lang))
    if st.button(f"📝 {t('register_instead', lang)}", key="login_page_register_link"):
        go_to("register")


# ---------------------------------------------------------------------------
# REGISTER PAGE
# ---------------------------------------------------------------------------
def render_register_page():
    lang = lang_code()
    st.markdown(f"## 📝 {t('register', lang)}")

    options = [t("customer", lang), t("worker", lang)]
    admin_label = f"{t('admin', lang)} (first-time setup)"
    if not any_admin_exists():
        options.append(admin_label)

    # Honor a role pre-selection coming from a dedicated "Worker Registration" /
    # "Customer Registration" shortcut button, if one was used to get here.
    # We set the radio's own widget-state key directly (rather than passing
    # `index=`) so it reliably overrides any previously "sticky" selection
    # from an earlier visit to this page in the same session.
    role_hint = st.session_state.pop("register_role_hint", None)
    if role_hint == "worker":
        st.session_state["register_role_radio"] = t("worker", lang)
    elif role_hint == "customer":
        st.session_state["register_role_radio"] = t("customer", lang)

    role_tab = st.radio(t("register_as", lang), options, horizontal=True, key="register_role_radio")

    role = "customer"
    if role_tab == t("worker", lang):
        role = "worker"
    elif role_tab == admin_label:
        role = "admin"
        st.info("No admin account exists yet. This form will create the first (and only) admin account. "
                "Once created, this option disappears.")

    with st.form("register_form"):
        name = st.text_input(t("name", lang), key="register_name_input")
        email = st.text_input(t("email", lang), key="register_email_input")
        phone = st.text_input(t("phone", lang), key="register_phone_input")
        location = ""
        if role != "admin":
            location = st.text_input(t("location", lang), key="register_location_input")
        password = st.text_input(t("password", lang), type="password", key="register_password_input")
        confirm_password = st.text_input(t("confirm_password", lang), type="password", key="register_confirm_password_input")
        submitted = st.form_submit_button(t("register", lang), type="primary", use_container_width=True,
                                           key="register_submit_btn")

        if submitted:
            if password != confirm_password:
                st.error("Passwords do not match.")
            else:
                ok, msg = register_user(name, email, phone, password, role, location)
                if ok:
                    st.success(msg)
                    st.session_state["page"] = "login"
                    st.rerun()
                else:
                    st.error(msg)

    st.caption(t("already_have_account", lang))
    if st.button(f"🔑 {t('login_instead', lang)}", key="register_page_login_link"):
        go_to("login")


# ---------------------------------------------------------------------------
# DASHBOARD ROUTER
# ---------------------------------------------------------------------------
def render_dashboard():
    user = st.session_state.get("user")
    if not user:
        st.warning("Please log in to view your dashboard.")
        st.session_state["page"] = "login"
        st.rerun()
        return

    lang = lang_code()
    if user["role"] == "customer":
        render_customer_dashboard(user, lang)
    elif user["role"] == "worker":
        render_worker_dashboard(user, lang)
    elif user["role"] == "admin":
        render_admin_dashboard(user, lang)


# ---------------------------------------------------------------------------
# MAIN ROUTER
# ---------------------------------------------------------------------------
# Every top-level page this app can be on. Anything outside this set falls
# back to the landing page instead of silently failing to render.
_VALID_PAGES = {"landing", "explore", "login", "register", "dashboard"}


def main():
    render_top_nav()

    page = st.session_state.get("page", "landing")
    if page not in _VALID_PAGES:
        page = "landing"
        st.session_state["page"] = "landing"

    try:
        if page == "landing":
            render_landing_page()
        elif page == "explore":
            render_explore_page()
        elif page == "login":
            render_login_page()
        elif page == "register":
            render_register_page()
        elif page == "dashboard":
            render_dashboard()
    except Exception as e:
        st.error("Something went wrong while loading this page. Please try again or return to the home page.")
        with st.expander("Technical details (for developers)"):
            st.exception(e)
        if st.button(f"🏠 {t('return_to_home', lang_code())}", key="error_return_home"):
            st.session_state["page"] = "landing"
            st.rerun()


if __name__ == "__main__":
    main()
