# 🦅 LogHawk

**LogHawk** is a lightweight log monitoring tool for detecting early indicators of security threats. It scans system and application logs for:

- 🛑 Failed login attempts
- ⚠️ Unusual traffic spikes
- 🔥 Critical system errors
- 🦠 Suspicious script activity

---

## 📌 Getting Started

### 1. Clone the Repository

bash
git clone https://github.com/YOUR-USERNAME/LogHawk.git
cd LogHawk

### 2. Make Scripts Executable
bash
Copy
Edit
chmod +x loghawk.sh

🐍 Usage (Python)
```bash
Copy
Edit
python3 loghawk.py /path/to/logfile.log

Example Output:
css
Copy
Edit

[🔐] 6 failed login attempts from 192.168.1.101
[🌐] High traffic from 10.0.0.55: 214 requests
[🔥] ERROR at 13:24:45: Disk quota exceeded
[🦠] Suspicious activity: curl download detected in cron job

💻 Usage (Bash)
bash
Copy
Edit
./loghawk.sh /path/to/logfile.log

⏱️ Automation Setup
Linux: Crontab
To run LogHawk every 10 minutes:

bash
Copy
Edit
crontab -e
Add this line (replace with your full path):

bash
Copy
Edit
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

Save and test the task.

# 📂 Project Structure
bash
Copy
Edit
LogHawk/
├── loghawk.py              # Python version
├── loghawk.sh              # Bash version
├── sample_logs/            # Test log files
├── screenshots/            # Images for report/README
├── README.md               # This file
└── LogHawk_Report.md       # Final report (optional: .pdf)
🧪 Sample Logs
Sample logs are located in the sample_logs/ folder for testing:

auth.log

access.log

system.log

🔄 Future Improvements
 Add email alerting

 JSON/CSV export

 Web UI dashboard

 Integration with Splunk or ELK Stack

📚 References
MITRE ATT&CK: https://attack.mitre.org/

NIST Log Management Guidelines: https://csrc.nist.gov/publications

Red Hat: Log Files and Monitoring

🤝 Contributing
Pull requests are welcome! If you discover new threat patterns or want to improve the tool, feel free to contribute.

📄 License
This project is licensed under the MIT License.

# 👨‍💻 Author
Linta Susan George
Cybersecurity Student @ Lighthouse Labs
🇨🇦 Canada

   

