"""
KaamSetu - Database layer (SQLite)
All persistent data lives here. No important data is kept only in session_state.
"""

import sqlite3
from contextlib import contextmanager
from datetime import datetime

from config import DB_PATH, DEFAULT_CATEGORIES


def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def get_db():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('customer','worker','admin')),
    profile_photo TEXT,
    is_active INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
    user_id INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    location TEXT
);

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    is_active INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS workers (
    user_id INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    about TEXT,
    main_occupation TEXT,
    main_category_id INTEGER REFERENCES categories(id),
    location TEXT,
    service_location TEXT,
    rate_info TEXT,
    availability TEXT NOT NULL DEFAULT 'Available',
    verification_status TEXT NOT NULL DEFAULT 'Not Verified'
        CHECK(verification_status IN ('Not Verified','Pending','Verified','Rejected')),
    is_trusted INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS worker_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    worker_id INTEGER NOT NULL REFERENCES workers(user_id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories(id),
    skill_name TEXT NOT NULL,
    years_experience REAL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS worker_experience (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    worker_id INTEGER NOT NULL REFERENCES workers(user_id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    organization TEXT,
    description TEXT,
    start_date TEXT,
    end_date TEXT
);

CREATE TABLE IF NOT EXISTS certificates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    worker_id INTEGER NOT NULL REFERENCES workers(user_id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    organization TEXT,
    year INTEGER,
    file_path TEXT,
    uploaded_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS portfolio_projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    worker_id INTEGER NOT NULL REFERENCES workers(user_id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    category_id INTEGER REFERENCES categories(id),
    location TEXT,
    project_date TEXT,
    video_path TEXT,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS portfolio_media (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL REFERENCES portfolio_projects(id) ON DELETE CASCADE,
    file_path TEXT NOT NULL,
    media_type TEXT NOT NULL DEFAULT 'photo'
);

CREATE TABLE IF NOT EXISTS worker_verification (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    worker_id INTEGER NOT NULL REFERENCES workers(user_id) ON DELETE CASCADE,
    document_path TEXT,
    note TEXT,
    status TEXT NOT NULL DEFAULT 'Pending' CHECK(status IN ('Pending','Verified','Rejected')),
    submitted_at TEXT NOT NULL,
    reviewed_at TEXT,
    admin_note TEXT
);

CREATE TABLE IF NOT EXISTS work_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL REFERENCES customers(user_id) ON DELETE CASCADE,
    worker_id INTEGER NOT NULL REFERENCES workers(user_id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories(id),
    description TEXT,
    location TEXT,
    preferred_date TEXT,
    preferred_time TEXT,
    additional_requirements TEXT,
    status TEXT NOT NULL DEFAULT 'Pending',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL UNIQUE REFERENCES work_requests(id) ON DELETE CASCADE,
    customer_id INTEGER NOT NULL REFERENCES customers(user_id) ON DELETE CASCADE,
    worker_id INTEGER NOT NULL REFERENCES workers(user_id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    comment TEXT,
    is_flagged INTEGER NOT NULL DEFAULT 0,
    is_hidden INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
);

-- Refundable ₹200 security deposit. One row per (user, role): created against
-- a user's FIRST booking (customer) / FIRST accepted project (worker) only.
-- Purely a simulated hold-and-refund flag for the prototype - no real payment
-- gateway, no penalty math, no partial deductions.
CREATE TABLE IF NOT EXISTS security_deposits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role TEXT NOT NULL CHECK(role IN ('customer','worker')),
    request_id INTEGER NOT NULL REFERENCES work_requests(id) ON DELETE CASCADE,
    amount INTEGER NOT NULL DEFAULT 200,
    status TEXT NOT NULL DEFAULT 'Required' CHECK(status IN ('Required','Paid','Refunded')),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    UNIQUE(user_id, role)
);
"""


def init_db():
    with get_db() as conn:
        conn.executescript(SCHEMA)
        # Seed categories if empty
        existing = conn.execute("SELECT COUNT(*) c FROM categories").fetchone()["c"]
        if existing == 0:
            conn.executemany(
                "INSERT INTO categories (name, is_active) VALUES (?, 1)",
                [(c,) for c in DEFAULT_CATEGORIES],
            )


def any_admin_exists() -> bool:
    with get_db() as conn:
        row = conn.execute("SELECT COUNT(*) c FROM users WHERE role='admin'").fetchone()
        return row["c"] > 0
