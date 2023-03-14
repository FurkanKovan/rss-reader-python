from Channel.channel import Channel

if __name__ == '__main__':
    channel_name = input("Enter a Youtube channel name: ")

    channel = Channel(channel_name)
    channel_url = channel.getUrl()
    channel_id = channel.getChannelId(channel_url)
    channel.getMainPageVideos(channel_url, channel_id)
