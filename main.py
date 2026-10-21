from pyscript import document

# Starting members, grouped by grade.
gr_7 = {'Ashlyn Tambilawan', 'Jayleen Galang', 'Kim Poleen', 'Kevin De Chavez'}
gr_8 = {'Rhon Santos', 'Joshua Evan', 'Marisol Panopi'}
gr_9 = {'Dabe Adante', 'Geoffrey Eman', 'Jeanzel Enriqui'}
gr_10 = {'MJ Nuestro', 'Prince Ulayao', 'Franz Ulayao'}
current_members = gr_7 | gr_8 | gr_9 | gr_10


def new_member(event):
    first_name = document.getElementById("Fname").value.strip()
    last_name = document.getElementById("Lname").value.strip()
    full_name = f"{first_name} {last_name}".strip()

    if full_name:
        current_members.add(full_name)

    document.getElementById("output").innerText = "\n".join(sorted(current_members))



