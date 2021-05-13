{
    'name': 'HiCar Blog',
    'version': '1.0',
    'summary': 'HiCar Blog',
    'description': """HiCar Blog""",
    'category': 'Productivity',
    'website': 'https://github.com/buituhoang/hicar_blog',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/blog_youtube_channel.xml',
        'views/blog_youtube.xml',
        'views/blog_news.xml',
        'data/cron.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}