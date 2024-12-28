# Getting Started

## Staring the Application
When running the application locally, the user first needs to run it. To do this, you need to;
1. Install Python; to install it follow the instructions for your operating system;
   * **Windows**
      * Using Winget (_recommended_)
         1. Open Windows Terminal: Search for "Terminal" in the Start Menu and open it.
         2. Install Python: Execute the following command:
         ```bash
         winget install --id Python.Python.x64 
         ```
      * Manual Installation
         1. Download: Go to the official Python website (https://www.python.org/downloads/windows/) and download the latest installer.
         2. Run the installer:
           Important: During installation, check the box that says "Add Python 3.x to PATH." This makes Python accessible from the command prompt.
           Proceed with the installation as guided by the installer.
   * **macOS** 
      * Using Homebrew (_recommended_)
         1. Install Homebrew: If you don't have Homebrew, install it by following the instructions on their official website (https://brew.sh/).
         2. Install Python: Open Terminal and execute:
            ```bash
            brew install python3
            ```
      * Manual Installation
         1. Download: Download the macOS installer from the official Python website (https://www.python.org/downloads/macos/).
         2. Open the installer: Follow the on-screen instructions.
                Important: Make sure to add Python to your system's PATH during installation.
   * **Linux**
      * Using apt (deb - Debian, Ubuntu, etc.)
         ```bash
         sudo apt update
         sudo apt install python3 
         ```
      * Using dnf (redhat - RHEL, CentOS, Fedora)
         ```bash
         sudo dnf update
         sudo dnf install python3
         ```
      * Using pacman (arch)
         ```bash
         sudo pacman -Syu
         sudo pacman -S python
         ```
      * Manual Installation 
         1. Download: Download the source code from Python's official website (https://www.python.org/downloads/source/).
         2. Extract and build:
            ```bash
            tar -xf Python-3.x.x.tgz 
            cd Python-3.x.x
            ./configure --enable-optimizations 
            sudo make altinstall 
            ```
         (Using altinstall avoids conflicts with the system's default Python installation)
2. Run the app
   * Open a terminal in the Dog-Breed-Finder directory (folder)
   * Run the script
     ```Bash
     python3 app.py
     ```

## Accessing the Application
1. Open the Dog Breed Finder in your web browser by navigating to the provided URL or `http://127.0.0.1:5000` if running locally.
2. Use the navigation menu to access the app’s features:
    - **Breed Information**: Learn about specific dog breeds.
    - **Search**: Find dog breeds that suit your preferences and living situation.