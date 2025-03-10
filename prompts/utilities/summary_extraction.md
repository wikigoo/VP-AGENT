---
title: "Summary Extraction"
category: "2.1"
tags: ["utility", "summary", "extraction", "AI", "content"]
summary: "Prompt for automatically extracting summaries from long and complex texts."
last_updated: "2023-08-16"
language: "en"
related_files: ["prompts/utilities/tag_extraction.md"]
---

# Summary Extraction Utility

## Purpose
This prompt is designed to extract concise and informative summaries from longer texts while preserving key information.

## Instructions

1. Analyze the input text for:
   - Main topics and themes
   - Key arguments or points
   - Important conclusions
   - Critical data or statistics

2. Create a summary that:
   - Is approximately 10-15% of the original text length
   - Maintains the original tone and perspective
   - Preserves the most important information
   - Follows a logical flow

3. Format the summary with:
   - An introductory sentence establishing the context
   - Body paragraphs covering main points
   - A concluding sentence capturing the significance

4. For technical content:
   - Preserve specialized terminology
   - Maintain numerical data accuracy
   - Keep citations when critical

## Example Input/Output

### Input:
[Long text about climate change impacts]

### Output:
"This report examines climate change impacts across five continents, highlighting temperature increases of 1.5°C over pre-industrial levels. Key findings include accelerated polar ice melt (15% increase since 2000), rising sea levels (projected 0.5-1.2m by 2100), and ecosystem disruption affecting 30% of species. Mitigation strategies focus on renewable energy transition and carbon capture technologies, while adaptation measures emphasize infrastructure resilience and agricultural innovation. The authors conclude that immediate action could limit warming to 2°C, preventing the most catastrophic outcomes."

## Special Cases

- For multi-section documents: Provide brief summaries of each section followed by an overall summary
- For narrative texts: Focus on plot points, character development, and themes rather than details
- For technical papers: Emphasize methodology, findings, and implications over background information
