
def main():
    client_id="161975af6e9c43eaa63de06b51331fdb"
    client_secret="31704bd491a849d6bc440204d21a4776"
    token=getToken(client_id,client_secret)
    artists=getArtists()
    records=[]
    try:
        for artist in artists:
            print("artist,{} begins".format(artist))
            value=artist.split(",")
            name,country=value[0],value[1]
            record=Spotify.getArtistID(name,country,1,token).getAudioFeatures()
            records+=record
    except:
        print("The artist,{},is not currently registered to Spotify".format(artist))
    print("end processing")
    saveFile(records,'json')
    




if __name__=='__main__':

    main()
