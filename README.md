🧠 Auto TER Fillup

Auto TER Fillup is a lightweight Python automation script that helps you quickly fill out Teacher Evaluation Reports (TER) at your university. It uses pyautogui to simulate keyboard inputs and pyperclip to handle copy-paste — automating the repetitive task of navigating and completing TER forms.

> ⚠️ This script interacts with your screen directly. Make sure the TER form is open and active before running.

---

✨ Features

- ⏱️ Delays start to give you time to prepare
- 🔄 Automatically navigates and fills TER form fields
- 📝 Pasts pre-set responses like "Everything" and "Nothing"
- ⚙️ Simple to modify for your own feedback style

---

## 🛠 Tech Used

- Python 3
- [`pyautogui`](https://pyautogui.readthedocs.io/en/latest/) – for simulating keyboard inputs  
- [`pyperclip`](https://pyperclip.readthedocs.io/en/latest/) – for copying/pasting text  
- `time` – for sleep delays

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install pyautogui pyperclip
