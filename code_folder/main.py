from snippet_functions import add_snippet, delete_snippet, update_snippet
from trie_functions import Node, add_to_trie, delete_from_trie, deletion_status_nodes, create_prefix_tree, prefix_match_node
from id_functions import search_prefix_id, get_specific_id, get_common_id

# ultimate dictionary to store snippets
snippets = {}

# initialize title trie
title_root = create_prefix_tree(Node(), "title", snippets)

# initialize tag trie
tag_root = create_prefix_tree(Node(), "tag", snippets)

# user input menu
choice = '0'
while choice != 'EXIT' :
    choice = input("\nEnter:\n1 to add snippet\n2 to search for a snippet (using title)\n3 to search for a snippet (using tag)\n4 to update snippet\n5 to delete snippet\n6 to view the snippets with metadata\n7 to check deletion status of a prefix\n8 to display pinned snippets\nEXIT to exit\nYour choice: ")

    if choice == '1' :
        add_confirm = '_'
        while add_confirm != 'EXIT' :
            add_confirm = input("To continue, press 1 again. Else, enter 'EXIT': ")

            if add_confirm != '1' and add_confirm != 'EXIT' :
                print("Please enter valid choice")

            elif add_confirm == 'EXIT' :
                break
            
            else :
                snippets, title_root, tag_root = add_snippet(snippets, title_root, tag_root)
    
    elif choice == '2' :
        search_choice = 0
        while search_choice != 'EXIT':
            search_choice = input("\nEnter 1 to search for a prefix, 'EXIT' to exit: ")
            
            if search_choice != '1' and search_choice != 'EXIT' :
                print("Please enter valid choice") 

            elif search_choice == 'EXIT' :
                break

            else :
                in_prefix_list = input("Enter your prefix: ").split() 
                id_matches = get_common_id(title_root, "title", in_prefix_list)
                if id_matches is not None : 
                    print(f"ID matches found: \n")
                    for id_num in id_matches : print(f"{id_num} : {snippets[id_num]["title"]}")
                else : print("No matches found")

    elif choice == '3' :
        search_choice = 0
        while search_choice != 'EXIT':
            search_choice = input("\nEnter 1 to search for a prefix, 'EXIT' to exit: ")
            
            if search_choice != '1' :
                print("Please enter valid choice") 

            elif search_choice == 'EXIT' :
                break

            else :
                in_prefix_list = input("Enter your prefix: ").split() 
                id_matches = get_common_id(tag_root, "tags", in_prefix_list)
                if id_matches is not None : 
                    print(f"ID matches found: \n")
                    for id_num in id_matches : print(f"{id_num} : {snippets[id_num]["tags"]}")
                else : print("No matches found")
    
    elif choice == '4' :
        update_confirm = '_'
        while update_confirm != 'EXIT' :
            update_confirm = input("\nTo continue, press 4 again. Else, enter 'EXIT': ")

            if update_confirm != '4' and update_confirm != 'EXIT' :
                print("Please enter valid choice")

            elif update_confirm == 'EXIT' :
                break
            
            else :
                id_num = input("Enter ID of snippet to update: ") 
                while id_num not in snippets :
                    id_num = input("Enter valid ID: ") 
                snippets, title_root, tag_root = update_snippet(id_num, snippets, title_root, tag_root)
                print(f"Snippet with ID: {id_num} is updated")
                break

    elif choice == '5' :
        delete_confirm = '_'
        while delete_confirm != 'EXIT' :
            delete_confirm = input("To continue, press 5 again. Else, enter 'EXIT': ")

            if delete_confirm != '5' and delete_confirm != 'EXIT' :
                print("Please enter valid choice")

            elif delete_confirm == 'EXIT' :
                break
            
            else :
                id_num = input("Enter ID of snippet to delete: ") 
                while id_num not in snippets :
                    id_num = input("Enter valid ID: ") 
                snippets, title_root, tag_root = delete_snippet(id_num, snippets, title_root, tag_root)
                print(f"\nSnippet with ID {id_num} is deleted")
                break

    elif choice == '6' :
        for id_num in snippets :
            print(f"\nContents of snippet with ID {id_num}")
            for key, value in snippets[id_num].items() :
                print(f"{key} : {value}")
            print("\n")
    
    elif choice == '7' :
        search_choice = 0
        while search_choice != 'EXIT':
            search_choice = input("Enter 1 to check for title, 2 to check for tag, EXIT to exit: ")

            if search_choice == 'EXIT' :
                break

            elif search_choice != '1' and search_choice != '2' :
                print("Please enter valid choice") 

            else :
                word = input("Enter word to search: ")
                if search_choice == '1' : root = title_root
                elif search_choice == '2' : root = tag_root
                status_dict = deletion_status_nodes(root, word)
                if status_dict is None : print("Word does not exist")
                else : print(status_dict)
    
    elif choice == '8' :
        print("Pinned snippets: ")
        for id_num in snippets :
            if snippets[id_num]["pin"] :
                print(f"{id_num} : {snippets[id_num]["title"]}")

print("\nThank you for using the snippet search engine!")
