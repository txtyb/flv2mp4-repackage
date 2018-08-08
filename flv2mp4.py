import os
flv=list()

for filename in os.listdir():
    #i=os.path.splitext(filename)
    if os.path.splitext(filename)[1] not in {'.mp4','.mp3','.py'}:
        flv.append(filename)
print(flv)
for i in flv:
    os.system('ffmpeg -i '+i+' '+'-acodec copy -vcodec copy '+os.path.splitext(i)+'.mp4')
