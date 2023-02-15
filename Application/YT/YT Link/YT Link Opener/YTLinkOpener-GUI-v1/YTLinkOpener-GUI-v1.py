import pytube
from pytube import YouTube
import PySimpleGUI as sg
import test1
from test1 import Data

class YT_Channel_ID(Data):
    def __init__(self,channel_ID_link):
        super().__init__()
             
        self.channel_ID_link=channel_ID_link
        self.channel=self.GetChannelByChannelID()
        
        self.channel_id=self.GetChannelID()
        self.channel_all_video_urls=self.GetAllYTUrl()
        self.channel_playlists_urls=self.GetPlaylistsUrl()
        self.channel_name=self.GetYTChannelName()
        self.featured_channels_url=self.GetFeatureChannelsUrl()
        self.community_url=self.GetCommunityUrl()
        self.about_url=self.GetAboutUrl()
        self.yt_api_key=self.GetYTAPIKey()
        
        self.initial_data=self.GetInitialData()
        
        print(self.initial_data)
        
        for i in range(0,10,1):
            print("---------------------------------------")
        result=self.GetNestedDatas(self.initial_data)
        print(result)
        for i in range(0,10,1):
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
        val='tags'
        result=self.GetValueByKeyInNestedDatas(self.initial_data,val,containValue=False)
        print(result)
        
    
        
    def GetChannelByChannelID(self):
        return pytube.Channel(self.channel_ID_link)
    
    def GetChannelID(self):
        return self.channel.channel_id
    
    def GetPlaylistsUrl(self):
        return self.channel.playlists_url
    
    def GetAllYTUrl(self):
        return self.channel.video_urls
    
    def GetYTChannelName(self):
        return self.channel.channel_name
    
    def GetFeatureChannelsUrl(self):
        return self.channel.featured_channels_url
    
    def GetCommunityUrl(self):
        return self.channel.community_url
    
    def GetAboutUrl(self):
        return self.channel.about_url
    
    def GetYTAPIKey(self):
        return self.channel.yt_api_key
    
    def GetInitialData(self):
        return self.channel.initial_data
      

class YTLinkOpener(YT_Channel_ID):
    def __init__(self,channel_ID_link):
        super().__init__(channel_ID_link)
        print(self.channel_ID_link)
        
class YT_Channel_ID_Knowledge(YT_Channel_ID):
    def __init__(self,channel_ID_link):
       super().__init__(channel_ID_link)

       
       
    
   
    
tar_url='https://www.youtube.com/channel/UCO-n4ZDDXKPKK29c5eaytpA'
inst=YT_Channel_ID(tar_url)
