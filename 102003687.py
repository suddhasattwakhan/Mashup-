from pytube import YouTube
import pydub 
import urllib.request
import re
import os
import sys
import ffmpeg
from moviepy.editor import concatenate_audioclips,AudioFileClip

def main():
    delete_after_use = True                              
    if len(sys.argv) == 5:
        x = sys.argv[1]
        x = x.replace(' ','') + "songs"
        try:
            n = int(sys.argv[2])                               
            y = int(sys.argv[3])
        except:
            sys.exit("Wrong Parameters entered")
        output_name = sys.argv[4]
    else:
        sys.exit('Wrong number of arguments provided (pls provide 4)')

    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + str(x))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                                                      
    for i in range(n):
        yt = YouTube("https://www.youtube.com/watch?v=" + video_ids[i]) 
        print("Downloading File "+str(i+1)+" .......")
        mp4files = yt.streams.filter(only_audio=True).first().download(filename='tempaudio-'+str(i)+'.mp3')

    print("Files downloaded.")
    print("Getting the mashup ready.....")

    # if os.path.isfile(str(os.getcwd())+"\\tempaudio-0.mp3"):
    #     pydub.AudioSegment.converter = 'C:\\ffmpeg\\bin\\ffmpeg.exe'   
    #     # sound = pydub.AudioSegment.from_mp3("test.mp3")   
    #     # pydub.AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"   
    #     fin_sound = pydub.AudioSegment.from_file(str(os.getcwd())+"\\tempaudio-0.mp3",format='mp3')
    #     # for i in range(1,n):
    #     aud_file =str(os.getcwd())+ "\\tempaudio-"+str(i)+".mp3"
    #     fin_sound = fin_sound.append(pydub.AudioSegment.from_file(aud_file)[0:y*1000],crossfade=1000)
    #     print("hello")
    for i in range(n):
        input_audio_clip=AudioFileClip(f"tempaudio-{i}.mp3")
        final_clip=input_audio_clip.set_duration(y)
        final_clip.to_audiofile(f"{i}-tempaudioNew.mp3")

    def concatenate_audio_moviepy(audio_clip_paths, output_path):
        clips = [AudioFileClip(c) for c in audio_clip_paths]
        final_clip = concatenate_audioclips(clips)
        final_clip.write_audiofile(output_path)

    clips=[f"{i}-tempaudioNew.mp3" for i in range(n)]
    concatenate_audio_moviepy(clips,output_name)
  
# print(fin_sound)
    # try:
    #     fin_sound.export(output_name, format="mp3")
    #     print("File downloaded successfuly. Stored as " + str(output_name))
    # except:
    #     sys.exit("Error saving file. Try differrent file name")
        
    # if delete_after_use:
    #     for i in range(n):
            # os.close("tempaudio-"+str(i)+".mp3")
            # os.close(f"{i}-tempaudioNew.mp3")
            # os.remove("./tempaudio-"+str(i)+".mp3")
            # os.remove(f"{i}-tempaudioNew.mp3")
            # shutil.rmtree("./processed_audios", ignore_errors=False)
            # shutil.rmtree("./raw_audios", ignore_errors=False)

if __name__ == '__main__':
    main()