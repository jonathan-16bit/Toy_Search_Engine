from trie_functions import add_to_trie, delete_from_trie

# getting code from a file
def get_file_code(filename) :
    with open(filename, 'r') as file :
        return file.read()

# function to add snippets 
# added input validation
def add_snippet(snippets, title_root, tag_root) :

    # unique ID number for each snippet
    while True :
        id_key = input("Enter unique id: ")
        if id_key != "" :
            if id_key not in snippets : 
                snippets[id_key] = {}
                break
    snippets[id_key]["id"] = id_key

    # title of the snippet
    while True :
        title = " ".join(input("Enter title: ").split())
        if title != "" :
            snippets[id_key]["title"] = title
            break

    # tags to mark concepts used
    while True :
        tags = [tag.lower() for tag in input("Enter tags (in case of multi-word tags, separate by underscores): ").split()]
        if tags != [] :
            snippets[id_key]["tags"] = tags
            break

    # to pin/star the snippet
    while True :
        pin = input("Enter 1 to pin this data, 0 otherwise: ")
        if pin != "" and (pin == '0' or pin == '1'):
            snippets[id_key]["pin"] = bool(int(pin))
            break

    # code from code file
    # for simplicity im assuming its a python file (and that it exists)
    while True :
        code_file = input("Enter name of file in which code is present: ")
        if code_file[-3:] == ".py" :
            snippets[id_key]["code"] = get_file_code(code_file)
            break

    # so far only the dictionary has been updated
    # the following is needed to update the tries after every insertion
    for word in snippets[id_key]["title"].split() :
        title_root = add_to_trie(title_root, word, id_key)

    for word in snippets[id_key]["tags"] :
        tag_root = add_to_trie(tag_root, word, id_key)

    # technically the dictionary and the roots will be modified in place anyways
    return (snippets, title_root, tag_root)  

# function to delete snippets from the snippets dict 
def delete_snippet(id_num, snippets, title_root, tag_root) :
    if id_num not in snippets : 
        return None

    # deleting words of title from the prefix tree
    title_words_to_delete = sorted(snippets[id_num]["title"].split(), key = len, reverse = True)
    for word in title_words_to_delete :
        title_root = delete_from_trie(title_root, word, id_num)
    
    # deleting tags from the prefix tree
    tags_to_delete = sorted(snippets[id_num]["tags"], key = len, reverse = True)
    for word in tags_to_delete :
        tag_root = delete_from_trie(tag_root, word, id_num)

    # dictionary data deletion for that id_num
    del snippets[id_num]

    return (snippets, title_root, tag_root)

# updation logic
# input : id number (which cant be modified)
# should be able to update the title, tags, pin status and final code
def update_snippet(id_key, snippets, title_root, tag_root) :
    update_choice = '_'
    while update_choice != 'EXIT' :
        update_choice = input("Enter:\n1 to update title\n2 to update tags\n3 to change pin status\n4 to change code content\nEXIT to exit: ")

        # all these are for overwriting the snippets dictionary and modifying the tries
        if update_choice == '1' :
            while True :
                title = " ".join(input("Enter title: ").split())
                if title != "" :
                    
                    # deleting old title tokens
                    for word in snippets[id_key]["title"].split() :
                        title_root = delete_from_trie(title_root, word, id_key)

                    snippets[id_key]["title"] = title 

                    # adding new title tokens
                    for word in snippets[id_key]["title"].split() :
                        title_root = add_to_trie(title_root, word, id_key)

                    break

        # same logic as above
        elif update_choice == '2' :    
            while True :
                tags = [tag.lower() for tag in input("Enter tags (in case of multi-word tags, separate by underscores): ").split()]
                if tags != [] :
                    for word in snippets[id_key]["tags"] :
                        tag_root = delete_from_trie(tag_root, word, id_key)

                    snippets[id_key]["tags"] = tags 

                    for word in snippets[id_key]["tags"] : 
                        tag_root = add_to_trie(tag_root, word, id_key)

                    break

        elif update_choice == '3' :
            while True :
                pin = input("Enter 1 to pin this data, 0 otherwise: ")
                if pin != "" and (pin == '0' or pin == '1'):
                    snippets[id_key]["pin"] = bool(int(pin))
                    break

        elif update_choice == '4' :
            filename = input("Enter name of file in which code is present: ")
            snippets[id_key]["code"] = get_file_code(filename)
    
    return (snippets, title_root, tag_root)
