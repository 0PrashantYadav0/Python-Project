import json
import time

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w+") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, videos in enumerate(videos, start=1):
        print("\n");
        print('*'*70)
        print(f"{index}\n\tVideo name - {videos['name']}\n\tDuration of video - {videos['time']} \n\tYoutube url - {videos['url']}")
        print('*'*70)
        time.sleep(1)

def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    url = input("Enter the url of the video: ")
    videos.append({"name": name, "time": time, "url": url})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1<= index <= len(videos):
        name = input("Enter the name of the video: ")
        time = input("Enter the time of the video: ")
        url = input("Enter the url of the video: ")
        videos[index-1] = {"name": name, "time": time, "url": url}
        save_data_helper(videos)
    else:
        print("Invalid index")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video deleted successfully")
    else:
        print("Invalid index")



def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager :")
        print("1. List all Youtube videos: ")
        print("2. Add a new Youtube video: ")
        print("3. Update a Youtube video: ")
        print("4. Delete a Youtube video: ")
        print("5. Exit from App: ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
