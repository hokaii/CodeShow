import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("刘奶奶找牛奶奶买牛奶，牛奶奶给刘奶奶拿牛奶，刘奶奶说牛奶奶的牛奶不如柳奶奶的牛奶，牛奶奶说柳奶奶的牛奶会流奶，柳奶奶听见了大骂牛奶奶你的才会流奶，柳奶奶和牛奶奶泼牛奶吓坏了刘奶奶，大骂再也不买柳奶奶和牛奶奶的牛奶")