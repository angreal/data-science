import angreal
import os
import subprocess
import glob

test = angreal.command_group(name='test', about='Run test suite')

@test()
@angreal.command(name='unit', about='Run unit tests')
def run_unit_tests():
    """Run the unit test suite for the project."""
    root_dir = angreal.get_root()
    cmd = ['pytest', '-svvv', os.path.join(root_dir, "..", "tests", "unit")]
    
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=root_dir)
    return result.returncode == 0

@test()
@angreal.command(name='integration', about='Run integration tests')
def run_integration_tests():
    """Run the integration test suite for the project."""
    root_dir = angreal.get_root()
    cmd = ['pytest', '-svvv', os.path.join(root_dir, "..", "tests", "integration")]
    
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=root_dir)
    return result.returncode == 0

@test()
@angreal.command(name='functional', about='Run functional tests')
def run_functional_tests():
    """Run the functional test suite for the project."""
    root_dir = angreal.get_root()
    cmd = ['pytest', '-svvv', os.path.join(root_dir, "..", "tests", "functional")]
    
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=root_dir)
    return result.returncode == 0

@test()
@angreal.command(name='notebook', about='Run notebook execution tests')
@angreal.argument(name='epoch', long='epoch', short='e',
                 takes_value=True,
                 help='Specific epoch to test (e.g., "001")')
def run_notebook_tests(epoch=None):
    """Run notebook execution tests.
    
    This only tests that notebooks execute without errors and does not
    compare outputs (for security reasons).
    """
    root_dir = angreal.get_root()
    cmd = ['pytest', '--nbval-lax']  # Only check execution, not outputs
    
    # Determine which notebooks to test
    if epoch:
        notebook_path = f"notebooks/epoch_{epoch}"
        if not os.path.exists(os.path.join(root_dir, notebook_path)):
            print(f"Error: Epoch {epoch} not found.")
            return False
        cmd.append(notebook_path)
    else:
        cmd.append("notebooks")
    
    # Run the notebook tests
    print(f"\nRunning notebook tests: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=root_dir)
    
    if result.returncode != 0:
        print("\nSome notebooks failed execution.")
        print("This is expected for older notebooks that might use outdated APIs.")
        print("Consider updating them or marking them as legacy.")
        return False
    
    return True

@test()
@angreal.command(name='all', about='Run all test suites')
def run_all_tests():
    """Run all test suites for the project."""
    success = True
    
    # Run all test types
    if not run_unit_tests():
        success = False
    if not run_integration_tests():
        success = False
    if not run_functional_tests():
        success = False
    if not run_notebook_tests(epoch=None):        success = False
    
    return success
