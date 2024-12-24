import httpx
import json

def send_song_generation_request():
    # Load session cookies
    with open("cookies.json", "r") as f:
        cookies = json.load(f)

    # Create a client with cookies
    client = httpx.Client(cookies={cookie['name']: cookie['value'] for cookie in cookies})

    # Define the endpoint and payload for song creation
    url = "https://www.suno.com/create"
    payload = {
        "Song description": "Friendship Days",  # Example description
        "title": "My Song",                     # Example title
        "genre": "Pop",                         # Example genre
    }

    # Send the POST request to create the song
    response = client.post(url, json=payload, follow_redirects=True)

    # Check and print raw response
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")  # Print raw response body

    if response.status_code == 200:
        try:
            # Try parsing the response as JSON
            json_response = response.json()
            song_uuid = json_response.get("song_uuid")
            if song_uuid:
                print(f"Song created successfully. Song UUID: {song_uuid}")
            else:
                print("Failed to find 'song_uuid' in the response.")
        except json.JSONDecodeError:
            print("Response is not in JSON format.")
    else:
        print(f"Failed to create song. Status code: {response.status_code}")

if __name__ == "__main__":
    send_song_generation_request()
