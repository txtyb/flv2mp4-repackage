import os
flv=list()

for filename in os.listdir():
    #i=os.path.splitext(filename)
    if os.path.splitext(filename)[1] not in {'.mp3','.py'}:
        flv.append(filename.replace(' ','\ ').replace('&','\&'))
print(flv)
for i in flv:
    os.system('ffmpeg -i '+i+' '+'-f mp3 -ac 2 -ab 192 '+os.path.splitext(i)[0]+'.mp3')
