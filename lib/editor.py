# Create temp file. Invoke editor passing temp file. 
# When user quits, check if editor has successfully exited, read temp file. Prefill temp file with whatever I want 
# Application blocks and waits for editor to be done.
# Check if editor variable is empty. Set it.

import subprocess
import os
import tempfile

# Get default editor from the environment variable 'EDITOR'.
# If 'EDITOR' not set raise KeyError.
editor = os.environ['EDITOR']

# Create temp file. 'delete=False' parameter ensures file is not deleted when closed.
tmp = tempfile.NamedTemporaryFile(delete=False)

# Write comment to temp file. 'b' before string denotes a bytes literal, which is necessary for writing binary data.
tmp.write(b"# this comment works")
tmp.close()         # Close temp file to ensure all data is written and file is ready to be opened by editor.

# Run editor with temp file as argument. This line blocks execution of script until editor is closed.
subprocess.run(editor.split() + [tmp.name], shell=True) 

# Print name of temp file to console. Lets you see where temp file is located on file system.
print(tmp.name)

# subprocess.run(["C:\\Users\\hmsh2\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code.cmd", "--wait"])
