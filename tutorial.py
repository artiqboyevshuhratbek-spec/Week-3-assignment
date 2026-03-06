import urllib.request
import json
genre = input("Enter an anime genre or name (e.g., Action, Romance): ").strip()

if genre:
    try:
        url = f"https://api.jikan.moe/v4/anime?q={genre}&limit=10"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        anime_list = []
        for anime in data.get("data", []):
            title = anime.get("title")
            score = anime.get("score", 0)
            year = anime.get("year", "Unknown")
            if score and score >= 7.0:
                anime_list.append({"title": title, "score": score, "year": year})
        anime_list = sorted(anime_list, key=lambda x: x["score"], reverse=True)
        print("\nTop Anime Recommendations:\n")
        for i, anime in enumerate(anime_list[:5], start=1):
            print(f"{i}. {anime['title']} (Score: {anime['score']}, Year: {anime['year']})")
        with open("anime_recommendations.json", "w", encoding="utf-8") as f:
            json.dump(anime_list[:5], f, indent=4, ensure_ascii=False)

    except Exception as e:
        print(f"Error: {e}")
else:
    print("404 Not found.")