# Create temp file. Invoke editor passing temp file. 
# When user quits, check if editor has successfully exited, read temp file. Prefill temp file with whatever I want 
# Application blocks and waits for editor to be done.
# Check if editor variable is empty. Set it.

import subprocess
import os
import tempfile


editor = os.environ['EDITOR']

tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"# this comment works")
tmp.close()
subprocess.run(editor.split() + [tmp.name], shell=True) 
print(tmp.name)

# subprocess.run(["C:\\Users\\hmsh2\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code.cmd", "--wait"])
