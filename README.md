# QuantumCompiler

## How to use pre-commit hooks

1. In your virtual environment run
    - `pip install -r requirements-dev.txt`

2. Make sure pre-commit has been installed correctly
    - `pre-commit --version` → e.g. `pre-commit 2.10.1`

3. Install pre-commit hooks
   - `pre-commit install`

4. Done, pre-commit hooks will be run before each commit

### Tips

   - If you want to make a commit without running checks, use `--no-verify` flag
   - If you want to run checks without creating a commit, run `pre-commit run --all-files`
