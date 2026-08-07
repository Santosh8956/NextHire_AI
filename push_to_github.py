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


def auto_push(commit_message: str = "Auto-update NextHire AI features & enhancements"):
    """Stages all modified files, commits with message, and pushes to remote GitHub repo."""
    try:
        print("📦 Staging changes...")
        subprocess.run(["git", "add", "."], check=True)

        print(f"📝 Committing: {commit_message}")
        subprocess.run(["git", "commit", "-m", commit_message], check=False)

        print("🚀 Pushing to GitHub (https://github.com/Santosh8956/NextHire_AI)...")
        res = subprocess.run(["git", "push", "-u", "origin", "main"], check=False)
        
        if res.returncode == 0:
            print("✅ Successfully pushed to GitHub!")
        else:
            print("ℹ️ Git push step completed. Ensure remote origin URL and GitHub authentication credentials are set.")

    except Exception as e:
        print(f"⚠️ Error during auto-push: {e}")


if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "Auto-update NextHire AI project codebase"
    auto_push(msg)
