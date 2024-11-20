# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:24:09 2024

@author: Administrator
"""

from googleapiclient.discovery import build
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 根据需求设置代理
# 也可以在运行的终端中设置
# windows cmd中 
# os.environ["http_proxy"]= "http://127.0.0.1:7890"
# os.environ["https_proxy"]= "http://127.0.0.1:7890"
# os.environ["all_proxy"] = "socks5://127.0.0.1:7890

# 替换为你的API密钥
api_key = 'xxx'

# 替换为你想查询的频道ID
# 这个ID用网上给的方法获取的，不是那么直接
channel_id = 'UC_iMvY293APrYBx0CJReIVw'

youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_videos(channel_id):
    # 获取上传的视频播放列表ID
    request = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    )
    response = request.execute()
    
    uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while True:
        # 获取播放列表中的视频
        playlist_request = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        playlist_response = playlist_request.execute()
        
        for item in playlist_response['items']:
            video_title = item['snippet']['title']
            videos.append(video_title)
        
        next_page_token = playlist_response.get('nextPageToken')
        
        if not next_page_token:
            break
    
    return videos

video_titles = get_channel_videos(channel_id)
for title in video_titles:
    print(title)
