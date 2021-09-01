from shutil import rmtree
from unittest import TestCase

from core.project import Project
from tests import TEMP_TEST_LOCATION


class TestProject(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        TEMP_TEST_LOCATION.mkdir(parents=True, exist_ok=True)

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        rmtree(str(TEMP_TEST_LOCATION), ignore_errors=True)

    def test_create(self):
        project_name = 'test_project'
        temp_project_location = TEMP_TEST_LOCATION.joinpath('project')
        temp_project_location.mkdir(parents=True, exist_ok=True)
        expected_config_location = temp_project_location.joinpath(f'{project_name}.yml')

        project = Project.create(project_name, config_path=temp_project_location)
        self.assertTrue(expected_config_location.exists())
        self.assertDictEqual(Project.DEFAULTS, project.config_data)

        with self.assertRaises(ValueError):
            Project.create(project_name, config_path=temp_project_location)

    def test_update(self):
        self.assetTrue(False)


