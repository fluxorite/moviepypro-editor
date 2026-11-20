import sys
import os
import base64
import subprocess
import random

try:
    from moviepy import VideoFileClip, AudioFileClip
    import moviepy.video.fx as vfx
except ImportError:
    print("[!] Error: MoviePy library not found. Run: pip install moviepy")
    sys.exit()

def get_num(prompt):
    """Secure numeric input validation"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("   [!] Error: Please enter a valid number!")

def exit_gracefully(sig):
    """Displays a logical message and closes the script"""
    quotes = [
        "Editing is where the movie is finally made.",
        "Your imagination is the limit. See you soon!",
        "Every frame matters. Thanks for using MoviePy Pro.",
        "Creativity takes courage. Keep creating!",
        "Work hard in silence, let your success be your noise."
    ]
    os.system('clear')
    print("\n")
    os.system(f'echo "{random.choice(quotes)}" | boxes -d parchment | toilet --gay -f term')
    os.system(f'echo "DESIGNED BY: {sig}" | boxes -d stone | toilet --gay -f term')
    print("\n   [✔] Script safely closed. Goodbye!\n")
    sys.exit()

def start_editor():
    # Signature "HANSRAJ"
    sig = "HANSRAJ"
    
    # 1. Old School Big ASCII Header
    os.system('clear')
    header_art = r"""
    ##########################################################
    #                                                        #
    #   __  __  ______      _______  ______  _______   __    #
    #  |  \/  |/ __ \ \    / /_   _||  ____||  __ \ \ / /    #
    #  | \  / | |  | \ \  / /  | |  | |__   | |__) \ V /     #
    #  | |\/| | |  | |\ \/ /   | |  |  __|  |  ___/ \ /      #
    #  | |  | | |__| | \  /   _| |_ | |____ | |     | |      #
    #  |_|  |_|\____/   \/   |_____||______||_|     |_|      #
    #                                                        #
    ##########################################################
    """
    os.system(f'echo "{header_art}" | toilet --gay -f term | boxes -d stone')
    os.system(f'echo "ENGINEERED BY:{sig}" | boxes -d parchment | toilet --gay -f term')
    print("\n" + "="*60)

    try:
        # 2. File Selection
        print("\n[?] Input Video File:")
        video_name = input("──> Filename (e.g. video.mp4): ").strip()
        
        if not video_name or not os.path.exists(video_name):
            os.system(f'toilet -f term --gay "FILE NOT FOUND!" | boxes -d dog')
            return

        try:
            clip = VideoFileClip(video_name)
        except Exception as e:
            print(f"   [!] Could not load video: {e}")
            return

        # 3. Comprehensive Feature Menu
        print("\nChoose Operation (Use Arrow Keys):")
        menu = [
            "1. Trim Video", "2. Change Speed", "3. Resize Resolution", 
            "4. Rotate/Flip", "5. Mute Audio", "6. Volume Control", 
            "7. Brightness/Color", "8. Fade In/Out", "9. Reverse Video", 
            "10. Mirror Effect", "11. Crop Video", "12. Invert Color", 
            "13. Extract MP3", "14. Change Background Music", "15. Exit"
        ]
        
        menu_str = " ".join([f'"{i}"' for i in menu])
        choice = subprocess.check_output(f'gum choose {menu_str}', shell=True, text=True).strip()

        if "15" in choice: exit_gracefully(sig)
        
        final_clip = clip

        # --- Features Logic ---
        if "1." in choice:
            final_clip = clip.subclipped(get_num("   Start (sec): "), get_num("   End (sec): "))
        elif "2." in choice:
            final_clip = clip.with_effects([vfx.MultiplySpeed(get_num("   Speed Factor: "))])
        elif "3." in choice:
            final_clip = clip.resized(width=int(get_num("   Target Width: ")))
        elif "4." in choice:
            sub = subprocess.check_output('gum choose "90" "180" "MirrorX" "MirrorY"', shell=True, text=True).strip()
            if "MirrorX" in sub: final_clip = clip.with_effects([vfx.MirrorX()])
            elif "MirrorY" in sub: final_clip = clip.with_effects([vfx.MirrorY()])
            else: final_clip = clip.rotated(int(sub))
        elif "5." in choice:
            final_clip = clip.without_audio()
        elif "6." in choice:
            final_clip = clip.with_effects([vfx.MultiplyVolume(get_num("   Volume Factor: "))])
        elif "7." in choice:
            final_clip = clip.with_effects([vfx.Colorx(get_num("   Brightness Factor: "))])
        elif "8." in choice:
            d = get_num("   Fade Duration: ")
            final_clip = clip.with_effects([vfx.FadeIn(d), vfx.FadeOut(d)])
        elif "9." in choice:
            print("   [!] Processing Reverse Effect...")
            final_clip = clip.with_effects([vfx.TimeMirror()])
        elif "11." in choice:
            w, h = clip.size
            final_clip = clip.cropped(x_center=w/2, y_center=h/2, width=w/2, height=h/2)
        elif "12." in choice:
            final_clip = clip.with_effects([vfx.InvertColors()])
        elif "13." in choice:
            audio_out = os.path.splitext(video_name)[0] + ".mp3"
            clip.audio.write_audiofile(audio_out)
            os.system(f'toilet -f term --gay "AUDIO SAVED" | boxes -d spring')
            return
        elif "14." in choice:
            music_file = input("   Enter MP3 Filename: ").strip()
            if os.path.exists(music_file):
                new_audio = AudioFileClip(music_file).subclipped(0, clip.duration)
                final_clip = clip.with_audio(new_audio)
            else:
                print("   [!] Audio file not found!")

        # 4. Exporting
        output = "edited_" + video_name
        print(f"\n[+] Rendering Video... Please wait.")
        final_clip.write_videofile(output, codec="libx264", audio_codec="aac", threads=4)
        
        os.system(f'toilet -f term --gay "SUCCESSFULLY COMPLETED" | boxes -d spring')

    except KeyboardInterrupt:
        exit_gracefully(sig)
    except Exception as e:
        os.system(f'echo "CRITICAL ERROR: {e}" | boxes -d nuke | toilet --gay -f term')

if __name__ == "__main__":
    start_editor()