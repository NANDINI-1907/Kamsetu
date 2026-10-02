"""
KaamSetu - Authentication module
Handles registration and login for Customer, Worker, and Admin roles.
No default/hard-coded credentials. Passwords are always bcrypt-hashed.
"""

import sqlite3
import streamlit as st

from database import get_db, now, any_admin_exists
from utils.security import hash_password, verify_password
from utils.validation import is_valid_email, is_valid_phone, is_strong_password, non_empty


def register_user(name, email, phone, password, role, location=""):
    """
    Register a new user (customer, worker, or admin-bootstrap only).
    Returns (success: bool, message: str).
    """
    name = (name or "").strip()
    email = (email or "").strip().lower()
    phone = (phone or "").strip()

    if not non_empty(name):
        return False, "Please enter your full name."
    if not is_valid_email(email):
        return False, "Please enter a valid email address."
    if not is_valid_phone(phone):
        return False, "Please enter a valid phone number."
    ok, msg = is_strong_password(password)
    if not ok:
        return False, msg
    if role not in ("customer", "worker", "admin"):
        return False, "Invalid role."

    if role == "admin" and any_admin_exists():
        return False, "An admin account already exists. Please log in instead."

    try:
        with get_db() as conn:
            existing = conn.execute(
                "SELECT id FROM users WHERE email = ? OR phone = ?", (email, phone)
            ).fetchone()
            if existing:
                return False, "An account with this email or phone already exists."

            password_hash = hash_password(password)
            cur = conn.execute(
                """INSERT INTO users (name, email, phone, password_hash, role, is_active, created_at)
                   VALUES (?, ?, ?, ?, ?, 1, ?)""",
                (name, email, phone, password_hash, role, now()),
            )
            user_id = cur.lastrowid

            if role == "customer":
                conn.execute(
                    "INSERT INTO customers (user_id, location) VALUES (?, ?)",
                    (user_id, location.strip()),
                )
            elif role == "worker":
                conn.execute(
                    """INSERT INTO workers (user_id, location, availability, verification_status, created_at)
                       VALUES (?, ?, 'Available', 'Not Verified', ?)""",
                    (user_id, location.strip(), now()),
                )
        return True, "Registration successful! You can now log in."
    except sqlite3.IntegrityError:
        return False, "An account with this email or phone already exists."
    except Exception as e:
        return False, f"Something went wrong during registration. Please try again."


def login_user(identifier, password, expected_role=None):
    """
    Log in using email or phone + password.
    Returns (success: bool, user_dict_or_message).
    """
    identifier = (identifier or "").strip().lower()
    if not identifier or not password:
        return False, "Please enter your credentials."

    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE (LOWER(email) = ? OR phone = ?)",
            (identifier, identifier),
        ).fetchone()

    if not row:
        return False, "No account found with these credentials."
    if not row["is_active"]:
        return False, "This account has been deactivated. Please contact support."
    if not verify_password(password, row["password_hash"]):
        return False, "Incorrect password. Please try again."
    if expected_role and row["role"] != expected_role:
        return False, f"This account is not registered as a {expected_role}."

    user = dict(row)
    return True, user


def change_password(user_id, current_password, new_password):
    """Change a logged-in user's password after verifying their current one."""
    ok, msg = is_strong_password(new_password)
    if not ok:
        return False, msg

    with get_db() as conn:
        row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        if not row:
            return False, "Account not found."
        if not verify_password(current_password, row["password_hash"]):
            return False, "Current password is incorrect."
        new_hash = hash_password(new_password)
        conn.execute("UPDATE users SET password_hash = ? WHERE id = ?", (new_hash, user_id))
    return True, "Password changed successfully!"


def logout():
    for key in ["user", "page", "selected_worker_id"]:
        if key in st.session_state:
            del st.session_state[key]
    st.session_state["page"] = "landing"
