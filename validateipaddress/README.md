# Validate IP Address

A command-line tool that validates IP addresses against multiple criteria for security purposes. The tool checks if an IP address is within known trusted ranges (allowlist), blocked ranges (denylist), or belongs to major cloud providers. It helps identify potentially dangerous IPs by checking against reserved networks, military/DoD ranges, and known problematic hosting providers, while also detecting if the IP belongs to cloud infrastructure like AWS or Azure. The tool returns detailed validation results including whether the IP is safe to use, any matches in allowed ranges, and cloud provider information if applicable.