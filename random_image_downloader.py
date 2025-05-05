import requests
import random, os

UNSPLASH_ACCESS_KEY = "unsplash_access_key"  # Replace with your Unsplash access key
headers = {
    "Accept-Version": "v1",
    "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
}

# Folder where everything will be saved
output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)


keywords = [
    "hydrant", "test", "boat", "company", "CEO", "footballer", "backpack", "radio", "volcano", "mirror",
    "microphone", "dentist", "airplane", "mushroom", "robot", "notebook", "scanner", "stairs", "turtle", "telescope",
    "cathedral", "graffiti", "violin", "pyramid", "jellyfish", "mechanic", "pharmacy", "cowboy", "drone", "tennis",
    "glasses", "teapot", "cactus", "rocket", "apple", "village", "jungle", "astronaut", "actor", "keychain",
    "window", "arcade", "umbrella", "alley", "crane", "toolbox", "sandbox", "zebra", "kangaroo", "snowman",
    "candle", "sandwich", "keyboard", "chessboard", "cashier", "carpenter", "blanket", "printer", "soccer", "hamburger",
    "cookie", "director", "telescope", "hat", "satellite", "glacier", "shopping", "maze", "paintbrush", "rug",
    "hammock", "toothbrush", "mailbox", "supermarket", "sculpture", "escalator", "piggybank", "casino", "screwdriver", "chalkboard",
    "penguin", "elevator", "sunglasses", "magazine", "puzzle", "aquarium", "fortune", "desert", "trophy", "smoothie",
    "giraffe", "pizza", "barber", "magnet", "bagpipe", "lighthouse", "metro", "skateboard", "chewing", "perfume",
    "barcode", "bubble", "icecream", "dinosaur", "cinema", "clown", "castle", "canoe", "funnel", "syrup",
    "hatstand", "cash", "courtroom", "nurse", "storm", "vacuum", "oxygen", "pepper", "soap", "taxi",
    "blender", "trumpet", "pearl", "butcher", "dictionary", "postcard", "scissors", "bakery", "spreadsheet", "saxophone",
    "lab", "smartphone", "headphones", "cabin", "gym", "unicorn", "hammer", "wrench", "record", "curtain",
    "theatre", "ballerina", "iceberg", "coin", "lottery", "goggles", "mosquito", "eraser", "antenna", "tractor",
    "tent", "fence", "cave", "spaceship", "lock", "speaker", "shoe", "swamp", "passport", "flashdrive",
    "surfboard", "stapler", "concert", "puppet", "compass", "farm", "trailer", "fountain", "binoculars", "sushi",
    "glove", "anchor", "barbell", "wheelchair", "museum", "pliers", "stage", "disco", "bridge", "skyscraper",
    "lizard", "tuxedo", "flashlight", "camera", "radiator", "bulldozer", "vending", "lantern", "shovel", "freezer",
    "lipstick", "noodles", "engine", "whistle", "painter", "joystick", "swimmingpool", "zipline", "potion", "steam",
    "crate", "raft", "gallery", "firetruck", "jeep", "chalk", "outlet", "chimney", "palm", "jar",
    "popsicle", "couch", "marshmallow", "sandcastle", "hoodie", "briefcase", "wheelbarrow", "scarf", "torch", "canal",
    "river", "racetrack", "courthouse", "trapdoor", "easel", "bench", "ladder", "sock", "spatula", "globe",
    "quilt", "match", "envelope", "heater", "vase", "tripod", "marshland", "bandage", "cello", "alleyway",
    "hedge", "tablet", "ring", "subway", "rope", "gnome"
]



for i in range(200):
    query = random.choice(keywords)
    try:
        response = requests.get(
            "https://api.unsplash.com/search/photos",
            headers=headers,
            params={
                "query": query,
                "per_page": 1,
                "orientation": "landscape"
            }
        )

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to fetch data for query '{query}'. Status code: {response.status_code}")
            continue

        # Parse the JSON response
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Invalid JSON response for query '{query}'.")
            continue

        # Check if there are results
        if not data.get("results"):
            print(f"No results found for query '{query}'.")
            continue

        # Download the image
        img_url = data["results"][0]["urls"]["regular"]
        img_data = requests.get(img_url).content
        filename = f"unsplash_{i}_{query}.jpg"
        filepath = os.path.join(output_folder, filename)
        with open(filepath, "wb") as f:
            f.write(img_data)
        print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"An error occurred for query '{query}': {e}")