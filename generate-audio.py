import pyttsx3

# Path to the .txt file
input_text_file = "sample_text.txt"  # Replace with your .txt file name

# Read text from the file
try:
    with open(input_text_file, "r") as file:
        text = file.read().strip()
except FileNotFoundError:
    print(f"Error: The file {input_text_file} was not found.")
    exit()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Output MP3 file
output_mp3_file = "output_speech.mp3"

# Convert text to speech and save to MP3
engine.save_to_file(text, output_mp3_file)
engine.runAndWait()

print(f"MP3 file has been generated: {output_mp3_file}")
