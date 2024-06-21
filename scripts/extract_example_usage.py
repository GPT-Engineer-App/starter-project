import os
import re


def extract_usage_section(file_content):
    """
    Extract the "Usage" section from the given file content.
    """
    usage_section = ""
    in_usage_section = False
    for line in file_content.splitlines():
        if line.startswith("## Usage"):
            in_usage_section = True
        elif line.startswith("## ") and in_usage_section:
            # Exit when another section starts
            break
        if in_usage_section and not line.startswith("## Usage"):
            usage_section += line + "\n"
    return usage_section


def process_files(directory):
    """
    Process all Markdown files in the given directory to extract the "Usage" section.
    """
    all_usages = ""
    for filename in os.listdir(directory):
        if filename.endswith(".mdx"):
            with open(os.path.join(directory, filename), "r") as file:
                component_name = filename.replace(".mdx", "")
                content = file.read()
                usage_section = extract_usage_section(content)
                if usage_section:
                    # Extract the title for naming the section in the consolidated file
                    title_match = re.search(r"^title:\s*(.*)", content, re.MULTILINE)
                    if title_match:
                        # title = title_match.group(1).strip()
                        all_usages += f"# Example Usage for {component_name}\n\n"
                        all_usages += usage_section
                        all_usages += "\n\n"

    # Write all usages to a single file next to the script
    with open("all_usages.md", "w") as output_file:
        output_file.write(all_usages)


if __name__ == "__main__":
    ui_path = "/Users/fabian/git/ui"
    components_dir = "apps/www/content/docs/components"
    directory = os.path.join(ui_path, components_dir)
    print(f"Processing files in {directory}")
    process_files(directory)
