import httpx
import json
import time

from SongCreation import send_song_generation_request


def query_song_status(song_uuid):
    # Load session cookies again
    with open("cookies.json", "r") as f:
        cookies = json.load(f)

    # Create a client with cookies
    client = httpx.Client(cookies={cookie['name']: cookie['value'] for cookie in cookies})

    # Define the status endpoint with the song UUID
    url = f"https://www.suno.com/feed/{song_uuid}"

    # Loop to check the status continuously
    while True:
        response = client.get(url)

        if response.status_code == 200:
            status = response.json().get("status")
            print(f"Song status: {status}")

            if status == "completed":  # Example status to break the loop
                print(f"Song generation completed.")
                break
        else:
            print(f"Failed to check song status: {response.text}")
            break

        # Wait for 5 seconds before checking again
        time.sleep(5)

if __name__ == "__main__":
    song_uuid = send_song_generation_request()
    if song_uuid:
        query_song_status(song_uuid)
