"""
The MIT License (MIT)

Copyright (c) 2021 AnonymousDapper
"""

from __future__ import annotations

__all__ = ("TNBException", "HTTPException", "Forbidden", "NotFound", "NetworkServerError")


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp.client_reqrep import ClientResponse


class TNBException(Exception):
    """
    Root exception for aiotnb. Can be used to catch any library errors.
    """

    pass


class HTTPException(TNBException):
    """
    Base exception for any HTTP errors.

     Attributes
     ----------
     response: :class:`aiohttp.ClientResponse`
        The response from the failed request.

    text: :class:`str`
        Error message.

    status: :class:`int`
        HTTP status code of the response.
    """

    def __init__(self, response: ClientResponse, message: str):
        self.response = response
        self.message = message

        super().__init__(f"{response.status} {response.reason}: {message}")


class Forbidden(HTTPException):
    """
    Exception representing an HTTP 403 response.

    :class:`HTTPException` subclass.
    """

    pass


class NotFound(HTTPException):
    """
    Exception representing an HTTP 404 response.

    :class:`HTTPException` subclass.
    """

    pass


class NetworkServerError(HTTPException):
    """
    Exception representing an HTTP 503 response.

    :class:`HTTPException` subclass.
    """

    pass
