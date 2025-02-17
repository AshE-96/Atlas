"""
ATLAS - Advanced Transport Loading System
Developed by M2GH
Version 0.1.0
"""

import sqlite3
from datetime import datetime
import pandas as pd
import os
from colorama import init, Fore, Back, Style
from tabulate import tabulate
import time
import csv
import matplotlib.pyplot as plt
from pathlib import Path

# Initialize colorama for cross-platform colored output
init()

def show_splash_screen():
    clear_screen()
    splash = f"""
{Fore.CYAN}
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    █                                                  █
    █   █▀▄▀█ ▄▀█ █▀▀ █ █▀▀   █▀█ █▀█ █▀ ▀█▀ █▀▄▀█ █▀  █
    █   █ ▀ █ █▀█ █▄█ █ █▄▄   █▀▀ █▄█ ▄█  █  █ ▀ █ ▄█  █
    █                                                  █
    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

{Fore.GREEN}
    ╔════════════════════════════════════════════════════╗
    ║             A T L A S  -  v1.0.0                   ║
    ║     Advanced Transport Loading System              ║
    ║                                                    ║
    ║     Developed by: M2GH                             ║
    ║     Copyleft  2025                                 ║
    ╚════════════════════════════════════════════════════╝
{Style.RESET_ALL}
    """
    print(splash)
    time.sleep(2)

def create_fancy_text(text, padding=1):
    width = len(text) + 2 * padding
    border = f"╔{'═' * width}╗"
    content = f"║{' ' * padding}{text}{' ' * padding}║"
    bottom = f"╚{'═' * width}╝"
    return f"\n{border}\n{content}\n{bottom}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration=1):
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{Fore.CYAN}Loading {animation[i % len(animation)]}", end="")
        time.sleep(0.1)
        i += 1
    print(f"\r{' ' * 20}\r", end="")

def init_db():
    conn = sqlite3.connect('atlas.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS carriers
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  capacity FLOAT,
                  status TEXT,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS packages
                 (id INTEGER PRIMARY KEY,
                  weight FLOAT,
                  destination TEXT,
                  status TEXT,
                  carrier_id INTEGER,
                  loading_time TIMESTAMP,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    conn.commit()
    conn.close()

def show_menu():
    clear_screen()
    print(Fore.CYAN + create_fancy_text(" ATLAS - Advanced Transport Loading System "))
    print(Fore.YELLOW + "\n╔════════════════ MAIN MENU ════════════════╗")
    print(Fore.YELLOW + "║                                            ║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  1. Add New Carrier                        " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  2. Add New Package                        " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  3. Show Carriers List                     " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  4. Show Packages List                     " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  5. Assign Package to Carrier              " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  6. Bulk Import Packages                   " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  7. Generate Loading Plan                  " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  8. View Statistics                        " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.RED + "  0. Exit                                   " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║                                            ║")
    print(Fore.YELLOW + "╚════════════════════════════════════════════╝" + Style.RESET_ALL)

def add_carrier():
    clear_screen()
    print(Fore.CYAN + create_fancy_text(" ADD NEW CARRIER "))
    name = input(Fore.GREEN + "\nEnter carrier name: " + Fore.WHITE)
    while True:
        try:
            capacity = float(input(Fore.GREEN + "Enter carrier capacity (kg): " + Fore.WHITE))
            if capacity > 0:
                break
            print(Fore.RED + "Capacity must be greater than 0!")
        except ValueError:
            print(Fore.RED + "Please enter a valid number!")
    
    conn = sqlite3.connect('atlas.db')
    c = conn.cursor()
    c.execute('INSERT INTO carriers (name, capacity, status) VALUES (?, ?, ?)',
              (name, capacity, 'Ready'))
    conn.commit()
    conn.close()
    
    loading_animation()
    print(Fore.GREEN + f"\n✓ Carrier '{name}' successfully added!")
    input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

def add_package():
    clear_screen()
    print(Fore.CYAN + create_fancy_text(" ADD NEW PACKAGE "))
    while True:
        try:
            weight = float(input(Fore.GREEN + "\nEnter package weight (kg): " + Fore.WHITE))
            if weight > 0:
                break
            print(Fore.RED + "Weight must be greater than 0!")
        except ValueError:
            print(Fore.RED + "Please enter a valid number!")
            
    destination = input(Fore.GREEN + "Enter package destination: " + Fore.WHITE)
    
    conn = sqlite3.connect('atlas.db')
    c = conn.cursor()
    c.execute('INSERT INTO packages (weight, destination, status) VALUES (?, ?, ?)',
              (weight, destination, 'Pending'))
    conn.commit()
    conn.close()
    
    loading_animation()
    print(Fore.GREEN + f"\n✓ Package ({weight}kg) to {destination} successfully added!")
    input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

def show_carriers():
    clear_screen()
    print(Fore.CYAN + create_fancy_text(" CARRIERS LIST "))
    conn = sqlite3.connect('atlas.db')
    df = pd.read_sql_query('''
        SELECT 
            c.id,
            c.name,
            c.capacity,
            c.status,
            COUNT(p.id) as packages,
            COALESCE(SUM(p.weight), 0) as total_load,
            c.capacity - COALESCE(SUM(p.weight), 0) as remaining_capacity
        FROM carriers c
        LEFT JOIN packages p ON c.id = p.carrier_id AND p.status = 'Loaded'
        GROUP BY c.id
    ''', conn)
    conn.close()
    
    if len(df) == 0:
        print(Fore.RED + "\nNo carriers registered yet!")
    else:
        print("\n" + tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    
    input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

def show_packages():
    clear_screen()
    print(Fore.CYAN + create_fancy_text(" PACKAGES LIST "))
    conn = sqlite3.connect('atlas.db')
    df = pd.read_sql_query('''
        SELECT 
            p.id,
            p.weight,
            p.destination,
            p.status,
            COALESCE(c.name, '-') as carrier,
            p.loading_time
        FROM packages p
        LEFT JOIN carriers c ON p.carrier_id = c.id
    ''', conn)
    conn.close()
    
    if len(df) == 0:
        print(Fore.RED + "\nNo packages registered yet!")
    else:
        print("\n" + tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    
    input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

def assign_package():
    clear_screen()
    print(Fore.CYAN + create_fancy_text(" ASSIGN PACKAGE TO CARRIER "))
    
    conn = sqlite3.connect('atlas.db')
    print(Fore.GREEN + "\nAvailable Carriers:")
    carriers_df = pd.read_sql_query('''
        SELECT 
            c.id,
            c.name,
            c.capacity,
            c.status,
            COALESCE(SUM(p.weight), 0) as current_load,
            c.capacity - COALESCE(SUM(p.weight), 0) as available_capacity
        FROM carriers c
        LEFT JOIN packages p ON c.id = p.carrier_id AND p.status = 'Loaded'
        GROUP BY c.id
        HAVING available_capacity > 0
    ''', conn)
    
    if len(carriers_df) == 0:
        print(Fore.RED + "\nNo available carriers!")
        conn.close()
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    print("\n" + tabulate(carriers_df, headers='keys', tablefmt='fancy_grid', showindex=False))
    
    print(Fore.GREEN + "\nPending Packages:")
    packages_df = pd.read_sql_query('''
        SELECT id, weight, destination, status
        FROM packages
        WHERE status = 'Pending'
    ''', conn)
    
    if len(packages_df) == 0:
        print(Fore.RED + "\nNo pending packages!")
        conn.close()
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    print("\n" + tabulate(packages_df, headers='keys', tablefmt='fancy_grid', showindex=False))
    
    try:
        carrier_id = int(input(Fore.YELLOW + "\nEnter carrier ID: " + Fore.WHITE))
        package_id = int(input(Fore.YELLOW + "Enter package ID: " + Fore.WHITE))
    except ValueError:
        print(Fore.RED + "\n✗ Invalid input!")
        conn.close()
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    c = conn.cursor()
    
    # Verify carrier exists and has capacity
    c.execute('''
        SELECT capacity - COALESCE(SUM(p.weight), 0) as available_capacity
        FROM carriers c
        LEFT JOIN packages p ON c.id = p.carrier_id AND p.status = 'Loaded'
        WHERE c.id = ?
        GROUP BY c.id
    ''', (carrier_id,))
    result = c.fetchone()
    
    if not result:
        print(Fore.RED + "\n✗ Carrier not found!")
        conn.close()
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    available_capacity = result[0]
    
    # Verify package exists and is pending
    c.execute('SELECT weight, status FROM packages WHERE id = ?', (package_id,))
    result = c.fetchone()
    
    if not result:
        print(Fore.RED + "\n✗ Package not found!")
        conn.close()
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    package_weight, package_status = result
    
    if package_status != 'Pending':
        print(Fore.RED + "\n✗ Package is not pending!")
        conn.close()
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    loading_animation()
    
    if package_weight <= available_capacity:
        c.execute('''
            UPDATE packages 
            SET carrier_id = ?, status = 'Loaded', loading_time = ? 
            WHERE id = ?
        ''', (carrier_id, datetime.now(), package_id))
        conn.commit()
        print(Fore.GREEN + "\n✓ Package successfully assigned to carrier!")
    else:
        print(Fore.RED + "\n✗ Error: Insufficient carrier capacity!")
    
    conn.close()
    input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

def bulk_import_packages():
    clear_screen()
    print(Fore.CYAN + create_fancy_text(" BULK IMPORT PACKAGES "))
    print(Fore.GREEN + "\nPrepare a CSV file with columns: weight,destination")
    print(Fore.GREEN + "Example: packages.csv")
    print(Fore.WHITE + "\nweight,destination")
    print("5.2,Tehran")
    print("3.7,Shiraz")
    print("2.1,Mashhad")
    
    file_path = input(Fore.YELLOW + "\nEnter CSV file path: " + Fore.WHITE)
    
    if not os.path.exists(file_path):
        print(Fore.RED + "\n✗ File not found!")
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    conn = sqlite3.connect('atlas.db')
    c = conn.cursor()
    
    success_count = 0
    error_count = 0
    
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    weight = float(row['weight'])
                    destination = row['destination']
                    
                    if weight <= 0:
                        error_count += 1
                        continue
                        
                    c.execute('''
                        INSERT INTO packages (weight, destination, status)
                        VALUES (?, ?, ?)
                    ''', (weight, destination, 'Pending'))
                    
                    success_count += 1
                    
                except (ValueError, KeyError):
                    error_count += 1
                    continue
        
        conn.commit()
        loading_animation()
        print(Fore.GREEN + f"\n✓ Successfully imported {success_count} packages!")
        if error_count > 0:
            print(Fore.RED + f"✗ Failed to import {error_count} packages.")
            
    except Exception as e:
        print(Fore.RED + f"\n✗ Error reading file: {str(e)}")
    
    conn.close()
    input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

def generate_loading_plan():
    clear_screen()
    print(Fore.CYAN + create_fancy_text(" GENERATE LOADING PLAN "))
    
    conn = sqlite3.connect('atlas.db')
    c = conn.cursor()
    
    # Get all carriers with their current load
    carriers_df = pd.read_sql_query('''
        SELECT 
            c.id,
            c.name,
            c.capacity,
            COALESCE(SUM(p.weight), 0) as current_load,
            c.capacity - COALESCE(SUM(p.weight), 0) as available_capacity
        FROM carriers c
        LEFT JOIN packages p ON c.id = p.carrier_id AND p.status = 'Loaded'
        GROUP BY c.id
        HAVING available_capacity > 0
        ORDER BY available_capacity DESC
    ''', conn)
    
    # Get all pending packages
    packages_df = pd.read_sql_query('''
        SELECT id, weight, destination
        FROM packages
        WHERE status = 'Pending'
        ORDER BY weight DESC
    ''', conn)
    
    if len(carriers_df) == 0:
        print(Fore.RED + "\nNo available carriers!")
        conn.close()
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    if len(packages_df) == 0:
        print(Fore.RED + "\nNo pending packages!")
        conn.close()
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    print(Fore.GREEN + "\nGenerating optimal loading plan...")
    loading_animation(2)
    
    assignments = []
    
    # Simple bin-packing algorithm
    for _, package in packages_df.iterrows():
        for _, carrier in carriers_df.iterrows():
            if package['weight'] <= carrier['available_capacity']:
                assignments.append({
                    'carrier_id': carrier['id'],
                    'carrier_name': carrier['name'],
                    'package_id': package['id'],
                    'package_weight': package['weight'],
                    'destination': package['destination']
                })
                carrier['available_capacity'] -= package['weight']
                break
    
    if not assignments:
        print(Fore.RED + "\nCouldn't generate a loading plan - insufficient capacity!")
        conn.close()
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
        return
    
    # Display the loading plan
    df = pd.DataFrame(assignments)
    print(Fore.GREEN + "\nProposed Loading Plan:")
    print("\n" + tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    
    if input(Fore.YELLOW + "\nExecute this loading plan? (y/n): " + Fore.WHITE).lower() == 'y':
        for assignment in assignments:
            c.execute('''
                UPDATE packages 
                SET carrier_id = ?, status = 'Loaded', loading_time = ? 
                WHERE id = ?
            ''', (assignment['carrier_id'], datetime.now(), assignment['package_id']))
        
        conn.commit()
        loading_animation()
        print(Fore.GREEN + f"\n✓ Successfully assigned {len(assignments)} packages!")
    
    conn.close()
    input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

def view_statistics():
    clear_screen()
    print(Fore.CYAN + create_fancy_text(" SYSTEM STATISTICS "))
    
    conn = sqlite3.connect('atlas.db')
    
    # General statistics
    stats_df = pd.read_sql_query('''
        SELECT
            (SELECT COUNT(*) FROM carriers) as total_carriers,
            (SELECT COUNT(*) FROM packages) as total_packages,
            (SELECT COUNT(*) FROM packages WHERE status = 'Loaded') as loaded_packages,
            (SELECT COUNT(*) FROM packages WHERE status = 'Pending') as pending_packages,
            (SELECT COALESCE(SUM(weight), 0) FROM packages) as total_weight,
            (SELECT COALESCE(SUM(capacity), 0) FROM carriers) as total_capacity
    ''', conn)
    
    # Carrier utilization
    carrier_stats = pd.read_sql_query('''
        SELECT 
            c.name,
            c.capacity,
            COUNT(p.id) as packages,
            COALESCE(SUM(p.weight), 0) as total_load,
            ROUND(COALESCE(SUM(p.weight), 0) * 100.0 / c.capacity, 1) as utilization
        FROM carriers c
        LEFT JOIN packages p ON c.id = p.carrier_id AND p.status = 'Loaded'
        GROUP BY c.id
        ORDER BY utilization DESC
    ''', conn)
    
    # Destination statistics
    dest_stats = pd.read_sql_query('''
        SELECT 
            destination,
            COUNT(*) as package_count,
            ROUND(SUM(weight), 1) as total_weight,
            ROUND(AVG(weight), 1) as avg_weight
        FROM packages
        GROUP BY destination
        ORDER BY package_count DESC
    ''', conn)
    
    conn.close()
    
    # Display statistics
    print(Fore.GREEN + "\nSystem Overview:")
    print(Fore.WHITE + "═" * 50)
    print(f"Total Carriers: {stats_df['total_carriers'][0]}")
    print(f"Total Packages: {stats_df['total_packages'][0]}")
    print(f"Loaded Packages: {stats_df['loaded_packages'][0]}")
    print(f"Pending Packages: {stats_df['pending_packages'][0]}")
    print(f"Total Weight: {stats_df['total_weight'][0]:.1f} kg")
    print(f"Total Capacity: {stats_df['total_capacity'][0]:.1f} kg")
    
    print(Fore.GREEN + "\nCarrier Utilization:")
    print(Fore.WHITE + "═" * 50)
    print(tabulate(carrier_stats, headers='keys', tablefmt='fancy_grid', showindex=False))
    
    print(Fore.GREEN + "\nDestination Statistics:")
    print(Fore.WHITE + "═" * 50)
    print(tabulate(dest_stats, headers='keys', tablefmt='fancy_grid', showindex=False))
    
    # Generate and save charts
    try:
        # Create charts directory if it doesn't exist
        Path("charts").mkdir(exist_ok=True)
        
        # Carrier Utilization Chart
        plt.figure(figsize=(10, 6))
        plt.bar(carrier_stats['name'], carrier_stats['utilization'])
        plt.title('Carrier Utilization')
        plt.xlabel('Carriers')
        plt.ylabel('Utilization (%)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('charts/carrier_utilization.png')
        
        # Destination Distribution Chart
        plt.figure(figsize=(10, 6))
        plt.pie(dest_stats['package_count'], labels=dest_stats['destination'], autopct='%1.1f%%')
        plt.title('Package Distribution by Destination')
        plt.tight_layout()
        plt.savefig('charts/destination_distribution.png')
        
        print(Fore.GREEN + "\nCharts have been saved to the 'charts' directory!")
        
    except Exception as e:
        print(Fore.RED + f"\nError generating charts: {str(e)}")
    
    input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

def main():
    show_splash_screen()
    init_db()
    while True:
        show_menu()
        choice = input(Fore.GREEN + "\nEnter your choice (0-8): " + Fore.WHITE)
        
        if choice == '1':
            add_carrier()
        elif choice == '2':
            add_package()
        elif choice == '3':
            show_carriers()
        elif choice == '4':
            show_packages()
        elif choice == '5':
            assign_package()
        elif choice == '6':
            bulk_import_packages()
        elif choice == '7':
            generate_loading_plan()
        elif choice == '8':
            view_statistics()
        elif choice == '0':
            clear_screen()
            print(Fore.CYAN + create_fancy_text(" Thank you for using ATLAS! "))
            print(Fore.GREEN + "\nDeveloped by M2GH")
            time.sleep(1.5)
            break
        else:
            print(Fore.RED + "\nInvalid option!")
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

if __name__ == '__main__':
    main()
