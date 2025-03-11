---
title: "Getting Started with VP-AGENT"
date: "2023-08-18"
tags: ["guide", "introduction", "overview"]
category: "tutorials/getting_started"
summary: "Introduction to the VP-AGENT repository and how to use it"
language: "en"
related_files: ["tutorials/contribution_guide.md"]
---

# Getting Started with VP-AGENT

This guide introduces the VP-AGENT repository, its purpose, and how to use it effectively.

## What is VP-AGENT?

VP-AGENT is a repository designed to organize and manage:

1. System prompts for AI assistants
2. Documentation and tutorials
3. Templates and examples

The repository uses a structured approach to make information easily accessible to both humans and AI assistants.

## Repository Organization

The VP-AGENT repository is organized into these main directories:

- `/prompts/main/`: Contains primary system prompts that define the behavior of AI assistants
- `/prompts/utilities/`: Contains helper prompts for specific tasks like tag extraction
- `/tutorials/`: Contains guides and documentation about the system
- `/templates/`: Contains example templates for creating new content
- `/main/`: Contains core configuration files including the structure JSON

## Key Components

### 1. System Prompts

System prompts are instructions for AI models that define:
- How to respond to questions
- How to format responses
- How to access and prioritize information
- How to handle different types of queries

### 2. Documentation

Documentation files provide detailed information about:
- How the system works
- How to contribute new content
- Best practices for using the system
- Technical details and specifications

### 3. JSON Structure

The `vp_agent_structure.json` file serves as the central index for the repository:
- Maps categories to specific files
- Maintains a tag system for content discovery
- Stores summaries of each file for quick reference
- Tracks relationships between related files

## How to Use This Repository

### For End Users

1. Browse the `/tutorials/` directory for guides and documentation
2. Look at the `/templates/` directory for examples
3. Use the system prompts with compatible AI assistants

### For Contributors

1. Read the [Contribution Guide](contribution_guide.md)
2. Use the templates in the `/templates/` directory
3. Follow the metadata and organization standards

## Next Steps

- Read the [Contribution Guide](contribution_guide.md) to learn how to add new content
- Explore the system prompts to understand how they work
- Check out the templates for examples of different content types
