import re
import json


with open("data_log.txt","r") as f:
    log_data = f.read()
    lines = log_data.splitlines()




# TASK - 1
ip_pattern =  r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ips = re.findall(ip_pattern, log_data)
unique_ips = sorted(set(ips))
print("ip addresses:", unique_ips)




# TASK - 2
actions_dict = {}

pattern = r'INFO.*User\s+(\w+).*?(UPDATE|DELETE|CREATE|created a new record)'
for line in lines:
    match = re.search(pattern, line)
    if match:
        user = match.group(1)
        action = match.group(2)

        if user not in actions_dict:
            actions_dict[user] = set()

        actions_dict[user].add(action)

actions_dict = {k:list(v) for k,v in actions_dict.items()}

print("User Actions:", actions_dict)




# TASK - 3
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emails = re.findall(email_pattern, log_data)
print("Emails:", emails)




# TASK - 4
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
phones = set(re.findall(phone_pattern, log_data))
print("Phone Numbers:", phones)




# TASK - 5
url_pattern = r'https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
urls = set(re.findall(url_pattern, log_data))
print("URLs:", urls)




# TASK - 6
levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
level_count = {level:0 for level in levels}
for line in lines:
    for level in levels:
        if re.search(level, line):
            level_count[level] += 1
print("Log Level Count:", level_count)




# TASK - 7
timestamp_pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]'
timestamps = re.findall(timestamp_pattern, log_data)
timestamps.sort()
print("Timestamps:", timestamps)




# TASK - 8
masked_log = log_data
masked_log = re.sub(ip_pattern, "***.***.***.***", masked_log)
masked_log = re.sub(phone_pattern, "XXX-XXX-XXXX", masked_log)
masked_log = re.sub(email_pattern, "hidden@example.com", masked_log)
with open("masked_data_log.txt", "w") as f:
    f.write(masked_log)
print("Masked log file created")




# TASK - 9
error_pattern = r'\bDB_ERR\d{4}\b'
errors = list(set(re.findall(error_pattern, log_data)))
print("Error Codes:", errors)




# TASK - 10
log_pattern = r'\[(.*?)\]\s+(INFO|WARNING|ERROR|CRITICAL)\s+(.*)'

parsed_logs = []
for line in lines:
    match = re.match(log_pattern, line)
    if match:
        entry = {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        }
        parsed_logs.append(entry)
with open("parsed_log.json", "w") as f:
    json.dump(parsed_logs, f, indent=4)
print("JSON log file created")