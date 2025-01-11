# Playwright - Useful Commands

## Checking Versions

### Check Python Version
```bash
py --version
```

### Check pip Version
```bash
py -m pip --version
```

## Installation

### Upgrade pip
```bash
py -m pip install --upgrade pip
```

### Install Playwright
```bash
py -m pip install playwright
```

### Install All Browsers
```bash
py -m playwright install
```

### Install pytest
```bash
py -m pip install pytest
```


## Recording Tests

### Start Playwright Codegen (Action Recorder)
```bash
py -m playwright codegen
```
This tool allows you to record actions in the browser and generate automation code.

## Running Scripts

### Run a Playwright Script
```bash
py script.py
```

### Run a Playwright Script in Headed Mode (with visible browser)
```bash
py script.py --headed
```

## Reports

### Generate HTML Report (After Running Tests)
```bash
npx playwright show-report
```

### Show Trace Viewer (For Debugging)
```bash
py -m playwright show-trace trace.zip
```
Use this command to analyze test results using the trace replay tool.

---

## Notes

- **Codegen**: You can provide a URL to record actions on a specific page, e.g.:
  ```bash
  py -m playwright codegen https://example.com
  ```
- **Running Scripts**: To run tests with a visible browser, use the `--headed` flag. By default, Playwright runs in headless mode (without UI).
- **Reports and Trace Viewer**: You can use the built-in reporting tool and trace viewer to help debug test failures.



