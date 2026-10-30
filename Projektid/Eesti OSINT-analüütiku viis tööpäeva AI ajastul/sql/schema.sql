PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS sources(source_id TEXT PRIMARY KEY, url TEXT NOT NULL, rights TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS evidence(
 evidence_id TEXT NOT NULL, sha256 TEXT NOT NULL, source_id TEXT NOT NULL REFERENCES sources,
 title TEXT NOT NULL, published_at TEXT NOT NULL, captured_at TEXT NOT NULL, ingested_at TEXT NOT NULL,
 path TEXT NOT NULL, url TEXT NOT NULL, text TEXT NOT NULL, synthetic INTEGER NOT NULL CHECK(synthetic IN (0,1)),
 PRIMARY KEY(evidence_id,sha256));
CREATE TABLE IF NOT EXISTS contracts(contract_id TEXT PRIMARY KEY,buyer TEXT,supplier TEXT,
 base_eur REAL CHECK(base_eur>0), award_eur REAL CHECK(award_eur>=0),bids INTEGER CHECK(bids>=0),evidence_id TEXT);
CREATE TABLE IF NOT EXISTS audit(ts TEXT,action TEXT,detail TEXT);
