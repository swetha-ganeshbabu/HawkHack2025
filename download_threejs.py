import requests
import os

# Create the js directory if it doesn't exist
os.makedirs('static/js', exist_ok=True)

# URLs for the files
files = {
    'three.min.js': 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js',
    'GLTFLoader.js': 'https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js'
}

# Download each file
for filename, url in files.items():
    print(f'Downloading {filename}...')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'static/js/{filename}', 'wb') as f:
                f.write(response.content)
            print(f'Successfully downloaded {filename}')
        else:
            print(f'Failed to download {filename}, status code: {response.status_code}')
    except Exception as e:
        print(f'Error downloading {filename}: {str(e)}') 