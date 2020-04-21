Dictionary = {}
string = ""
ObList = []
Save = 0


f = open("tunes.txt")
for line in f:
    if line != '\n':
        string += line
    else:
        if string != "\n":
            ObList = string.split("\n")
            Dictionary[ObList[1]] = ObList
        string = ""


#conjunction junction what's your function?
def Displaysongs():
    artist = []
    for item in Dictionary.values():
        print item

def Displayartists():
    artists = []
    for item in Dictionary:
        if Dictionary[item][0] not in artists:
            artists.append(Dictionary[item][0])
    print artists
    return artists


def Displaygivenartist():
    userartist = raw_input("Please enter artist")
    for item in Dictionary:
        if Dictionary[item][0] == userartist:
            print item

def Displaygenres():
    genres = []
    for item in Dictionary:
        genreonly = Dictionary[item][3]
        if ";" in genreonly:
            genreonly = genreonly.split(";")[0]
        if genreonly in genres:
            genres.append(genreonly)




def Displaygivengenre():
    usergenre = raw_input("Please enter genre")
    for item in Dictionary:
        Dictionarygenre = Dictionary[item][3]
        if ";" in usergenre:
            Dictionarygenre = Dictionarygenre.split(";")[0]
        if Dictionarygenre == usergenre:
            print item



def Displayallplaylists():
    playlists = []
    for item in Dictionary:
        playlistonly = Dictionary[item][3]
        #print playlistonly
        if ";" in playlistonly:
            playlistonly = playlistonly.split(";")[1:]
            for playlist in playlistonly:
                if not playlist in playlists:
                    playlists.append(playlist)
    print playlists


def Displaysonggivenplaylist():
    userplaylist = raw_input("Please enter playlist")
    for item in Dictionary:
        Dictionaryplaylist = Dictionary[item][3]
        if ";" in Dictionaryplaylist:
            Dictionaryplaylist = Dictionaryplaylist.split(";")[1:]
        if userplaylist in Dictionaryplaylist:
            print item


def Recommendsonggivensong():
    usergivensong = raw_input("Please enter a song name")
    for item in Dictionary:
        if usergivensong in Dictionary:
            usergivenartist = Dictionary[usergivensong][0]
            usergivenalbum = Dictionary[usergivensong][2]
            for item in Dictionary:
                if (Dictionary[item][0] == usergivenartist or Dictionary[item][2] == usergivenalbum):
                    print Dictionary[item]
                    print ("\n")



def Recommendartistsgivenartist():
    usergivenartist = raw_input("Please enter a song name")
    for item in Dictionary:
        if Dictionary[item][0] == usergivenartist:
            usergivengenre = Dictionary[item][3].split(";")[0]
    for item in Dictionary:
        if Dictionary[item][0] == usergivenartist == usergivengenre:
            print Dictionary[item]
            print "\n"



def Newsonggiveninfo():

    songname = raw_input("Please enter song name")
    if songname in Dictionary:
        print ("Song already exist in library")
    else:
        artist = raw_input("Enter artist name")
        album = raw_input("Enter album name")
        genre = raw_input("Enter genre")
        playlist = raw_input("Enter playlist")
        if playlist is not "":
            genreplaylist = genre + ";" + playlist
        genreplaylist = genre + ";" + playlist
        Dictionary[songname] = [artist, songname, album, genre,playlist]


def Newplaylist():
    userplaylists = raw_input("Please enter a playlist name")
    for item in Dictionary:
        if userplaylists in Dictionary[item][3]:
            print ("Please try again")
            return
    print ("Please enter song to add to the playlist")
    userexistingsong = raw_input()
    if userexistingsong in Dictionary:
        Dictionary[userexistingsong][3] += (";" + userplaylists)
    else:
        print ("Song does not exist")


def Addsongtoplaylist():
    userplaylists = raw_input("Please enter a playlist name")
    print ("Please enter song to add to the playlist")
    userexistingsong = raw_input()
    if userexistingsong in Dictionary:
        Dictionary[userexistingsong][3] += (";" + userplaylists)

def Save():
    global Save
    f = open("tunes.txt", 'w')
    for item in Dictionary:
        f.write(Dictionary[item][0]+("\n"))
        f.write(Dictionary[item][1]+("\n"))
        f.write(Dictionary[item][2]+("\n"))
        f.write(Dictionary[item][3]+("\n"))
        f.write("\n")
    f.close()
    Save = 1

def Quit():
    pass

while 1:

    print """

    1. Display all songs\n
    2. Display all artist\n
    3. Display all songs with a given artist\n
    4. Display all genres\n
    5. Display all songs with a given genre\n
    6. Display all playlist\n
    7. Display all songs with a given playlist\n
    8. Recommend relevant songs with a given song\n
    9. Recommend relevant artists with a given artist\n
    10. Add a new song with all relevant information given\n
    11. Create a new playlist\n
    12. Add a song to a playlist\n
    13. Save Changes\n
    14. Quit\n"""

    print "please enter your selection via the digit provided at the front of the commands above"

# Calling the functions


    userinput = input()
    if userinput == 1:
        Displaysongs()

    if userinput == 2:
        Displayartists()

    if userinput == 3:
        Displaygivenartist()

    if userinput == 4:
        Displaygenres()

    if userinput == 5:
        Displaygivengenre()

    if userinput == 6:
        Displayallplaylists()

    if userinput == 7:
        Displaysonggivenplaylist()

    if userinput == 8:
        Recommendsonggivensong()

    if userinput == 9:
        Recommendartistsgivenartist()

    if userinput == 10:
        Newsonggiveninfo()

    if userinput == 11:
        Newplaylist()

    if userinput == 12:
        Addsongtoplaylist()

    if userinput == 13:
        #f = open('tunes.txt','w')
        Save()

    if userinput == 14:
        if Save == 1:
            break
        else:
            print ("You haven't saved your changes are you sure you want to quit?")
            userinput = raw_input()
            if userinput in ["Yes","Ye","Y","y","yes","ye"]:
                break
            else:
                pass


