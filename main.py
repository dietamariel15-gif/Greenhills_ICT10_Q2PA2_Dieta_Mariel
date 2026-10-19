# Working with Sets
from pyscript import document, display # importing document and display package


Grade7 = {'Daon Shin', 'Brooke Baguio'}
Grade8 = {'Ariana Grande', 'Taylor Swift'}
Grade9 = {'Olivia Rodrigo', 'Bruno Mars'}
Grade10 = {'Samantha Jose', 'Summer Baguio'}

# Set for newly added members
new_members = set()

# Function to display membership results
def show_members():

    # Union of all sets
    all_members = Grade7 | Grade8 | Grade9 | Grade10 | new_members

    # Clear previous results
    document.getElementById('output').innerHTML = ''

    # Display all members using f-strings
    display(f"All Members: {all_members}", target='output')

    # Display total number of members
    display(f"Total Members: {len(all_members)}", target='output')


# Function to add a new member
def add_member(event):

    # Get the first name and last name
    first_name = document.getElementById('fname').value.strip().lower()
    last_name = document.getElementById('lname').value.strip().lower()

    # Combine the names
    full_name = first_name + ' ' + last_name

    # Add the new member using .add()
    new_members.add(full_name)

    # Update the results
    show_members()


# Display the original members
show_members()

