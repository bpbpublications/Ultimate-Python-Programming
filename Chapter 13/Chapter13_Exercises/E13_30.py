import os

for name in os.listdir('.'):
    if os.path.isfile(name) and name.endswith('.py'):
        with open(name, 'a') as f:
            f.write('"Copyright 2023 DS. All Rights Reserved."')
