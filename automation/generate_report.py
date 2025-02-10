import os
import git
import jinja2
import pypandoc

# Get latest commit details
repo = git.Repo(search_parent_directories=True)
commit = repo.head.commit
commit_data = {
    "commit_id": commit.hexsha,
    "author": commit.author.name,
    "date": commit.committed_datetime.strftime("%Y-%m-%d %H:%M:%S"),
}

# Load the markdown template
with open("docs/report_template.md", "r") as file:
    template = jinja2.Template(file.read())

# Render markdown
rendered_markdown = template.render(commit_data)

# Save to markdown file
md_path = "docs/commit_report.md"
pdf_path = "docs/commit_report.pdf"
with open(md_path, "w") as file:
    file.write(rendered_markdown)

# Convert to PDF
pypandoc.convert_file(md_path, "pdf", outputfile=pdf_path)

print(f"Generated report: {pdf_path}")