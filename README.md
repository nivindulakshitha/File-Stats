# File Operations Utility

This utility provides functionalities to retrieve statistics of a file such as size, ownership, and timestamps.

### Usage:
1. Ensure `fileOps.py` is present in the same directory.
2. Import `fileStat` class from `fileOps` module.
3. Create an instance of `fileStat` by providing the file path.
4. Use `getFileStat()` method to retrieve file statistics.

### Example (app.py):
```python
from fileOps import fileStat

myfileStat = fileStat(filepath="sample.txt")
if (myfileStat.fileReady):
    print(myfileStat.getFileStat())
```

### Classes:
- `__file__`: Handles file operations and readiness state.
- `fileStat`: Inherits from `__file__` and provides file statistics retrieval.

### Methods:
- `getFilepath()`: Returns the file path.
- `setFilePath(new_filepath)`: Updates the file path.
- `getFileStat()`: Retrieves file statistics.

### Note:
Ensure proper file path and permissions for accurate results.
