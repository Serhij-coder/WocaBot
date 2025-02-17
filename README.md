# WocaBot
WocaBot is an automated bot that solves **WocaBee** tasks for you.

## Installation

### Windows:
1. Clone or download the repository.
2. Install Playwright:
    ```sh
    pip install playwright
    sudo npx playwright install
    ```
3. Configure **config.py**:
    - Comment out the line:
      ```python
      # import myLogin
      ```
    - Choose your browser (firefox, chromium, or webkit):
      ```python
      BROWSER = "firefox"
      ```
    - Enter your WocaBee login credentials:
      ```python
      LOGIN = "your_login"
      PASSWORD = "your_password"
      ```
4. You’re done! 🎉

---

### Linux:
1. Clone or download the repository.
2. Install Playwright:

    **For Arch Linux:**  
    ```sh
    sudo pacman -S python-playwright
    ```
    **For Ubuntu/Debian:**  
    ```sh
    sudo apt install python3-pip
    pip3 install playwright
    ```
    **For Fedora:**  
    ```sh
    sudo dnf install python3-pip
    pip3 install playwright
    ```
    **For CentOS/RHEL:**  
    ```sh
    sudo yum install python3-pip
    pip3 install playwright
    ```
    **For openSUSE:**  
    ```sh
    sudo zypper install python3-pip
    pip3 install playwright
    ```
3. Install browsers:
    ```sh
    playwright install
    ```
4. Configure **config.py**:
    - Comment out the line:
      ```python
      # import myLogin
      ```
    - Choose your browser (firefox, chromium, or webkit):
      ```python
      BROWSER = "firefox"
      ```
    - Enter your WocaBee login credentials:
      ```python
      LOGIN = "your_login"
      PASSWORD = "your_password"
      ```
5. You’re done! 🎉

---

### macOS:
🚧 **Coming Soon!**  

---

## Usage  
1. Run the program:  
    ```sh
    python main.py
    ```
2. In the browser window, select the package you want to complete.  
3. In the console window, press **Enter** to start the main loop.  
4. Wait while the bot completes the tasks.  
> A more user-friendly experience will be implemented soon.  

---

## ⚠️ Warnings  
1. **The bot currently cannot solve pexeso and picture-based exercises.** (Coming soon!)  
2. **The program is sensitive and may stop unexpectedly.**  
   - It’s best to leave it running without interruptions.  
3. **If the program crashes, all progress will be lost!**  
   - If the console stops printing messages, the program will close in 30 seconds.  
   - Save your progress before this happens!  

---
