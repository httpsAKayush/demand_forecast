-- ...existing code...
-- Minimal schema for M5-like dataset
CREATE TABLE IF NOT EXISTS items (
    item_id TEXT PRIMARY KEY,
    dept_id TEXT,
    cat_id TEXT
);

CREATE TABLE IF NOT EXISTS stores (
    store_id TEXT PRIMARY KEY,
    state_id TEXT
);

CREATE TABLE IF NOT EXISTS calendar (
    date DATE PRIMARY KEY,
    wm_yr_wk INTEGER,
    weekday TEXT,
    month INTEGER,
    year INTEGER,
    event_name_1 TEXT,
    event_type_1 TEXT
);

CREATE TABLE IF NOT EXISTS prices (
    store_id TEXT,
    item_id TEXT,
    wm_yr_wk INTEGER,
    sell_price NUMERIC,
    PRIMARY KEY (store_id, item_id, wm_yr_wk)
);

CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    store_id TEXT,
    item_id TEXT,
    date DATE,
    sales INTEGER
);