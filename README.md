# Subission for 2024's HackYeah hackaton.

## Installing server:
 - Clone the repo with `git clone https://nonelone/hackyeah-2024`
 - Generate secret using python's `secret` library by envoking `secrets.token_hex(32)` and set resulting token as SECRET_KEY variable in `instance/secrets.py`
 - If you have `podman` installed run `run.sh`
 - If you use `docker` instead, change _podman_ to _docker_ in `run.sh`

Website should be avaliable on localhost on port 5000.  
Note that the app works in developement mode and **is not to be used in production**

## Installing exetension
### Google Chrome / Chromium
* Open Chrome.
* In the address bar, type `chrome://extensions/` and hit Enter.
* In the top right corner, toggle the switch for Developer mode to enable it.
* Click the Load unpacked button.
* Select the `extension` folder.

### Mozilla Firefox (currently buggy)
* Open Firefox.
* In the address bar, type `about:debugging#/runtime/this-firefox` and press Enter
* Click the Load Temporary Add-on button.
* Navigate to the folder `extension` containing extension’s files.
* Select the manifest.json file.
