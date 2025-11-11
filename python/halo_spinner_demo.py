#!/usr/bin/env python3
"""
Halo Spinner Demonstration Script
Shows various halo spinner functionalities including basic spinners,
color changes, success/failure states, and advanced features.
"""

import time
try:
    from halo import Halo
except ImportError:
    print("❌ halo not installed. Install with: pip install halo")
    exit(1)

def demo_basic_spinner():
    """Demonstrate basic halo spinner functionality"""
    print("=== Basic Halo Spinner Demo ===")
    
    spinner = Halo(text='Loading basic data...', spinner='dots')
    spinner.start()
    time.sleep(2)
    spinner.succeed('✅ Basic loading complete!')

def demo_context_manager():
    """Demonstrate halo as context manager"""
    print("\n=== Context Manager Demo ===")
    
    with Halo(text='Processing with context manager...', spinner='line') as spinner:
        time.sleep(2)
        spinner.succeed('✅ Context manager complete!')

def demo_dynamic_updates():
    """Demonstrate dynamic text and color updates"""
    print("\n=== Dynamic Updates Demo ===")
    
    spinner = Halo(text='Starting process...', spinner='dots', color='blue')
    spinner.start()
    
    time.sleep(1)
    spinner.text = 'Processing data...'
    spinner.color = 'yellow'
    
    time.sleep(1)
    spinner.text = 'Almost finished...'
    spinner.color = 'green'
    
    time.sleep(1)
    spinner.succeed('✅ Dynamic updates complete!')

def demo_different_spinners():
    """Demonstrate different spinner styles"""
    print("\n=== Different Spinner Styles Demo ===")
    
    spinners = ['dots', 'line', 'pipe', 'dots12', 'arrow3', 'bouncingBar']
    
    for spinner_name in spinners:
        spinner = Halo(text=f'Testing {spinner_name} spinner...', spinner=spinner_name)
        spinner.start()
        time.sleep(1.5)
        spinner.succeed(f'✅ {spinner_name} complete')

def demo_colors():
    """Demonstrate different colors"""
    print("\n=== Color Variations Demo ===")
    
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    
    for color in colors:
        spinner = Halo(text=f'Testing {color} color...', spinner='dots', color=color)
        spinner.start()
        time.sleep(0.8)
        spinner.succeed(f'✅ {color} complete')

def demo_success_failure():
    """Demonstrate success, failure, and warning states"""
    print("\n=== Success/Failure States Demo ===")
    
    # Success
    spinner = Halo(text='Attempting successful operation...', spinner='dots')
    spinner.start()
    time.sleep(1)
    spinner.succeed('✅ Operation succeeded!')
    
    # Failure
    spinner = Halo(text='Attempting operation that will fail...', spinner='dots')
    spinner.start()
    time.sleep(1)
    spinner.fail('❌ Operation failed!')
    
    # Warning
    spinner = Halo(text='Attempting operation with warning...', spinner='dots')
    spinner.start()
    time.sleep(1)
    spinner.warn('⚠️  Operation completed with warnings')
    
    # Info
    spinner = Halo(text='Providing information...', spinner='dots')
    spinner.start()
    time.sleep(1)
    spinner.info('ℹ️  Information provided')

def demo_countdown_timer():
    """Demonstrate countdown timer functionality"""
    print("\n=== Countdown Timer Demo ===")
    
    duration = 5
    spinner = Halo(text='Countdown starting...', spinner='clock')
    spinner.start()
    
    for i in range(duration * 10):
        remaining = duration - (i / 10)
        spinner.text = f'Retrying in {remaining:.1f}s...'
        time.sleep(0.1)
    
    spinner.succeed('✅ Countdown complete!')

def demo_api_simulation():
    """Simulate API calls with error handling"""
    print("\n=== API Call Simulation Demo ===")
    
    pages = 4
    total_records = 0
    failed_pages = []
    
    for page in range(1, pages + 1):
        spinner = Halo(text=f'Fetching page {page}...', spinner='dots', color='blue')
        spinner.start()
        
        try:
            # Simulate API delay
            time.sleep(0.5)
            
            # Simulate occasional failure
            if page == 3:
                raise Exception("Simulated API timeout")
            
            # Process records
            records_in_page = 10
            for record in range(records_in_page):
                total_records += 1
                spinner.text = f'Fetching page {page}... ({total_records} records)'
                time.sleep(0.1)
            
            spinner.succeed(f'✅ Page {page} complete ({records_in_page} records)')
            
        except Exception as e:
            failed_pages.append(page)
            spinner.fail(f'❌ Page {page} failed: {str(e)}')
    
    # Summary
    if failed_pages:
        print(f"⚠️  Completed with errors. Failed pages: {failed_pages}")
    else:
        print(f"🎉 API simulation complete! Total records: {total_records}")

def demo_advanced_features():
    """Demonstrate advanced halo features"""
    print("\n=== Advanced Features Demo ===")
    
    # Spinner with custom symbols
    spinner = Halo(text='Custom spinner...', spinner={'interval': 100, 'frames': ['🌍', '🌎', '🌏']})
    spinner.start()
    time.sleep(2)
    spinner.succeed('✅ Custom spinner complete!')
    
    # Enabled/disabled demonstration
    spinner = Halo(text='This spinner can be disabled...', spinner='dots')
    spinner.start()
    time.sleep(1)
    
    spinner.stop()
    print("🔇 Spinner stopped (but process continues)")
    time.sleep(1)
    
    spinner.start()
    time.sleep(1)
    spinner.succeed('✅ Spinner restarted and completed!')

if __name__ == "__main__":
    print("Halo Spinner Demonstration")
    print("===========================")
    
    try:
        demo_basic_spinner()
        demo_context_manager()
        demo_dynamic_updates()
        demo_different_spinners()
        demo_colors()
        demo_success_failure()
        demo_countdown_timer()
        demo_api_simulation()
        demo_advanced_features()
        
        print("\n🎉 All halo demonstrations complete!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")