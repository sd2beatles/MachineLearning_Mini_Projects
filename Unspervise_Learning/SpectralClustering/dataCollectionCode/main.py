
def getArtists():
    #collect artists from the outside source
    kpops=pd.read_csv("/kpop_idols.xls")
    k_artists=kpops[kpops.Group.notnull()].loc[:,"Group"]
    k_artists=list(set([artist.strip()+",KOR" for artist in k_artists]))
    
    artists="/data.csv"
    worlds=pd.read_csv(artists)
    world_artists=worlds.artists.map(lambda x:filtering(x))
    random_numbers=sorted(np.random.choice(1749,500,replace=False))
    world_artists=world_artists[random_numbers].tolist()
    artists=world_artists+k_artists
    return k_artists





def main():
    client_id="replace_me"
    client_secret="replace_me"
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
