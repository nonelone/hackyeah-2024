# Subission for 2024's HackYeah hackaton.

### Instalation:
 - Clone the repo with `git clone https://nonelone/hackyeah-2024`
 - Generate secret using python's `secret` library by envoking `secrets.token_hex(32)` and set resulting token as SECRET_KEY variable in `instance/secrets.py`
 - If you have `podman` installed run `run.sh`
 - If you use `docker` instead, change _podman_ to _docker_ in `run.sh`

Website should be avaliable on localhost on port 5000.  
Note that the app works in developement mode and **is not to be used in production**
