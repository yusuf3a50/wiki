# Systemd Service Creation for Python Scripts

This guide explains how to create systemd services that run Python scripts from a virtual environment, either continuously or periodically using timers.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Method 1: Continuous Running Service](#method-1-continuous-running-service)
- [Method 2: Periodic Execution with Timers](#method-2-periodic-execution-with-timers)
- [Service Management](#service-management)
- [Troubleshooting](#troubleshooting)

## Overview

Systemd is the init system used by most modern Linux distributions. It can manage services that:
- Run continuously in the background
- Execute periodically on a schedule (using timers)
- Restart automatically on failure
- Start on boot

For more information about systemd, see [Understanding and Using systemd](https://www.linux.com/training-tutorials/understanding-and-using-systemd/)

## Prerequisites

1. **Python Virtual Environment**: Set up a virtual environment for your script
   ```bash
   python3 -m venv /path/to/your/venv
   source /path/to/your/venv/bin/activate
   pip install your-required-packages
   deactivate
   ```

2. **Python Script**: Have your Python script ready and tested

3. **Root/Sudo Access**: Required to create and manage systemd services

## Method 1: Continuous Running Service

This method creates a service that runs continuously, suitable for:
- Long-running processes
- Scripts with internal loops
- Services that need to be always available

### Step 1: Create Your Python Script

Example of a long-running script with internal loop:

```python
# /home/username/myproject/sync-script.py
from dirsync import sync
import time

def run():
    while True:
        # Perform task every 30 seconds
        sync('/source/folder', '/destination/folder', 'sync')
        time.sleep(30)

if __name__ == '__main__':
    run()
```

### Step 2: Create the Service File

Create a service file in `/etc/systemd/system/`:

```bash
sudo vi /etc/systemd/system/my-service.service
```

**Service file content:**

```ini
[Unit]
Description=My Python Script Service
After=multi-user.target

[Service]
Type=simple
Restart=always
RestartSec=10
WorkingDirectory=/home/username/myproject
ExecStart=/home/username/myproject/venv/bin/python /home/username/myproject/sync-script.py
User=username
Group=username

# Optional: Logging
StandardOutput=append:/var/log/my-service.log
StandardError=append:/var/log/my-service-error.log

[Install]
WantedBy=multi-user.target
```

`WantedBy` creates a dependency relationship that tells systemd:

"This service should be started when the system reaches multi-user.target"
What are targets?
Targets are systemd's way of grouping units and defining system states (similar to runlevels in SysV init):

multi-user.target: Normal multi-user system (command-line, networking available, no GUI)

**Key Configuration Options:**
- `Type=simple`: The process started is the main process
- `Restart=always`: Automatically restart if the service crashes
- `RestartSec=10`: Wait 10 seconds before restarting
- `WorkingDirectory`: Set the working directory for the script
- `ExecStart`: Full path to Python in venv + full path to script
- `User`/`Group`: Run as specific user (optional, omit to run as root)

## Method 2: Periodic Execution with Timers

This method uses systemd timers to run a script periodically, suitable for:
- Scheduled tasks (similar to cron)
- Scripts that should run once and exit
- Tasks that don't need to run continuously

### Step 1: Create Your Python Script

Example of a script that runs once and exits:

```python
# /home/username/myproject/backup-script.py
import os
import shutil
from datetime import datetime

def backup():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    source = '/data/important'
    destination = f'/backups/backup_{timestamp}'
    shutil.copytree(source, destination)
    print(f"Backup completed: {destination}")

if __name__ == '__main__':
    backup()
```

### Step 2: Create the Service File

```bash
sudo vi /etc/systemd/system/my-backup.service
```

**Service file content:**

```ini
[Unit]
Description=My Backup Script
Wants=my-backup.timer

[Service]
Type=oneshot
WorkingDirectory=/home/username/myproject
ExecStart=/home/username/myproject/venv/bin/python /home/username/myproject/backup-script.py
User=username
Group=username

# Optional: Logging
StandardOutput=append:/var/log/my-backup.log
StandardError=append:/var/log/my-backup-error.log

[Install]
WantedBy=multi-user.target
```

**Key Configuration Options:**
- `Type=oneshot`: The service runs once and exits
- `Wants=my-backup.timer`: Links to the timer unit

### Step 3: Create the Timer File

```bash
sudo vi /etc/systemd/system/my-backup.timer
```

**Timer file content:**

```ini
[Unit]
Description=Run my backup script periodically
Requires=my-backup.service

[Timer]
# Run 5 minutes after boot
OnBootSec=5min

# Run every hour
OnUnitActiveSec=1h

# Alternative: Run at specific times (calendar-based)
# OnCalendar=daily
# OnCalendar=*-*-* 02:00:00
# OnCalendar=Mon,Fri *-*-* 12:00:00

[Install]
WantedBy=timers.target
```

**Timer Options:**
- `OnBootSec`: Time after system boot
- `OnUnitActiveSec`: Time after the service last finished
- `OnCalendar`: Calendar-based scheduling (cron-like)

**Calendar Examples:**
- `daily` or `00:00:00`: Every day at midnight
- `hourly`: Every hour
- `*-*-* 02:00:00`: Every day at 2 AM
- `Mon,Fri *-*-* 12:00:00`: Monday and Friday at noon
- `*:0/15`: Every 15 minutes

## Service Management

### Reload Systemd

After creating or modifying service files:
```bash
sudo systemctl daemon-reload
```

### Enable Service (Start on Boot)

**For continuous services:**
```bash
sudo systemctl enable my-service.service
```

**For timer-based services:**
```bash
sudo systemctl enable my-backup.timer
```

### Start Service

**For continuous services:**
```bash
sudo systemctl start my-service.service
```

**For timer-based services:**
```bash
sudo systemctl start my-backup.timer
```

### Check Status

**For continuous services:**
```bash
sudo systemctl status my-service.service
```

**For timer-based services:**
```bash
# Check timer status
sudo systemctl status my-backup.timer

# Check service status
sudo systemctl status my-backup.service

# List all timers
systemctl list-timers
```

### Stop Service

```bash
sudo systemctl stop my-service.service
# or
sudo systemctl stop my-backup.timer
```

### Restart Service

```bash
sudo systemctl restart my-service.service
```

### Disable Service (Don't Start on Boot)

```bash
sudo systemctl disable my-service.service
# or
sudo systemctl disable my-backup.timer
```

### View Logs

```bash
# View service logs
sudo journalctl -u my-service.service

# Follow logs in real-time
sudo journalctl -u my-service.service -f

# View logs since boot
sudo journalctl -u my-service.service -b

# View last 100 lines
sudo journalctl -u my-service.service -n 100

# View logs from specific time
sudo journalctl -u my-service.service --since "2024-01-01 00:00:00"
```

## Troubleshooting

### Common Issues

1. **Service fails to start**
   - Check the service status: `sudo systemctl status my-service.service`
   - View detailed logs: `sudo journalctl -u my-service.service -n 50`
   - Verify Python path: Run `which python` inside your venv
   - Check file permissions: Ensure the service can access all files

2. **Script works manually but not as service**
   - Use absolute paths in your Python script (not relative paths)
   - Set `WorkingDirectory` in the service file
   - Ensure all required environment variables are set
   - Check that the user has necessary permissions

3. **Virtual environment not working**
   - Use full path to Python binary: `/path/to/venv/bin/python`
   - Verify venv exists: `ls -la /path/to/venv/bin/python`
   - Test manually: `/path/to/venv/bin/python /path/to/script.py`

4. **Timer not running**
   - Check if timer is active: `systemctl list-timers`
   - Verify timer is enabled: `sudo systemctl is-enabled my-backup.timer`
   - Check timer logs: `sudo journalctl -u my-backup.timer`

### Testing Tips

1. **Test your script manually first:**
   ```bash
   source /path/to/venv/bin/activate
   python /path/to/script.py
   ```

2. **Test with full paths (as service will run):**
   ```bash
   /path/to/venv/bin/python /path/to/script.py
   ```

3. **Run service in foreground for debugging:**
   ```bash
   sudo /path/to/venv/bin/python /path/to/script.py
   ```

### Useful Commands

```bash
# Reload systemd configuration
sudo systemctl daemon-reload

# Check if service is enabled
systemctl is-enabled my-service.service

# Check if service is active
systemctl is-active my-service.service

# View service unit file
systemctl cat my-service.service

# Edit service file
sudo systemctl edit --full my-service.service

# View all failed services
systemctl --failed

# Analyze boot time
systemd-analyze blame
```

## Example: Complete Setup

Here's a complete example for a periodic backup script:

### 1. Create virtual environment and install dependencies
```bash
cd /home/username/backups
python3 -m venv venv
source venv/bin/activate
pip install required-packages
deactivate
```

### 2. Create Python script
```bash
vi /home/username/backups/backup.py
```

### 3. Create service file
```bash
sudo vi /etc/systemd/system/backup.service
```

### 4. Create timer file
```bash
sudo vi /etc/systemd/system/backup.timer
```

### 5. Enable and start
```bash
sudo systemctl daemon-reload
sudo systemctl enable backup.timer
sudo systemctl start backup.timer
systemctl list-timers
```

## References

- [Understanding and Using systemd](https://www.linux.com/training-tutorials/understanding-and-using-systemd/)
- [Running a Python Script from systemd](https://johnsturgeon.me/2024/07/01/python-script-as-service/)
- [systemd.service Manual](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
- [systemd.timer Manual](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)
