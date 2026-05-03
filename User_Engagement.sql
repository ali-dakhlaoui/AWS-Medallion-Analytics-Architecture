SELECT 
    u.full_name, 
    u.company, 
    u.plan,
    COUNT(e.event_id) AS activity_count
FROM users u
LEFT JOIN events e ON u.user_id = e.user_id
WHERE LOWER(u.plan) = 'free'
GROUP BY u.full_name, u.company, u.plan
ORDER BY activity_count DESC;