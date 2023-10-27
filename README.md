# plugin-downloads
Checking how many times all the zip artifacts were downloaded from a release. 

# Setup
Make sure you have a github API token and the right permissions for that token on your repository and the API

# Install
pipenv install -r requirements.txt

# Run
python downloads.py <path to a release API endpoint>

```
python downloads.py /repos/org/blahblahblah/releases
'https://github.com/org/blahblahblah/releases/download/2.9.0/blahblahblah-2.9.0.0.zip'
23459
'https://github.com/org/blahblahblah/releases/download/2.8.0/blahblahblah-2.8.0.0.zip'
12233
'https://github.com/org/blahblahblah/releases/download/2.6.0/blahblahblah-2.6.0.0.zip'
101234
'https://github.com/org/blahblahblah/releases/download/2.5.0/blahblahblah.zip'
131234
'https://github.com/org/blahblahblah/releases/download/2.4.0/blahblahblah.zip'
362334
```
