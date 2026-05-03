SELECT 
    plan, 
    SUM(mrr) AS total_mrr, 
    COUNT(user_id) AS subscriber_count
FROM subscriptions
WHERE status = 'active'
GROUP BY plan
ORDER BY total_mrr DESC;