---
title: "VP-AGENT Contribution Guide"
date: "2023-08-18"
tags: ["contribution", "guide", "workflow", "metadata"]
category: "tutorials/contribution"
summary: "Complete guide for adding new content to the VP-AGENT repository"
language: "en"
related_files: ["templates/system_prompt_template.md", "templates/tutorial_template.md"]
---

# VP-AGENT Contribution Guide

This guide explains how to add new content to the VP-AGENT repository, including file organization, metadata requirements, and best practices.

## File Organization

The VP-AGENT repository is organized into the following main directories:

- `/prompts/main/`: Primary system prompts that define VP AGENT's behavior
- `/prompts/utilities/`: Helper prompts for specific tasks like tag extraction
- `/tutorials/`: Documentation and guides for using and contributing to the system
- `/templates/`: Example templates for creating new content
- `/main/`: Core configuration files including the structure JSON

## Adding New Content

### Step 1: Choose the Right Location

Select the appropriate directory based on your content type:
- System prompts go in `/prompts/main/`
- Utility prompts go in `/prompts/utilities/`
- Guides and documentation go in `/tutorials/`
- Example templates go in `/templates/`

### Step 2: Create the Markdown File

Create a new markdown file with a descriptive name using underscores for spaces:
- `system_prompt_name.md`
- `utility_prompt_name.md`
- `guide_topic_name.md`

### Step 3: Add Required Metadata

Every file must include YAML frontmatter at the top with the following fields:

```yaml
---
title: "Descriptive Title"
date: "YYYY-MM-DD"
tags: ["relevant-tag", "another-tag"]
category: "main-category/sub-category"
summary: "Brief description of the file contents"
language: "en" (or "fa" for Persian, etc.)
related_files: ["path/to/related1.md", "path/to/related2.md"]
---
Step 4: Write Your Content
Write your content using proper markdown formatting:

Use headings for organization (# for main title, ## for sections)
Use code blocks for examples
Use bullet points and numbered lists for clarity
Include examples where helpful
Step 5: Commit Your Changes
Commit your file to the repository. The GitHub Action will automatically:

Detect your new file
Extract metadata
Update the vp_agent_structure.json file
Step 6: Verify the Update
Check that your file appears correctly in:

The vp_agent_structure.json file
The category listings
The tag collections
Metadata Best Practices
Effective Tags
Choose tags that:

Describe the content type (system-prompt, tutorial, template)
Indicate the subject matter (documentation, contribution, workflow)
Highlight key concepts (metadata, JSON, GitHub)
Include relevant technologies (markdown, YAML, Python)
Useful Summaries
Write summaries that:

Clearly state the purpose of the file
Include key functionality or topics covered
Are concise (ideally 10-15 words)
Help users decide if the content is relevant to their needs
Examples
See the /templates/ directory for complete examples of different content types.

yaml

## گام 4: ایجاد فایل قالب برای سیستم پرامپت

1. یک پوشه به نام `templates` ایجاد کنید (اگر وجود ندارد).

2. یک فایل جدید به نام `system_prompt_template.md` در پوشه `templates/` ایجاد کنید.

3. محتوای زیر را در این فایل قرار دهید:

```markdown
---
title: "System Prompt Template"
date: "2023-08-18"
tags: ["template", "system-prompt", "example"]
category: "templates"
summary: "Standard template for creating new system prompts"
language: "en"
related_files: ["prompts/main/psm_vp_agent.md", "tutorials/contribution_guide.md"]
---

# System Prompt Template

Use this template when creating new system prompts for VP AGENT.

## Basic Structure

=================== PSM [NAME]
ROLE AND PURPOSE
[Define the specific role and purpose of this system prompt]

INSTRUCTIONS
[Main instructions for the AI model]

RESPONSE FORMAT
[How responses should be structured]

EXAMPLES
[Example interactions showing expected behavior]

=================== END OF PSM [NAME]
markdown

## Required Sections

Every system prompt should include these sections:

1. **ROLE AND PURPOSE**: Define what specific role the AI should adopt and what its main purpose is.

2. **INSTRUCTIONS**: The main body of instructions that guide the AI's behavior.

3. **RESPONSE FORMAT**: How the AI should structure its responses (e.g., sections, citations, style).

4. **EXAMPLES**: Sample interactions showing how the AI should respond in specific situations.

## Optional Sections

Depending on the complexity of the system prompt, you may also include:

- **KNOWLEDGE BASE**: Specific information the AI should know about
- **REASONING METHODOLOGY**: How the AI should approach problem-solving
- **ERROR HANDLING**: How to deal with mistakes or limitations
- **ETHICAL GUIDELINES**: Specific ethical considerations for this prompt

## Best Practices

- Use clear, concise language
- Break complex instructions into numbered steps
- Use ALL CAPS for section headings for visibility
- Include specific examples for ambiguous instructions
- Test your prompt with different types of queries before finalizing
