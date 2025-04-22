# Description
A toy CLI tool to store, retrieve, update, and delete code snippets with metadata like title, tags, and pin status.

# Before you proceed 
This project was created to play with prefix trees at the core level.

While it implements basic search engine functions, it would need features like data persistence, full-text search and relevance sorting to become a full application.

# Why use tries?
They enable O(len of keyword) prefix-based search of titles and tags. 

# Metadata details
Title: The name or description of the code snippet.

Tags: Labels that describe the content of the code snippet.

Pin status: A Boolean flag to indicate the priority status of a snippet.

(All metadata fields support retrieval via search)
