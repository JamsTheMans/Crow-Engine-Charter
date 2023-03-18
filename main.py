# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json
import pyogg

def convert_ogg_to_json(file_path):
    # Open the ogg file
    ogg_file = pyogg.VorbisFile(file_path)

    # Get the song information
    song_info = {}
    song_info["song"] = ogg_file.get_comment("TITLE")
    song_info["bpm"] = float(ogg_file.get_comment("BPM"))
    song_info["needsVoices"] = True  # Set this to True if the song requires vocals
    song_info["player1"] = "bf"  # Set the player1 chart type
    song_info["player2"] = "bf-pixel"  # Set the player2 chart type
    song_info["speed"] = 1.6  # Set the song speed

    # Get the song data
    song_data = []
    for page in ogg_file.pages():
        for packet in page.packets():
            # Process the packet data
            # ...

    # Create the JSON object
    chart = {}
    chart["song"] = song_info
    chart["notes"] = song_data

    # Write the JSON object to a file
    with open("chart.json", "w") as f:
        json.dump(chart, f, indent=4)

