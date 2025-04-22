# Node class for the prefix tree nodes
class Node() :
    def __init__(self) :
        self.child_chars = {}  
        self.is_word_end = False  
        self.id_set = set()
        self.is_deleted = False

# function to add a single word to a trie
def add_to_trie(root, word, id_num) :
    # working on a root under construction
    current_node = root  
    for char in word :
        if char not in current_node.child_chars :
            current_node.child_chars[char] = Node()
        current_node = current_node.child_chars[char]

        # adding this for updation logci
        current_node.is_deleted = False
        
    # after one whole word is processed
    current_node.is_word_end = True
    current_node.id_set.add(id_num)

    return root

# function to delete a word (not unique) on the basis of ID (unique)
# soft deletion, since id_num is removed and the letters remain (marked deleted)
def delete_from_trie(root, word, id_num) :  
    current_node = root
    seen_nodes = []

    for char in word :
        # in case the word doesnt exist
        if char not in current_node.child_chars :
            # returning the unmodified root (only modifiying after reaching last character)
            return root
            
        current_node = current_node.child_chars[char]
        # appending with char in case its needed at some point   
        seen_nodes.append((current_node, char))   

    # this removal of the ID happens regardless of the status of this nodes child_chars/id_set
    current_node.id_set.discard(id_num)

    # function to check if all child nodes are deleted
    def is_all_deleted(parent_node) :
        # empty dict is falsy
        if not parent_node.child_chars : 
            return True 

        for node in parent_node.child_chars.values() :
            if node.is_deleted is False : 
                return False
        return True
    
    # if the current node has children or is the final node for any other word, it shouldnt be marked deleted/word_end 
    reversed_seen_nodes = list(reversed(seen_nodes))
    for node, char in reversed_seen_nodes :
        # the parent node can be deleted only if all of its child nodes are as well
        # proper deletion occurs when longer words are deleted before the shorter ones
        if is_all_deleted(node) and not node.id_set: 
            node.is_deleted = True
        else :
            return root
    
    return root

def deletion_status_nodes(root, word) :
    current_node = root
    status_dict = {}
    for char in word :
        if char not in current_node.child_chars :
            return None
            
        if char not in status_dict :
            status_dict[char] = []
        current_node = current_node.child_chars[char]
        status_dict[char].append(current_node.is_deleted)

    return status_dict

# function to create a full prefix tree with a given node and for a given field (either title or tags)
def create_prefix_tree(specific_root, field, snippets) :
    for id_key in snippets :
        for word in snippets[id_key][field] :
            specific_root = add_to_trie(specific_root, word, id_key)  
    
    return specific_root

# returns end node of a given prefix
def prefix_match_node(prefix, root_node) :
    current_node = root_node
    for char in prefix :
        if char not in current_node.child_chars :
            return None 
        current_node = current_node.child_chars[char]

    return current_node 
