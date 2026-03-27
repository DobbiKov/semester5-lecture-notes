import subprocess
import os
import glob

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_command(cmd, description, quiet=False):
    """Run a command and print its status."""
    print(f"\n{'='*60}")
    print(f"  {description}")
    print(f"{'='*60}")
    if quiet:
        result = subprocess.run(cmd, cwd=PROJECT_DIR, shell=isinstance(cmd, str),
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        result = subprocess.run(cmd, cwd=PROJECT_DIR, shell=isinstance(cmd, str))
    if result.returncode != 0:
        print(f"Warning: Command exited with code {result.returncode}")
    return result.returncode


def generate_images():
    """Run generate_images.py to create all figures."""
    print("\n[Step 1] Generating images...")
    return run_command(
        ["python3", os.path.join(PROJECT_DIR, "generate_images.py")],
        "Running generate_images.py"
    )


def compile_latex():
    """Run pdflatex 3 times for proper cross-references."""
    print("\n[Step 2] Compiling LaTeX (3 passes)...")
    main_tex = os.path.join(PROJECT_DIR, "main.tex")
    
    for i in range(1, 4):
        ret = run_command(
            ["pdflatex", "-interaction=nonstopmode", main_tex],
            f"pdflatex pass {i}/3",
            quiet=(i > 1)  # Suppress output for passes 2 and 3
        )
        # if ret != 0 and i == 1:
        #     print("Error: First pdflatex pass failed. Check for LaTeX errors.")
        #     return ret
    
    return 0


def cleanup():
    """Remove image files."""
    print("\n[Step 3] Cleaning up...")
    
    # Remove image files (all .png files in the project directory)
    print("  Removing image files...")
    for img_path in glob.glob(os.path.join(PROJECT_DIR, "*.png")):
        os.remove(img_path)
        print(f"    Deleted: {os.path.basename(img_path)}")
    
    print("\n[Done] Compilation complete!")
    print(f"  Output: {os.path.join(PROJECT_DIR, 'main.pdf')}")


def main():
    """Main entry point."""
    print("=" * 60)
    print("  MDD303 Probabilités - Compile Script")
    print("=" * 60)
    
    # Step 1: Generate images
    ret = generate_images()
    if ret != 0:
        print("Error generating images. Aborting.")
        return 1
    
    # Step 2: Compile LaTeX (3 passes)
    ret = compile_latex()
    if ret != 0:
        print("Warning: LaTeX compilation had errors.")
    
    # Step 3: Cleanup
    cleanup()
    
    return 0


if __name__ == "__main__":
    exit(main())
