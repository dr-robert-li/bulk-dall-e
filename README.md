# Bulk DALL-E

This Python script allows you to generate images using OpenAI's DALL-E 3 model based on prompts provided in a file. It also expands the prompts using OpenAI's GPT-4 model to create more detailed and creative prompts for image generation.

## Prerequisites

- Python 3.x
- OpenAI Python library (`openai`)
- `requests` library

## Installation

1. Clone the repository or download the script file.

2. Install the required libraries:

```
pip install openai requests
```

## Usage

1. Run the script:

```
python dalle_public.py
```

2. When prompted, provide the following inputs:
- **Prompt file location**: Enter the path to the file containing the prompts, with each prompt on a separate line.
- **OpenAI API Key**: Enter your OpenAI API key.
- **Temperature**: Enter a value between 0.0 and 2.0 to control the randomness of the generated prompts. Higher values (above 0.8) can produce more creative but potentially less coherent results.
- **Additional context**: Provide any additional context or instructions for expanding the prompts, such as "Create an expanded prompt of no more than 40 words to create a high quality and realistic photo".

3. The script will process each prompt from the file, expand it using GPT-4, generate an image using DALL-E 3, and save the image in the `./images/` directory with the prompt as the filename.

4. The script will display the expanded prompt, image URL, and the time taken for each image generation.

## Configuration

- The script uses the `dall-e-3` model for image generation and the `gpt-4` model for prompt expansion. You can modify these model names in the code if needed.
- The generated images have a size of 1792x1024 pixels. You can change the size by modifying the `size` parameter in the `client.images.generate()` function call.
- The script adds a 30-second delay between each image generation to avoid hitting rate limits. You can adjust the delay by modifying the `time.sleep(30)` line at the end of the script.

## Notes

- Make sure you have a valid OpenAI API key and sufficient credits to generate images.
- The script creates an `./images/` directory in the current working directory to store the generated images. Ensure that you have write permissions in the directory.
- The script uses the input prompts as filenames for the generated images. Make sure the prompts are valid filenames and do not contain any invalid characters.

## License

This script is released under the [MIT License](LICENSE).
