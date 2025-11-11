#!/usr/bin/env python3
"""
Yaspin Spinner Demonstration Script
Shows various yaspin spinner functionalities including basic spinners,
dynamic text updates, success/failure states, and countdown timers.
"""

import time
from yaspin import yaspin
from yaspin.spinners import Spinners

def demo_basic_spinner():
    """Demonstrate basic spinner functionality"""
    print("=== Basic Yaspin Spinner Demo ===")
    
    with yaspin(text="Loading basic data...") as spinner:
        time.sleep(2)
        spinner.ok("✅ Basic loading complete!")

def demo_dynamic_text():
    """Demonstrate dynamic text updates during spinning"""
    print("\n=== Dynamic Text Updates Demo ===")
    
    with yaspin(text="Processing...") as spinner:
        for i in range(1, 6):
            spinner.text = f"Processing item {i}/5..."
            time.sleep(0.8)
        spinner.succeed("✅ All items processed!")

def demo_countdown_timer():
    """Demonstrate countdown timer with spinner"""
    print("\n=== Countdown Timer Demo ===")
    
    duration = 5
    with yaspin(text="Countdown starting...") as spinner:
        for i in range(duration * 10):
            remaining = duration - (i / 10)
            spinner.text = f"Retrying in {remaining:.1f}s..."
            time.sleep(0.1)
        spinner.succeed("✅ Countdown complete!")

def demo_different_spinners():
    """Demonstrate different spinner styles"""
    print("\n=== Different Spinner Styles Demo ===")
    
    spinners = [
        (Spinners.dots, "dots"),
        (Spinners.line, "line"),
        (Spinners.pipe, "pipe"),
        (Spinners.dots12, "dots12")
    ]
    
    for spinner_style, name in spinners:
        with yaspin(spinner=spinner_style, text=f"Testing {name} spinner...") as spinner:
            time.sleep(1.5)
            spinner.ok(f"✅ {name} complete")

def demo_success_failure():
    """Demonstrate success and failure states"""
    print("\n=== Success/Failure States Demo ===")
    
    # Success example
    with yaspin(text="Attempting successful operation...") as spinner:
        time.sleep(1)
        spinner.succeed("✅ Operation succeeded!")
    
    # Failure example
    with yaspin(text="Attempting operation that will fail...") as spinner:
        time.sleep(1)
        spinner.fail("❌ Operation failed!")
    
    # Warning example
    with yaspin(text="Attempting operation with warning...") as spinner:
        time.sleep(1)
        spinner.write("⚠️  Operation completed with warnings")

def demo_api_simulation():
    """Simulate API calls with yaspin spinners"""
    print("\n=== API Call Simulation Demo ===")
    
    pages = 3
    total_records = 0
    
    for page in range(1, pages + 1):
        with yaspin(text=f"Fetching page {page}...") as spinner:
            # Simulate API call delay
            time.sleep(1)
            
            # Simulate processing records
            records_in_page = 10
            for record in range(records_in_page):
                total_records += 1
                spinner.text = f"Fetching page {page}... ({total_records} records total)"
                time.sleep(0.1)
            
            spinner.succeed(f"✅ Page {page} complete ({records_in_page} records)")
    
    print(f"🎉 API simulation complete! Total records: {total_records}")

if __name__ == "__main__":
    print("Yaspin Spinner Demonstration")
    print("============================")
    
    try:
        demo_basic_spinner()
        demo_dynamic_text()
        demo_countdown_timer()
        demo_different_spinners()
        demo_success_failure()
        demo_api_simulation()
        
        print("\n🎉 All yaspin demonstrations complete!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
    except ImportError:
        print("❌ yaspin not installed. Install with: pip install yaspin")