from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from . import youtube

class BlogYoutubeChannel(models.Model):
    _name = 'blog.youtube.channel'
    _rec_name = 'name'

    def crawl_videos(self):
        channels = self.env['blog.youtube.channel'].sudo().search([])
        if channels:
            for channel in channels:
                try:
                    videos = youtube.youtubeCrawler(channel.channel_link)
                    if videos:
                        for video in videos:
                            blog_youtube = self.env['blog.youtube'].sudo().search([('url', 'ilike', video['url'])], limit=1)
                            if blog_youtube:
                                values = {
                                    'name': video['title'],
                                    'thumbnail_link': video['thumbnail'],
                                    'description': video['description'],
                                    'likes': int(video['likes']),
                                    'views': int(video['views']),
                                    'channel': channel.id
                                }
                                blog_youtube.sudo().write(values)
                            else:
                                values = {
                                    'name': video['title'],
                                    'url': video['url'],
                                    'thumbnail_link': video['thumbnail'],
                                    'description': video['description'],
                                    'likes': int(video['likes']),
                                    'views': int(video['views']),
                                    'channel': channel.id
                                }
                                self.env['blog.youtube'].sudo().create(values)
                    else:
                        pass
                except:
                    pass

    name = fields.Char(string='Channel Name', required=True)
    channel_link = fields.Char(string='Channel URL', required=True)
    videos = fields.One2many('blog.youtube', 'channel', string='Videos')



