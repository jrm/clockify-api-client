import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class Group(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(Group, self).__init__(api_key=api_key, api_url=api_url)

    def get_groups(self, workspace_id, params=None):
        """Returns list of all group in given workspace.
        :param workspace_id Id of workspace.
        :param params       Request URL query params.
        :return             List of Users dictionary representation.
        """
        try:
            if params:
                params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/user-groups?' + params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/user-groups/'
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e