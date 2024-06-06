# Create temp file. Invoke editor passing temp file. 
# When user quits, check if editor has successfully exited, read temp file. Prefill temp file with whatever I want 
# Application blocks and waits for editor to be done.
# Check if editor variable is empty. Set it.

import subprocess
import os
import tempfile

# Run Visual Studio Code and wait for it to close
subprocess.run(["C:\\Users\\hmsh2\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code.cmd", "--wait"])

# Check if the 'EDITOR' environment variable is set
editor = os.environ['EDITOR']

# Create temp file that doesn't delete itself after closing
tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"# this comment works")
tmp.close()

# Run the editor (specified in the 'EDITOR' environment variable) to open the temporary file
subprocess.run(editor.split() + [tmp.name], shell=True) 
# Print the name of the temporary file
print(tmp.name)

