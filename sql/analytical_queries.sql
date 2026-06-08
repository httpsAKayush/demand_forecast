-- ...existing code...
-- Example analytical queries

-- 1. Top items by total sales
SELECT item_id, SUM(sales) AS total_sales
FROM sales
GROUP BY item_id
ORDER BY total_sales DESC
LIMIT 50;

-- 2. Weekly aggregated sales for a store
SELECT c.wm_yr_wk, SUM(s.sales) AS weekly_sales
FROM sales s
JOIN calendar c ON s.date = c.date
WHERE s.store_id = 'CA_1'
GROUP BY c.wm_yr_wk
ORDER BY c.wm_yr_wk;