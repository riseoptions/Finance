-- Käivita Pythoniga: python src/labs.py 8
SELECT contract_id,ROUND(100.0*(award_eur/base_eur-1),2) AS growth_pct FROM contracts ORDER BY growth_pct DESC;
SELECT supplier,COUNT(*) AS n,SUM(award_eur) AS value_eur FROM contracts GROUP BY supplier;
-- Mitte maksed: award_eur on sõlmitud lepingu hind.
SELECT evidence_id,COUNT(*) AS versions FROM evidence GROUP BY evidence_id HAVING COUNT(*)>1;
