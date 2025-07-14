# 🦅 LogHawk

**LogHawk** is a lightweight, script-based log monitoring tool that helps cybersecurity teams detect and respond to suspicious activity in real time. Designed with simplicity and flexibility in mind, LogHawk automates the analysis of system and application logs to identify potential threats such as:

- 🛑 Brute-force login attempts  
- ⚠️ Unusual traffic spikes  
- 🔥 Critical system errors  
- 🦠 Unauthorized or suspicious script activity  

## 📌 Why Use LogHawk?

Security teams are overwhelmed with data. LogHawk helps by:
- Automating log file analysis
- Detecting known Indicators of Compromise (IoCs)
- Providing clean, actionable output
- Supporting both Bash and Python workflows

LogHawk is open-source and designed for continuous improvement by the community.

---

## 🧰 Features

- ✅ Bash and Python script versions available
- ✅ Detects multiple failed logins (401, SSH)
- ✅ Highlights IP-based traffic spikes
- ✅ Flags `ERROR`, `CRITICAL`, and `panic` log messages
- ✅ Identifies suspicious use of `curl`, `wget`, `.sh`, etc.
- ✅ Output results in an easy-to-read format
- ✅ Supports Cron (Linux/macOS) and Task Scheduler (Windows)

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR-USERNAME/LogHawk.git
cd LogHawk
---


### 2. Make Scripts Executable
bash
chmod +x loghawk.sh

---

## 🐍 Usage (Python)

bash
python3 loghawk.py /path/to/logfile.log
Example Output:
css

---

[🔐] 6 failed login attempts from 192.168.1.101
[🌐] High traffic from 10.0.0.55: 214 requests
[🔥] ERROR at 13:24:45: Disk quota exceeded
[🦠] Suspicious activity: curl download detected in cron job

---

## 💻 Usage (Bash)
bash
./loghawk.sh /path/to/logfile.log

---

# ⏱️ Automation Setup
Linux: Crontab
To run LogHawk every 10 minutes:
bash
crontab -e
Add this line (replace path as needed):

bash
*/10 * * * * /full/path/to/loghawk.sh /var/log/auth.log

---


# Windows: Task Scheduler
To schedule LogHawk on Windows:

Open Task Scheduler

Create a basic task:

Trigger: Every 10 minutes
Action: Start a program

Program/script: python

Add arguments: C:\path\to\loghawk.py C:\logs\access.log

Save and test it
---



# 📂 Project Structure
bash

LogHawk/
├── loghawk.py              # Python version
├── loghawk.sh              # Bash version
├── sample_logs/            # Test log files
├── screenshots/            # Images for report/README
├── README.md               # This file
└── LogHawk_Report.md       # Final report (optional: .pdf)
# 🧪 Sample Logs
Example logs are included in the sample_logs/ folder. Use these to test:

auth.log
access.log
system.log

---

# 🔄 Future Improvements
 Add email alerting
 JSON/CSV export
 Web UI dashboard
 Integration with Splunk or ELK Stack

---

# 📚 References
MITRE ATT&CK: https://attack.mitre.org/

NIST Log Management Guidelines: https://csrc.nist.gov/publications

Red Hat: Log Files and Monitoring: https://access.redhat.com

---

# 🤝 Contributing
Pull requests are welcome! If you have new patterns to detect or want to optimize the tool, feel free to contribute.

---

# 📄 License
This project is licensed under the MIT License.

---

👨‍💻 Author
Linta Susan George
Cybersecurity Student @ Lighthouse Labs
🇨🇦 Canada

