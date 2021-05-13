from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

class BlogNews(models.Model):
    _name = 'blog.news'
    _rec_name = 'name'

    name = fields.Char(string='Title', required=True)
    url = fields.Char(string='News URL', required=True)
    thumbnail_link = fields.Char(string='Thumbnail URL')
    description = fields.Text(string='Description')
    hot = fields.Boolean(string='Hot News')



