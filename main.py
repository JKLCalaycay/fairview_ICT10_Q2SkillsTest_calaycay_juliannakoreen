from pyscript import display, document

def club_info_stuff(e):  #everything here is basically me assigning their values/corresponding things using dictionaries
    club_pick = int(document.getElementById("club_selected").value)
    club_advisors = { "Marching Band Club": "Emilio Alumno",
                      "Glee Club": "Denver Martin",
                      "Dance Club": "Alfred Cases",
                      "Math Club": "Nicole Gabuya",
                      "Science Club": "Jameelyn Maramag",
                      "Social Studies": "Roberto Lim",
                      "Communication Arts Club": "Yannis Fernandez",
                      "COCC": "JEMIMA DAVID",
                      "Volleyball Varsity": "Adrian Ruiz",
                      "Basketball Varsity": "Adrian Ruiz",}

    club_time = { "Marching Band Club": "Tue & Wed: 3-4:30 PM",
                      "Glee Club": "Mon: 3-5 PM",
                      "Dance Club": "Tue: 3-5 PM",
                      "Math Club": "Mon: 2:30-3 PM",
                      "Science Club": "tUE: 3-4 PM",
                      "Social Studies": "Tue: 3-4 PM",
                      "Communication Arts Club": "Wed & Fri: 3-4 PM",
                      "COCC": "Wed: 2:30-4:30 PM",
                      "Volleyball Varsity": "Wed: 3-4 PM",
                      "Basketball Varsity": "Mon: 3-4 PM",}

    club_place = { "Marching Band Club": "Band Room",
                      "Glee Club": "High School Music Room",
                      "Dance Club": "Teatro Preciosa",
                      "Math Club": "Room 404",
                      "Science Club": "Room 404",
                      "Social Studies": "Room 409",
                      "Communication Arts Club": "406",
                      "COCC": "Quadrangle/Teatro",
                      "Volleyball Varsity": "Quadrangle",
                      "Basketball Varsity": "Quadrangle",}

    club_desc = { "Marching Band Club": "For people with interests in instruments and performing!",
                      "Glee Club": "For people who enjoy singing and performing!",
                      "Dance Club": "For people who love to dance and perform!",
                      "Math Club": "For people who are skilled in Math and want to challenge their knowledge!",
                      "Science Club": "For people who are skilled in Science and want to experiment!",
                      "Social Studies": "For people who like philosophy, history, and politics!",
                      "Communication Arts Club": "For people who like public speaking, literature, and arts",
                      "COCC": "For people who want to be miserable",
                      "Volleyball Varsity": "For skilled volleyball players who want to compete",
                      "Basketball Varsity": "For skilled basketball players who want to compete",}

    club_members = { "Marching Band Club": "18",
                      "Glee Club": "18",
                      "Dance Club": "18",
                      "Math Club": "18",
                      "Science Club": "18",
                      "Social Studies": "18",
                      "Communication Arts Club": "18",
                      "COCC": "18",
                      "Volleyball Varsity": "18",
                      "Basketball Varsity": "18",}

    if club_pick == 1:  #these are my if else statements, so that the person can pic a club and get the right description for it!
        display(f"""Marching Band Club
        Advisor: {club_advisors["Marching Band Club"]} 
        Meeting Time: {club_time["Marching Band Club"]} 
        Location: {club_place["Marching Band Club"]} 
        Description: {club_desc["Marching Band Club"]} 
        Members: {club_members["Marching Band Club"]} 
        Category: Non-Academic""", target="info_output", append=False)

    elif club_pick == 2:
        display(f"""Glee Club
        Advisor: {club_advisors["Glee Club"]} 
        Meeting Time: {club_time["Glee Club"]} 
        Location: {club_place["Glee Club"]} 
        Description: {club_desc["Glee Club"]} 
        Members: {club_members["Glee Club"]} 
        Category: Non-Academic""", target="info_output", append=False)

    elif club_pick == 3:
        display(f"""Dance Club
        Advisor: {club_advisors["Dance Club"]} 
        Meeting Time: {club_time["Dance Club"]} 
        Location: {club_place["Dance Club"]} 
        Description: {club_desc["Dance Club"]} 
        Members: {club_members["Dance Club"]} 
        Category: Non-Academic""", target="info_output", append=False)

    elif club_pick == 4:
        display(f"""Math Club
        Advisor: {club_advisors["Math Club"]} 
        Meeting Time: {club_time["Math Club"]} 
        Location: {club_place["Math Club"]} 
        Description: {club_desc["Math Club"]} 
        Members: {club_members["Math Club"]} 
        Category: Academic""", target="info_output", append=False)

    elif club_pick == 5:
        display(f"""Science Club
        Advisor: {club_advisors["Science Club"]} 
        Meeting Time: {club_time["Science Club"]} 
        Location: {club_place["Science Club"]} 
        Description: {club_desc["Science Club"]} 
        Members: {club_members["Science Club"]} 
        Category: Academic""", target="info_output", append=False)

    elif club_pick == 6:
        display(f"""Social Studies Club
        Advisor: {club_advisors["Social Studies Club"]} 
        Meeting Time: {club_time["Social Studies Club"]} 
        Location: {club_place["Social Studies Club"]} 
        Description: {club_desc["Social Studies Club"]} 
        Members: {club_members["Social Studies Club"]} 
        Category: Academic""", target="info_output", append=False)

    elif club_pick == 7:
        display(f"""Communication Arts Club
        Advisor: {club_advisors["Communication Arts Club"]} 
        Meeting Time: {club_time["Communication Arts Club"]} 
        Location: {club_place["Communication Arts Club"]} 
        Description: {club_desc["Communication Arts Club"]} 
        Members: {club_members["Communication Arts Club"]} 
        Category: Academic""", target="info_output", append=False)

    elif club_pick == 8:
        display(f"""COCC
        Advisor: {club_advisors["COCC"]} 
        Meeting Time: {club_time["COCC"]} 
        Location: {club_place["COCC"]} 
        Description: {club_desc["COCC"]} 
        Members: {club_members["COCC"]} 
        Category: Non-Academic""", target="info_output", append=False)

    elif club_pick == 9:
        display(f"""Volleyball Varsity
        Advisor: {club_advisors["Volleyball Varsity"]} 
        Meeting Time: {club_time["Volleyball Varsity"]} 
        Location: {club_place["Volleyball Varsity"]} 
        Description: {club_desc["Volleyball Varsity"]} 
        Members: {club_members["Volleyball Varsity"]} 
        Category: Academic""", target="info_output", append=False)

    elif club_pick == 10:
        display(f"""Basketball Varsity
        Advisor: {club_advisors["Basketball Varsity"]} 
        Meeting Time: {club_time["Basketball Varsity"]} 
        Location: {club_place["Basketball Varsity"]} 
        Description: {club_desc["Basketball Varsity"]} 
        Members: {club_members["Basketball Varsity"]} 
        Category: Academic""", target="info_output", append=False)

    elif club_pick == 0:
        display(f"""Error, please select a valid club!""", target="info_output", append=False). #this is for if the person doesnt pick a valid club choice

    