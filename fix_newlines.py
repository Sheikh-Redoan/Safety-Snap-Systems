import os
import glob

project_dir = r"c:\Users\ssrab\Desktop\Projects\Safety Snap Systems"
for root, _, files in os.walk(project_dir):
    for filename in files:
        if filename.endswith(".js") or filename.endswith(".jsx") or filename.endswith(".css"):
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            if content.endswith("\\n"):
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content[:-2] + "\n")
