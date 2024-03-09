from pytube import YouTube

def dload(url, output_path):
    try:
        yt = YouTube(url)  

        stream = yt.streams.get_highest_resolution()

        stream.download(output_path=output_path)

        print("Download completed!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    
    video_url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output directory path to save the video: ")

    dload(video_url, output_path)