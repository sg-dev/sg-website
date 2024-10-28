import os
import re
import argparse

def replace_projects_with_research(directory):
    # Loop through all files in the specified directory
    for subdir, _, files in os.walk(directory):
        for file in files:
            # Only process Markdown files
            if file.endswith(".md"):
                file_path = os.path.join(subdir, file)
                
                # Read the content of the file
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Check if we're in the front matter by looking for the '---' block
                if content.startswith('---'):
                    # Find the end of the front matter block
                    front_matter_end = content.find('---', 3)
                    if front_matter_end != -1:
                        # Extract the front matter and replace 'projects:' with 'research:'
                        front_matter = content[:front_matter_end]
                        updated_front_matter = re.sub(r"^projects:(?=\s)", "research:", front_matter, flags=re.MULTILINE)
                        
                        # Update the content if there was a change
                        if front_matter != updated_front_matter:
                            new_content = updated_front_matter + content[front_matter_end:]
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.write(new_content)
                            print(f"Updated: {file_path}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Replace 'projects:' with 'research:' in Hugo front matter.")
    parser.add_argument("directory", type=str, help="Path to the Hugo content directory")
    args = parser.parse_args()

    # Run the replacement function with the provided directory path
    replace_projects_with_research(args.directory)

if __name__ == "__main__":
    main()
