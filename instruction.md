Parse the access log located at `/app/access.log`. Analyze the traffic and write a JSON summary report to `/app/report.json`.

Success Criteria:
1. The report must be saved to `/app/report.json`.
2. The JSON report must contain the key `total_requests` matching the total number of requests.
3. The JSON report must contain the key `unique_ips` matching the count of unique IP addresses.
4. The JSON report must contain the key `top_path` matching the most frequently requested path.

Do not modify `/app/access.log`.
You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.