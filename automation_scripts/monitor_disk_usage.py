#!/usr/bin/env python3

import os
import shutil
import smtplib
from email.message import EmailMessage

# Configuration
THRESHOLD_PERCENT = 80
ALERT_EMAIL = "user@example.com"


def check_disk_usage(path='/'):
    total, used, free = shutil.disk_usage(path)
    percent_used = used / total * 100
    return percent_used


def send_alert(percent):
    msg = EmailMessage()
    msg.set_content(f"Warning: Disk usage has exceeded {percent:.1f}%")
    msg['Subject'] = 'Disk Usage Alert'
    msg['From'] = 'monitor@example.com'
    msg['To'] = ALERT_EMAIL

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    usage = check_disk_usage()
    if usage > THRESHOLD_PERCENT:
        print(f"Disk usage is critically high: {usage:.1f}%")
        send_alert(usage)
    else:
        print(f"Disk usage is OK: {usage:.1f}%")
