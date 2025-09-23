import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import setup

file_types = setup.file_types  # Use your dictionary directly

class SetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Setup Configuration")
        
        
        
        self.source_dir = {}
        self.paths = {}
        self.extension_vars = {}

        for key in file_types:
            category = key.replace("_extensions", "")
            self.paths[category] = tk.StringVar()
            self.extension_vars[category] = {
                ext: tk.BooleanVar(value=True) for ext in file_types[key]
            }

        # Load source_dir from setup.py
        self.source_dir = tk.StringVar()
        if hasattr(setup, "source_dir"):
            self.source_dir.set(setup.source_dir)

        # Load existing settings from setup2.py
        for category in self.paths:
            path_var = f"{category}_dir"
            ext_var = f"{category}_extensions"

            if hasattr(setup, path_var):
                self.paths[category].set(getattr(setup, path_var))

            if hasattr(setup, ext_var):
                selected_exts = getattr(setup, ext_var)
                for ext in self.extension_vars[category]:
                    self.extension_vars[category][ext].set(ext in selected_exts)

        # GUI layout
        tk.Label(root, text="Source folder:").pack(pady=(10, 0))
        tk.Entry(root, textvariable=self.source_dir, width=60).pack()
        tk.Button(root, text="Browse Source folder", command=self.browse_source_folder).pack(pady=2)
        for category in self.paths:
            tk.Label(root, text=f"{category.capitalize()} Folder:").pack(pady=(10, 0))
            tk.Entry(root, textvariable=self.paths[category], width=60).pack()
            tk.Button(root, text=f"Browse {category}", command=lambda c=category: self.browse_folder(c)).pack(pady=2)

            tk.Label(root, text=f"{category.capitalize()} Extensions:").pack()
            ext_frame = tk.Frame(root)
            ext_frame.pack()
            for ext in self.extension_vars[category]:
                tk.Checkbutton(ext_frame, text=ext, variable=self.extension_vars[category][ext]).pack(side="left")

        tk.Button(root, text="Save Settings", command=self.save_settings, bg="lightgreen").pack(pady=30)

    def browse_source_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.source_dir.set(folder)

    def browse_folder(self, category):
        folder = filedialog.askdirectory()
        if folder:
            self.paths[category].set(folder)

    def save_settings(self):
        setup_path = Path(__file__).parent / "setup.py"

        try:
            with open(setup_path, "w", encoding="utf-8") as f:
                # Write file_types dictionary
                f.write("file_types = {\n")
                for key, exts in file_types.items():
                    ext_list = ", ".join(f'"{ext}"' for ext in exts)
                    f.write(f'    "{key}": [{ext_list}],\n')
                f.write("}\n\n")

                source_path = self.source_dir.get().replace("\\", "\\\\")
                f.write(f'source_dir = "{source_path}"\n')

                # Write folder paths
                for category in self.paths:
                    folder_path = self.paths[category].get().replace("\\", "\\\\")
                    f.write(f'{category}_dir = "{folder_path}"\n')

                f.write("\n")

                # Write selected extensions
                for category in self.extension_vars:
                    selected_exts = [f'"{ext}"' for ext, var in self.extension_vars[category].items() if var.get()]
                    f.write(f"{category}_extensions = [{', '.join(selected_exts)}]\n")

            messagebox.showinfo("Saved", f"Settings saved to:\n{setup_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings:\n{e}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SetupApp(root)
    root.mainloop()


