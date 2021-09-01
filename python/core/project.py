import yaml

from core.globals import LOCAL_PROJECT_LOCATION


class Project(object):
    DEFAULTS = {
        'apps': [],
        'description': '',
        'background_image': None
    }

    def __init__(self, config_location):
        if not config_location.exists():
            raise ValueError(f'{str(config_location)} does not exist.')
        self.config_location = config_location
        self.config_data = None
        self.load_config()

    @property
    def valid_keys(self):
        return self.DEFAULTS.keys

    @staticmethod
    def create(name, config_path=None):
        """
        Creates a new project profile with default values.

        Args:
            name: str - Desired name of the project.
            config_path: Path - Path to the project yaml file.

        Returns:
            Project: New Project class if successful.

        Raises:
            ValueError: If the project already exists.

        """

        if not config_path:
            project_config_path = LOCAL_PROJECT_LOCATION.joinpath(f'{name}.yml')
        else:
            project_config_path = config_path.joinpath(f'{name}.yml')

        if project_config_path.exists():
            raise ValueError(f'A config for {name} already exists.')

        default_config_values = Project.DEFAULTS
        default_config_values.update({'name': name})
        with open(project_config_path, 'w') as file_handle:
            yaml.dump(default_config_values, file_handle)

        return Project(config_location=project_config_path)

    def load_config(self):
        """Reloads the project values from the config."""
        with open(self.config_location, 'r') as file_handle:
            self.config_data = yaml.load(file_handle, yaml.Loader)
