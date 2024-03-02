import pymongo

client = pymongo.MongoClient("mongourl")
db = client["mydatabase"]
col = db["Videos"]


def addVideo():
    title = input("Enter video title: ")
    url = input("Enter video url: ")
    discriptioon = input("Enter video discription: ")
    col.insert_one({"title": title, "url": url, "discrption": discriptioon})
    print("Video added successfully")

def showVideos():
    for video in col.find():
        print(video)

def updateVideo():
    title = input("Enter video title: ")
    url = input("Enter video url: ")
    discriptioon = input("Enter video discription: ")
    col.update_one({"title": title}, {"$set": {"url": url, "discrption": discriptioon}})
    print("Video updated successfully")

def deleteVideo():
    title = input("Enter video title: ")
    col.delete_one({"title": title})
    print("Video deleted successfully")



def main():
    while True:
        print("\n Youtube manager App")
        print("1. Add Video")
        print("2. Show Videos")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                addVideo()
            case 2:
                showVideos()
            case 3:
                updateVideo()
            case 4:
                deleteVideo()
            case 5:
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
