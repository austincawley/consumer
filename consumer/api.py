"""
]
:license: Apache 2.0, see LICENSE for more details.
"""


def consume_url(url):
    """

    :param url:
    :return:
    """
    pass


def consume_swagger(swagger):
    """

    :param swagger:
    :return:
    """
    pass


def consume(url_or_swagger):
    """

    :param url_or_swagger: either a string URL or dict Swagger
    :return:
    """

    if type(url_or_swagger) is str:
        consumeURL(url_or_swagger)
    elif type(url_or_swagger) is dict:
        consumeSwagger(url_or_swagger)
    else:
        raise TypeError('Can only consume a string URL or dict Swagger docs')
