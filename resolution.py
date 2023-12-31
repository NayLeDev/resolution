import random
resolutions = ["Arrêter de fumer", "Boire plus d'eau", "Faire un bilan de santé", "Réduire sa consommation de sucre", "Dormir au moins 8 heures par nuit", "Se brosser les dents deux fois par jour", "Prendre des vitamines", "Se faire vacciner", "Manger plus de fruits et légumes", "Éviter le stress", "Faire du yoga", "Se détendre", "Sourire plus souvent", "Se faire masser", "Prendre soin de sa peau", "Passer plus de temps avec sa famille", "Organiser des réunions de famille", "Appeler ses parents plus souvent", "Rendre visite à ses grands-parents", "Faire des activités avec ses enfants", "Aider ses proches", "Dire je t'aime", "Faire des cadeaux", "Partager ses souvenirs", "Écouter les besoins de sa famille", "Jouer à des jeux vidéos", "Découvrir de nouveaux jeux", "S'améliorer dans ses jeux préférés", "Jouer en ligne avec ses amis", "Participer à des tournois de jeux", "Faire du sport", "Courir", "Nager", "Faire du vélo", "Faire de la randonnée", "Faire de la musculation", "Faire du stretching", "Faire du ski", "Faire du surf", "Faire du tennis", "Faire du football", "Faire du basket", "Faire du golf", "Faire du badminton", "Faire du ping-pong", "Réviser régulièrement ses leçons", "Participer en classe", "Faire ses devoirs avec sérieux", "Demander de l'aide quand on ne comprend pas", "Respecter les règles de vie de l'école", "S'organiser et gérer son temps", "Se fixer des objectifs et les atteindre", "Améliorer son orthographe", "Lire plus de livres", "Apprendre une nouvelle langue", "Découvrir de nouvelles cultures"]

texte = input("Entrez votre ancienne resolution que vous n'avez pas tenu: ")
mots = texte.lower().split()
resolutions_communes = []
for resolution in resolutions:
    for mot in mots:
        if mot in resolution.lower():
            resolutions_communes.append(resolution)
            break
if len(resolutions_communes) == 0:
    print("Aucune résolution n'a été trouvée en commun avec votre ancienne résolution.")
else:
    resolution_choisie = random.choice(resolutions_communes)
    print(f"Voici une résolution pour 2024\n : {resolution_choisie}.")
