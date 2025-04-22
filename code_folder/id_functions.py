from trie_functions import prefix_match_node

# returns all ID matches for a given prefix
def search_prefix_id(current_node) :
    id_matches = set()

    # in case there are no matching prefixes 
    if current_node is None :
        return None

    # needed for words that are prefixes of other valid words
    if current_node.is_word_end :
        id_matches.update(current_node.id_set)

    for char in current_node.child_chars :
        # adding in each step to make sure all are accounted for
        id_matches.update(search_prefix_id(current_node.child_chars[char]))
    
    return id_matches

# returns set of matching IDs for a single word
def get_specific_id(root, field, prefix) :
    return search_prefix_id(prefix_match_node(prefix, root))

# finds IDs of titles, given some combination of prefixes 
def get_common_id(root, field, in_prefix_list) :
    final_id_matches = None
    for in_prefix in in_prefix_list :
        if final_id_matches is None : final_id_matches = get_specific_id(root, field, in_prefix)
        else : final_id_matches &= get_specific_id(root, field, in_prefix)

    return final_id_matches
