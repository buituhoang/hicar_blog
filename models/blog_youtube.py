from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

class BlogYoutube(models.Model):
    _name = 'blog.youtube'
    _rec_name = 'name'

    name = fields.Char(string='Title', required=True)
    url = fields.Char(string='Video URL', required=True)
    thumbnail_link = fields.Char(string='Thumbnail URL')
    description = fields.Text(string='Description')
    likes = fields.Integer(string='Likes')
    views = fields.Integer(string='Views')
    hot = fields.Boolean(string='Hot Video')
    channel = fields.Many2one('blog.youtube.channel', string='Channel')

    

