from django.shortcuts import render

movies = {
    "Action": [
        {"name": "Avengers: Endgame",
    "rating": "8.4/10",
    "year": "2019",
    "description": "The Avengers unite for one final battle to defeat Thanos and save the universe.",
     "image": "https://originalvintagemovieposters.com/wp-content/uploads/2024/07/AVENGERS-END-GAME-10980-scaled.jpg",
     "trailer":"https://www.youtube.com/watch?v=TcMBFSGVi1c"},
        {"name": "John Wick",
        "rating": "7.4/10",
    "year": "2014",
    "description": "A retired hitman returns to seek revenge after a tragic personal loss.",
     "image": "https://m.media-amazon.com/images/I/81F5PF9oHhL._AC_SL1500_.jpg",
     "trailer":"https://www.youtube.com/watch?v=2AUmvWm5ZDQ"},
        {"name": "Mad Max: Fury Road",
    "rating": "8.1/10",
    "year": "2015",
    "description": "A lone warrior joins a rebel leader in a high-speed escape across a dangerous desert.",
     "image": "https://m.media-amazon.com/images/M/MV5BZDRkODJhOTgtOTc1OC00NTgzLTk4NjItNDgxZDY4YjlmNDY2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
     "trailer":"https://www.youtube.com/watch?v=hEJnMQG9ev8"},
        {"name":"RRR",
        "rating": "7.8/10",
    "year": "2022",
    "description": "Two brave revolutionaries fight against British rule and form a powerful friendship.",
     "image":"https://tse2.mm.bing.net/th/id/OIP.XqdCtJwOm9CBi64FsVybMAHaK-?r=0&cb=thfvnextfalcon2&rs=1&pid=ImgDetMain&o=7&rm=3",
     "trailer":"https://www.youtube.com/watch?v=NgBoMJy386Ms"},
    ],
    "Comedy": [
        {"name": "3 Idiots",
        "rating": "8.4/10",
    "year": "2009",
    "description": "Three engineering students discover the true meaning of success.", 
    "image": "https://m.media-amazon.com/images/M/MV5BNzc4ZWQ3NmYtODE0Ny00YTQ4LTlkZWItNTBkMGQ0MmUwMmJlXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
    "trailer":"https://www.youtube.com/watch?v=K0eDlFX9GMc"},
        {"name": "The Mask",
    "rating": "6.9/10",
    "year": "1994",
    "description": "A magical mask transforms an ordinary man into a hilarious superhero.", 
    "image": "https://tse1.mm.bing.net/th/id/OIP.-EF8fjQqJnYLzM7GogkziwHaLH?r=0&cb=thfvnextfalcon2&rs=1&pid=ImgDetMain&o=7&rm=3",
    "trailer":"https://www.youtube.com/watch?v=hOqVRwGVUkA"},
        {"name": "Home Alone",
        "rating": "7.7/10",
    "year": "1990",
    "description": "A young boy protects his home from two burglars during Christmas.",
     "image": "https://www.vintagemovieposters.co.uk/wp-content/uploads/2024/11/IMG_5793-scaled.jpeg",
     "trailer":"https://www.youtube.com/watch?v=jEDaVHmw7r4"},
    ],
    "Horror": [
        {"name": "The Conjuring",
        "rating": "7.5/10",
    "year": "2013",
    "description": "Paranormal investigators help a family haunted by dark forces.", 
    "image": "https://image.tmdb.org/t/p/original/hofZU4DdPYGwCNNpQeQo8IRU1oW.jpg",
    "trailer":"https://www.youtube.com/watch?v=k10ETZ41q5o"},
        {"name": "Insidious",
         "rating": "6.8/10",
    "year": "2010",
    "description": "A family battles terrifying supernatural spirits to save their son.",
    "image": "https://thfvnext.bing.com/th/id/R.22ef40047a81b05507bd6a82781e2eac?rik=bF%2f9k%2br8b5Az5A&riu=http%3a%2f%2fwww.horror.land%2fwp-content%2fuploads%2f2014%2f06%2fInsidious-Poster-1.jpg&ehk=EbPlVm%2fr%2bjIPa7pnMxfWeHc6v9QuQ%2b0%2bA4mS5SWeQqE%3d&risl=&pid=ImgRaw&r=0",
    "trailer":"https://www.youtube.com/watch?v=zuZnRUcoWos"},
        {"name": "IT",
        "rating": "7.3/10",
    "year": "2017",
    "description": "A group of children confronts an evil shape-shifting clown.",
     "image": "https://i.pinimg.com/originals/42/27/49/422749d0b52a6d652fe34105a00f2b65.jpg","trailer":"https://www.youtube.com/watch?v=xKJmEC5ieOk"},
    ],
    "Romance": [
        {"name": "Titanic",
        "rating": "7.9/10",
    "year": "1997",
    "description": "A timeless love story aboard the ill-fated Titanic.", 
    "image": "https://originalvintagemovieposters.com/wp-content/uploads/2020/02/TITANIC-8567-scaled-1044x1536.jpg",
    "trailer":"https://www.youtube.com/watch?v=kVrqfYjkTdQ"},
        {"name": "The Notebook",
        "rating": "7.8/10",
    "year": "2004",
    "description": "A touching romance that endures through time and hardship.", 
    "image": "https://i.etsystatic.com/55209953/r/il/ca4013/6401823337/il_1140xN.6401823337_8pch.jpg",
    "trailer":"https://www.youtube.com/watch?v=FC6biTjEyZw"},
        {"name": "La La Land",
         "rating": "8.0/10",
    "year": "2016",
    "description": "A musician and an actress chase their dreams while falling in love.",
    "image": "https://cdn.posteritati.com/posters/000/000/068/608/la-la-land-md-web.jpg",
    "trailer":"https://www.youtube.com/watch?v=0pdqf4P9MB8"},
    ],
}

def home(request):
    genre = "Action"      # Default value
    recommendation = movies.get(genre, [])

    if request.method == "POST":
        genre = request.POST.get("genre", "Action")
        recommendation = movies.get(genre, [])

    return render(request, "home.html", {
        "recommendation": recommendation,
        "selected_genre": genre
    })