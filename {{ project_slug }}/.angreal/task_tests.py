import angreal
from angreal.integrations.venv import VirtualEnv

import os
import subprocess
import webbrowser

cwd = os.path.join(angreal.get_root(),'..')
test = angreal.command_group(name="test", about="commands for testing the application and library")


@test()
@angreal.command(name="unit", about="run unit tests")
@angreal.argument(name="open", long="open", short='o', 
                  takes_value=False, help="open results in web browser")
def unit_tests(open=False):
    venv_path = os.path.join(cwd, '.venv')
    output_file = os.path.realpath(os.path.join(cwd,'htmlcov','index.html'))
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        subprocess.run('pytest -vvv --cov=src/{{ package_name }} '
                       '--cov-report html --cov-report term tests/unit',shell=True, cwd=cwd)    
        if open:
            webbrowser.open_new('file://{}'.format(output_file))


@test()
@angreal.command(name="integration", about="run integration tests")
@angreal.argument(name="open", long="open", short='o', 
                  takes_value=False, help="open results in web browser")
def integration_tests(open=False):
    venv_path = os.path.join(cwd, '.venv')
    output_file = os.path.realpath(os.path.join(cwd,'htmlcov','index.html'))
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        subprocess.run('pytest -vvv --cov=src/{{ package_name }} --cov-report html'
                       ' --cov-report term tests/integration',shell=True, cwd=cwd)
        if open:
            webbrowser.open_new('file://{}'.format(output_file))

@test()
@angreal.command(name="notebook", about="run notebook execution tests")
@angreal.argument(name="epoch", long="epoch", short='e',
                 takes_value=True,
                 help='Specific epoch to test (e.g., "001")')
def run_notebook_tests(epoch=None):
    """Run notebook execution tests.
    
    This only tests that notebooks execute without errors and does not
    compare outputs (for security reasons).
    """
    venv_path = os.path.join(cwd, '.venv')
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        cmd = ['pytest', '--nbval-lax']  # Only check execution, not outputs
        
        # Determine which notebooks to test
        if epoch:
            notebook_path = f"notebooks/epoch_{epoch}"
            if not os.path.exists(os.path.join(cwd, notebook_path)):
                print(f"Error: Epoch {epoch} not found.")
                return False
            cmd.append(notebook_path)
        else:
            cmd.append("notebooks")
        
        # Run the notebook tests
        print(f"\nRunning notebook tests: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=cwd)
        
        if result.returncode != 0:
            print("\nSome notebooks failed execution.")
            print("This is expected for older notebooks that might use outdated APIs.")
            print("Consider updating them or marking them as legacy.")
            return False
        
        return True

@test()
@angreal.command(name="all", about="run all tests (unit, integration, and notebooks)")
@angreal.argument(name="open", long="open", short='o', 
                  takes_value=False, help="open results in web browser")
def all_tests(open=False):
    """Run all test suites for the project."""
    venv_path = os.path.join(cwd, '.venv')
    output_file = os.path.realpath(os.path.join(cwd,'htmlcov','index.html'))
    success = True
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        # Run unit and integration tests with coverage
        result = subprocess.run('pytest -vvv --cov=src/{{ package_name }} '
                               '--cov-report html --cov-report term tests/',shell=True, cwd=cwd)
        if result.returncode != 0:
            success = False
        
        # Run notebook tests
        if not run_notebook_tests(epoch=None):
            success = False
            
        if open:
            webbrowser.open_new('file://{}'.format(output_file))
    
    return success

@test()
@angreal.command(name='static', about="run our static analysis")
@angreal.argument(name="open", long="open", short='o',
                   takes_value=False, help="open results in web browser")
def setup_env(open):
    venv_path = os.path.join(cwd, '.venv')
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        subprocess.run(
            (
                "mypy src/{{package_name}} --ignore-missing-imports --html-report typing_report"
            ),
            shell=True,
            cwd=cwd
        )

        if open:
            webbrowser.open(f'file:://{os.path.join(cwd,"typing_report","index.html")}')
