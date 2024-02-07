from mega import Mega

email = "nabothdemetrius@gmail.com"
password = "Naboth@04"

mega = Mega()
m = mega.login(email,password)
f = "F:\Software-Project\Sport-Highlights\Audios\\audio.wav"
m.upload(f)
