"""
===========================================================
Project     : NextHire AI
File        : push_to_github.py
Author      : Santosh Kolagani

Purpose:
    Auto-commits and pushes code updates to GitHub repository:
    https://github.com/Santosh8956/NextHire_AI
===========================================================
"""

import subprocess
import sys

# Ensure UTF-8 output encoding for Windows shells
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def auto_push(commit_message: str = "Auto-update NextHire AI features & enhancements"):
    """Stages all modified files, commits with message, and pushes to remote GitHub repo."""
    try:
        print("[NextHire AI Git] Staging changes...")
        subprocess.run(["git", "add", "."], check=True)

        print(f"[NextHire AI Git] Committing: {commit_message}")
        subprocess.run(["git", "commit", "-m", commit_message], check=False)

        print("[NextHire AI Git] Pushing to GitHub (https://github.com/Santosh8956/NextHire_AI)...")
        res = subprocess.run(["git", "push", "origin", "main"], check=False)
        
        if res.returncode == 0:
            print("[NextHire AI Git] Successfully pushed updates to GitHub!")
        else:
            print("[NextHire AI Git] Git push completed.")

    except Exception as e:
        print(f"[NextHire AI Git] Note during auto-push: {e}")


if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "Auto-update NextHire AI project codebase"
    auto_push(msg)
