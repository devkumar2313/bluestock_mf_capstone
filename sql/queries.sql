
--Required
--top 5 funds by aum
SELECT d.scheme_name, p.aum_crore
FROM fact_performance p
JOIN dim_fund d ON p.amfi_code = d.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;

--average nav per month
SELECT strftime('%Y-%m', date) AS month, AVG(nav) as avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

--sip inflows by year / yoy
SELECT strftime('%Y', transaction_date) AS year, SUM(amount_inr) as total_sip_volume
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

--transactions by state
SELECT state, COUNT(*) as tx_count, SUM(amount_inr) as total_volume
FROM fact_transactions
GROUP BY state
ORDER BY total_volume DESC;

--funds with expense ratio < 1%
SELECT scheme_name, category, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;

--custom
--highest sharpe ratio
SELECT d.scheme_name, p.sharpe_ratio, p.risk_grade
FROM fact_performance p
JOIN dim_fund d ON p.amfi_code = d.amfi_code
ORDER BY p.sharpe_ratio DESC
LIMIT 5;

--demographic insight
SELECT age_group, AVG(amount_inr) as avg_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY age_group
ORDER BY avg_sip_amount DESC;

--positive alpha
SELECT d.scheme_name, p.alpha
FROM fact_performance p
JOIN dim_fund d ON p.amfi_code = d.amfi_code
WHERE p.alpha > 0
ORDER BY p.alpha DESC;

--transaction volume by city tier
SELECT city_tier, SUM(amount_inr) as total_investment
FROM fact_transactions
GROUP BY city_tier;

--highest drawdown
SELECT d.category, d.scheme_name, MIN(p.max_drawdown_pct) as worst_drawdown
FROM fact_performance p
JOIN dim_fund d ON p.amfi_code = d.amfi_code
GROUP BY d.category;