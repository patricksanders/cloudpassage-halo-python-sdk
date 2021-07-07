"""User Class"""

from cloudpassage.utility import Utility as utility
from cloudpassage.http_helper import HttpHelper
from cloudpassage.halo_endpoint import HaloEndpoint


class User(HaloEndpoint):
    """Initializing the User class:
    Args:
        session (:class:`cloudpassage.HaloSession`) This will define how you
            interact with the Halo API, including proxy settings and API keys
            used for authentication.
    """

    object_name = "user"
    objects_name = "users"
    default_endpoint_version = 2

    def endpoint(self):
        """Return endpoint for API requests."""
        return "/v{}/{}".format(self.endpoint_version, self.objects_name)

    def list_all(self, **kwargs):
        """This method retrieves all Halo users

        Returns:
            list: List of dictionary objects describing Halo users
        """
        endpoint = self.endpoint()
        max_pages = 50
        request = HttpHelper(self.session)
        params = utility.sanitize_url_params(kwargs)
        response = request.get_paginated(
            endpoint, self.objects_name, max_pages, params=params
        )
        return response

    def create(self, username, first_name, last_name, email, access, **kwargs):
        endpoint = self.endpoint()
        user_data = {
            "username": username,
            "firstname": first_name,
            "lastname": last_name,
            "email": email,
            "access": access,
        }
        body = {self.object_name: utility.merge_dicts(user_data, kwargs)}
        request = HttpHelper(self.session)
        response = request.post(endpoint, body)
        return response[self.object_name]["id"]

    def delete(self, object_id):
        """Not implemented for this object."""
        raise NotImplementedError

    def update(self, object_body):
        """Not implemented for this object."""
        raise NotImplementedError

    def describe(self, object_id):
        """Not implemented for this object."""
        raise NotImplementedError
