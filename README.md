# ATLAS - Advanced Transport Loading System

[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](/)
[![License](https://img.shields.io/badge/License-Copyleft_2025-orange.svg)](/)
[![Python](https://img.shields.io/badge/Python-3.11-yellow.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

**ATLAS is a command-line application designed to streamline and manage transport loading operations.  It provides tools for efficient carrier and package management, intelligent loading plan generation, and insightful operational statistics, all within a user-friendly terminal interface.**

## Overview

ATLAS - Advanced Transport Loading System is a Python-based application built to simplify the complexities of managing carriers and packages in a transportation or logistics setting.  It offers a robust set of features accessible through a clear and intuitive command-line menu, enabling users to efficiently organize transport resources, optimize loading processes, and gain valuable insights into their operations.

Whether you are managing a small fleet or a larger transport operation, ATLAS provides the essential tools to enhance organization, improve loading efficiency, and gain a better understanding of your transport data.

## Features

*   **Carrier Management:**
    *   **Add New Carriers:** Easily register new carriers into the system, specifying their name and weight capacity.
    *   **View Carrier List:** Display a comprehensive list of registered carriers, including their ID, name, capacity, current status, number of packages loaded, total current load, and remaining capacity.

*   **Package Management:**
    *   **Add New Packages:** Quickly add new packages to the system, defining their weight and destination.
    *   **View Package List:** Show a detailed list of all registered packages, including their ID, weight, destination, current status, assigned carrier (if any), and loading timestamp.
    *   **Bulk Package Import:** Import multiple packages at once from a CSV file, streamlining data entry for large volumes of packages.

*   **Intelligent Loading Plan Generation:**
    *   **Automatic Package Assignment:** Generate an optimized loading plan that automatically assigns pending packages to available carriers based on carrier capacity and package weight, maximizing load efficiency.
    *   **Loading Plan Execution:**  Execute the generated loading plan to automatically assign packages to carriers in the database.

*   **Package Assignment to Carrier:**
    *   **Manual Assignment:** Manually assign specific pending packages to suitable carriers with available capacity, providing control over individual package assignments.

*   **Operational Statistics and Reporting:**
    *   **System Overview:** View key system statistics, including total carriers, total packages, loaded packages, pending packages, total package weight, and total carrier capacity.
    *   **Carrier Utilization:**  Display detailed carrier utilization statistics, showing each carrier's name, capacity, number of packages loaded, total load, and percentage utilization.
    *   **Destination Statistics:** Analyze package distribution by destination, providing insights into package counts, total weight, and average weight per destination.
    *   **Data Visualization:** Generate and save charts (PNG format) in a `charts` directory, visualizing carrier utilization and package distribution by destination for better data understanding.

*   **User-Friendly Command-Line Interface (CLI):**
    *   **Intuitive Menu System:** Navigate through application features using a clear and organized numbered menu.
    *   **Colored Output:** Utilizes `colorama` for visually enhanced and informative terminal output, making the application more pleasant to use.
    *   **Loading Animations:**  Provides visual feedback during processing tasks with loading animations, improving the user experience.
    *   **Fancy Text and Tables:**  Employs `tabulate` for well-formatted and readable tables and decorative text elements for a more polished interface.

## Technologies Used

ATLAS is built using Python 3.11 and leverages the following libraries:

*   **sqlite3:** For local database management to store carrier and package data persistently.
*   **pandas:** For efficient data manipulation, analysis, and creating DataFrames for tabular data display.
*   **colorama:** To enable cross-platform colored text output in the terminal, enhancing the user interface.
*   **tabulate:** For generating well-formatted and visually appealing tables in the command-line interface.
*   **datetime:** Python's built-in module for handling date and time operations, used for timestamping loading events.
*   **csv:** For handling CSV file input for bulk package import functionality.
*   **matplotlib:** For generating data visualizations, specifically charts for carrier utilization and destination distribution.
*   **pathlib:** For object-oriented filesystem path manipulation, used for creating the `charts` directory.
*   **time:** For implementing time delays and loading animations to improve user experience.
*   **os:** For interacting with the operating system, used for clearing the terminal screen.

## Setup and Installation

To run ATLAS locally, follow these steps:

1.  **Prerequisites:** Ensure you have Python 3.11 installed on your system. You can download Python from [https://www.python.org/](https://www.python.org/).2.  **Clone the Repository:**
    ```bash
    git clone [repository URL here] # Replace with your repository URL, e.g., git clone https://github.com/YourUsername/atlas.git
    cd atlas
    ```

3.  **Install Dependencies:** Navigate to the cloned repository directory in your terminal and install the required Python libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
    *(It is recommended to use a virtual environment to manage project dependencies. You can create one using `python -m venv venv` and activate it with `source venv/bin/activate` on Linux/macOS or `venv\Scripts\activate` on Windows before running the `pip install` command.)*

    **A `requirements.txt` file is included in the repository for easy installation of all dependencies.**

4.  **Run ATLAS:** Execute the main application script from your terminal:
    ```bash
    python your_atlas_script_name.py  # e.g., python atlas.py or python main.py
    ```
    *(Replace `your_atlas_script_name.py` with the actual name of your main Python script file if it's not `atlas.py`.)*

## Usage

Once ATLAS is running, you will be presented with the main menu. Use the numbered options to navigate and interact with the system:

1.  **Add New Carrier:** Choose option `1` to register a new carrier by providing its name and capacity.
2.  **Add New Package:** Select option `2` to add a new package, specifying its weight and destination.
3.  **Show Carriers List:** Option `3` displays a formatted table of all carriers with their details and current load status.
4.  **Show Packages List:** Option `4` shows a table of all packages and their status, including carrier assignment and loading time.
5.  **Assign Package to Carrier:** Use option `5` to manually assign a pending package to an available carrier. You will be prompted to enter the Carrier ID and Package ID.
6.  **Bulk Import Packages:** Option `6` allows you to import packages from a CSV file.  Ensure your CSV file (`packages.csv` for example) is in the correct format (weight,destination columns) and provide the file path when prompted.
7.  **Generate Loading Plan:** Select option `7` to automatically generate and optionally execute a loading plan that assigns all pending packages to carriers based on capacity.
8.  **View Statistics:** Choose option `8` to view comprehensive system statistics, carrier utilization reports, destination package analysis, and generate charts in the `charts` directory.
9.  **Exit:** Option `0` will gracefully exit the ATLAS application.

**Example Workflow:**

1.  **Start ATLAS:** Run `python your_atlas_script_name.py` in your terminal.
2.  **Add Carriers:** Use option `1` to add a few carriers with their respective capacities (e.g., Carrier A - 1000kg, Carrier B - 500kg).
3.  **Bulk Import Packages:** Use option `6` to import packages from a `packages.csv` file or manually add packages using option `2`.
4.  **Generate Loading Plan:** Select option `7` to create an optimized loading plan. Review the plan and choose to execute it.
5.  **View Statistics:** Use option `8` to see carrier utilization and other operational statistics, and check the `charts` directory for generated charts.
6.  **Exit:** Select option `0` when finished.


## Data Storage

ATLAS utilizes a local SQLite database file named `atlas.db` to store all carrier and package information. This database file is created in the same directory where you run the application and ensures data persistence between application sessions.

## License

**Copyleft 2025 M2GH.**  [MIT License](https://opensource.org/licenses/MIT).

## Author

Developed by M2GH

## Version

0.1.0
