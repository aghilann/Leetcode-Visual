from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json

views = Blueprint('views', __name__)

def name_only(arr):
    only_name = []
    for word in arr:
        d = word.find("-")
        only_name.append(word[:d])
    return only_name


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    string_manipulation = 0
    arrays = 0
    linked_lists = 0
    stacks = 0
    queues = 0
    hash_tables = 0
    binary_trees = 0
    heaps = 0
    graphs = 0
    dp = 0

    string_manipulation_name = []
    arrays_name = []
    linked_lists_name = []
    stacks_name = []
    queues_name = []
    hash_tables_name = []
    binary_trees_name = []
    heaps_name = []
    graphs_name = []
    dp_name = []
    
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            user = current_user

            # The goal is to determine the number of Points each section has
            # To get the data to user.notes.data

            for note in user.notes:
                info = note.data
                if info[-4:] == "Easy":
                    
                    if "String Manipulation" in info:
                        string_manipulation += 10
                        string_manipulation_name.append(info)
                    
                    elif "Array" in info:
                        arrays += 10
                        arrays_name.append(info)
                    
                    elif "Linked List" in info:
                        linked_lists += 10
                        linked_lists_name.append(info)
                    
                    elif "Stack" in info:
                        stacks += 10
                        stacks_name.append(info)
                    
                    elif "Queue" in info:
                        queues += 10
                        queues_name.append(info)                 
                    
                    elif "Hash Table" in info:
                        hash_tables += 10
                        hash_tables_name.append(info)

                    elif "Binary Tree" in info:
                        binary_trees += 10
                        binary_trees_name.append(info)

                    elif "Heap" in info:
                        heaps += 10
                        heaps_name.append(info) 

                    elif "Graph" in info:
                        graphs += 10
                        graphs_name.append(info)

                    elif "Dynamic Programming" in info or "DP" in info:
                        dp += 10
                        dp_name.append(info)                   
                    else:
                        pass

                elif info[-6:] == "Medium":
                    if "String Manipulation" in info:
                        string_manipulation += 20
                        string_manipulation_name.append(info)

                    elif "Array" in info:
                        arrays += 20
                        arrays_name.append(info)

                    elif "Linked List" in info:
                        linked_lists += 20
                        linked_lists_name.append(info)

                    elif "Stack" in info:
                        stacks += 20
                        stacks_name.append(info)

                    elif "Queue" in info:
                        queues += 20
                        queues_name.append(info)
                    elif "Hash Table" in info:
                        hash_tables += 20
                        hash_tables_name.append(info)
                    elif "Binary Tree" in info:
                        binary_trees += 20
                        binary_trees_name.append(info)
                    elif "Heap" in info:
                        heaps += 20
                        heaps_name.append(info)
                    elif "Graph" in info:
                        graphs += 20
                        graphs_name.append(info)
                    elif "Dynamic Programming" in info or "DP" in info:
                        dp += 20
                        dp_name.append(info)
                    else:
                        pass

                elif info[-4:] == "Hard":
                    
                    if "String Manipulation" in info:
                        string_manipulation += 40
                        string_manipulation_name.append(info)

                    elif "Array" in info:
                        arrays += 40
                        arrays_name.append(info)

                    elif "Linked List" in info:
                        linked_lists += 40
                        linked_lists_name.append(info)

                    elif "Stack" in info:
                        stacks += 40
                        stacks_name.append(info)

                    elif "Queue" in info:
                        queues += 40
                        queues_name.append(info)
                    elif "Hash Table" in info:
                        hash_tables += 40
                        hash_tables_name.append(info)
                    elif "Binary Tree" in info:
                        binary_trees += 40
                        binary_trees_name.append(info)
                    elif "Heap" in info:
                        heaps += 40
                        heaps_name.append(info)
                    elif "Graph" in info:
                        graphs += 40
                        graphs_name.append(info)
                    elif "Dynamic Programming" in info or "DP" in info:
                        dp += 40
                        dp_name.append(info)
                    else:
                        pass

                else:
                    pass
            flash('Note is too short!', category='error')

        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()



            user = current_user

            # The goal is to determine the number of Points each section has
            # To get the data to user.notes.data

            for note in user.notes:
                info = note.data
                if info[-4:] == "Easy":
                    
                    if "String Manipulation" in info:
                        string_manipulation += 10
                        string_manipulation_name.append(info)
                    
                    elif "Array" in info:
                        arrays += 10
                        arrays_name.append(info)
                    
                    elif "Linked List" in info:
                        linked_lists += 10
                        linked_lists_name.append(info)
                    
                    elif "Stack" in info:
                        stacks += 10
                        stacks_name.append(info)
                    
                    elif "Queue" in info:
                        queues += 10
                        queues_name.append(info)                 
                    
                    elif "Hash Table" in info:
                        hash_tables += 10
                        hash_tables_name.append(info)

                    elif "Binary Tree" in info:
                        binary_trees += 10
                        binary_trees_name.append(info)

                    elif "Heap" in info:
                        heaps += 10
                        heaps_name.append(info) 

                    elif "Graph" in info:
                        graphs += 10
                        graphs_name.append(info)

                    elif "Dynamic Programming" in info or "DP" in info:
                        dp += 10
                        dp_name.append(info)                   
                    else:
                        pass

                elif info[-6:] == "Medium":
                    if "String Manipulation" in info:
                        string_manipulation += 20
                        string_manipulation_name.append(info)

                    elif "Array" in info:
                        arrays += 20
                        arrays_name.append(info)

                    elif "Linked List" in info:
                        linked_lists += 20
                        linked_lists_name.append(info)

                    elif "Stack" in info:
                        stacks += 20
                        stacks_name.append(info)

                    elif "Queue" in info:
                        queues += 20
                        queues_name.append(info)
                    elif "Hash Table" in info:
                        hash_tables += 20
                        hash_tables_name.append(info)
                    elif "Binary Tree" in info:
                        binary_trees += 20
                        binary_trees_name.append(info)
                    elif "Heap" in info:
                        heaps += 20
                        heaps_name.append(info)
                    elif "Graph" in info:
                        graphs += 20
                        graphs_name.append(info)
                    elif "Dynamic Programming" in info or "DP" in info:
                        dp += 20
                        dp_name.append(info)
                    else:
                        pass

                elif info[-4:] == "Hard":
                    
                    if "String Manipulation" in info:
                        string_manipulation += 40
                        string_manipulation_name.append(info)

                    elif "Array" in info:
                        arrays += 40
                        arrays_name.append(info)

                    elif "Linked List" in info:
                        linked_lists += 40
                        linked_lists_name.append(info)

                    elif "Stack" in info:
                        stacks += 40
                        stacks_name.append(info)

                    elif "Queue" in info:
                        queues += 40
                        queues_name.append(info)
                    elif "Hash Table" in info:
                        hash_tables += 40
                        hash_tables_name.append(info)
                    elif "Binary Tree" in info:
                        binary_trees += 40
                        binary_trees_name.append(info)
                    elif "Heap" in info:
                        heaps += 40
                        heaps_name.append(info)
                    elif "Graph" in info:
                        graphs += 40
                        graphs_name.append(info)
                    elif "Dynamic Programming" in info or "DP" in info:
                        dp += 40
                        dp_name.append(info)
                    else:
                        pass

                else:
                    pass

            flash('Note added!', category='success')

    only_name_string_manipulation = name_only(string_manipulation_name)
    only_name_arrays = name_only(arrays_name)
    only_name_linked_lists = name_only(linked_lists_name)     
    only_name_stacks = name_only(stacks_name)  
    only_name_queues = name_only(queues_name)  
    only_name_hash_tables = name_only(hash_tables_name)  
    only_name_binary_trees = name_only(binary_trees_name)  
    only_name_heaps = name_only(heaps_name)  
    only_name_graphs = name_only(graphs_name)
    only_name_dp = name_only(dp_name)    
      
    return render_template("home.html", 
                                    user=current_user,
                                    string_manipulation=string_manipulation,
                                    arrays=arrays,
                                    linked_lists=linked_lists,
                                    stacks=stacks,
                                    queues=queues,
                                    hash_tables=hash_tables,
                                    binary_trees=binary_trees,
                                    heaps=heaps,
                                    graphs=graphs,
                                    dp=dp,
                                    string_manipulation_name=string_manipulation_name,
                                    arrays_name=arrays_name,
                                    linked_lists_name=linked_lists_name,
                                    stacks_name=stacks_name,
                                    queues_name=queues_name,
                                    hash_tables_name=hash_tables_name,
                                    binary_trees_name=binary_trees_name,
                                    heaps_name=heaps_name,
                                    graphs_name=graphs_name,
                                    dp_name=dp_name,
                                    only_name_string_manipulation=only_name_string_manipulation,
                                    only_name_arrays=only_name_arrays,
                                    only_name_linked_lists=only_name_linked_lists,
                                    only_name_stacks=only_name_stacks,
                                    only_name_queues=only_name_queues,
                                    only_name_hash_tables=only_name_hash_tables,
                                    only_name_binary_trees=only_name_binary_trees,
                                    only_name_heaps=only_name_heaps,
                                    only_name_graphs=only_name_graphs,
                                    only_name_dp=only_name_dp)



                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                               


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})