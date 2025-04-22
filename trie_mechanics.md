# How are the titles and tags stored?
Each title and list of tags is tokenized into individual words, and stored in two tries (one each for titles and tags).

Since the inherent structure is the same, we can look at the general logic behind the addition, deletion, and updation of a token. 

Each character in the token is associated with a node in the prefix tree. For this, we define a Node class with certain attributes.

Every instance of the Node class contains:  
i) A dictionary (child_chars) with the node's child characters as keys and references to the corresponding node objects as values.

ii) A Boolean flag (is_word_end) to indicate if the node is the end of a token (otherwise, it is considered a prefix).

iii) A set of all IDs (id_set) associated with the tokens whose last node is the current node.

iv) A Boolean flag (is_deleted) to indicate whether the node is marked as deleted (soft deletion).

# Addition of a token
When adding a new token, the program either creates a new branch, or continues along an existing one (for common prefixes). 

Whenever we encounter a character that doesn't exist in the child_chars dict, a new node is created (for that character) and added to the dict.

This continues until we reach the end of the token. Here, we set the is_word_end boolean to True, and add the ID associated with the token to the id_set.

# Deletion of a token
We need the root node (title_root / tag_root), the token we want to delete, and the id_num.

We start at the root node and traverse till the end of the token. During this traversal, a reference to each node is added to a list. 

Once the end character is reached, we go back up the tree (by going through the list in reverse), only marking the nodes as deleted if the following conditions are satisfied:  
i) Its child nodes are all deleted, or the child_chars dict is empty.

ii) The id_set associated with the word is empty (meaning no other snippet uses this token). 

Once these conditions are satisfied, we set the is_deleted flag to True.

# Updation of title/tags
Essentially involves deletion of the old tokens followed by addition of the new ones.

# Query: Why implement soft deletion?
It helps highlight the working behind the deletion process and how it reacts to different scenarios. The deletion_status_nodes function helps see this selective deletion of nodes in action, especially in cases of shared prefixes, common tokens across multiple titles/tags, and so on.
