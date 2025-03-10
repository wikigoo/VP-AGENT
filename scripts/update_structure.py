#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import yaml
import re
from datetime import datetime

def extract_frontmatter(content):
    """Extract YAML metadata from markdown content"""
    pattern = r'^---\s+(.*?)\s+---\s+'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            return {}
    return {}

def scan_markdown_files():
    """Scan all markdown files and extract metadata"""
    files_data = []
    tags_count = {}
    
    for root, dirs, files in os.walk('.'):
        # Skip system and hidden directories
        if '.git' in root or 'node_modules' in root or '.github' in root:
            continue
            
        for file in files:
            if file.endswith('.md') and file != 'README.md' and file != 'index.md':
                file_path = os.path.join(root, file)
                rel_path = file_path[2:] if file_path.startswith('./') else file_path
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    metadata = extract_frontmatter(content)
                    
                    if metadata and 'title' in metadata and 'category' in metadata:
                        file_data = {
                            'path': rel_path,
                            'category': metadata.get('category', ''),
                            'title': metadata.get('title', ''),
                            'tags': metadata.get('tags', []),
                            'summary': metadata.get('summary', ''),
                            'last_updated': metadata.get('last_updated', datetime.now().strftime('%Y-%m-%d')),
                            'language': metadata.get('language', 'en'),
                            'related_files': metadata.get('related_files', [])
                        }
                        
                        files_data.append(file_data)
                        
                        # Count tags
                        for tag in file_data['tags']:
                            if tag in tags_count:
                                tags_count[tag] += 1
                            else:
                                tags_count[tag] = 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    # Create tag data
    tags_data = []
    for tag, count in tags_count.items():
        related_tags = []
        for file_data in files_data:
            if tag in file_data['tags']:
                related_tags.extend([t for t in file_data['tags'] if t != tag])
        
        # Remove duplicate tags and limit to 5 related tags
        related_tags = list(set(related_tags))[:5]
        
        tags_data.append({
            'name': tag,
            'count': count,
            'related_tags': related_tags
        })
    
    return files_data, tags_data

def update_structure_json():
    """Update the vp_agent_structure.json file"""
    structure_file = 'main/vp_agent_structure.json'
    
    try:
        # Read existing JSON file
        with open(structure_file, 'r', encoding='utf-8') as f:
            structure_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        # Create basic structure if file doesn't exist
        structure_data = {'files': [], 'categories': [], 'tags': []}
    
    # Scan markdown files and extract data
    files_data, tags_data = scan_markdown_files()
    
    # Preserve existing categories
    categories = structure_data.get('categories', [])
    
    # Update files and tags
    structure_data['files'] = files_data
    structure_data['tags'] = tags_data
    
    # Ensure categories are preserved
    if categories:
        structure_data['categories'] = categories
    
    # Write updated data to file
    try:
        with open(structure_file, 'w', encoding='utf-8') as f:
            json.dump(structure_data, f, indent=2, ensure_ascii=False)
        
        print(f"Updated {structure_file} with {len(files_data)} files and {len(tags_data)} tags")
    except Exception as e:
        print(f"Error writing JSON file: {e}")

if __name__ == '__main__':
    update_structure_json()
