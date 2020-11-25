"""Unit tests for the scene runner class.

Authors: Ayush Baid, Aishwarya, Xialong, Frank Dellaert.
"""
import unittest
from typing import List

import dask
from dask.delayed import Delayed


class SceneRunner:
    """Runs SfM for the scenes."""

    def __init__(self, glob_patterns: List[str]):
        """Initialize from a list of glob patterns (for folders)."""

    def create_computation_graph(self) -> List[Delayed]:
        """Creates the computation graph to run SfM for all scenes.

        Returns:
            Result for each scene as a Delayed element.
        """


class SfmResult:
    """Result after running SFM for a single scene."""


class TestSceneRunner(unittest.TestCase):
    """Unit tests for the scene runner class."""

    def test_everything(self):
        """Test the whole pipeline for GTSFM."""

        # TODO: fix multiple digits
        scene_folders = [
            'oak/*',
            'beech/*',
        ]

        runner = SceneRunner(scene_folders)
        # TODO: test that the number of folders is correct
        graph = runner.create_computation_graph()
        # TODO: what can we test about the graph which indicates correctness

        with dask.config.set(scheduler='single-threaded'):
            results = dask.compute(graph)[0]
            self.assertTrue(isinstance(results, list))
            self.assertEqual(len(results), 6)
            scene_result = results[0]
            self.assertTrue(isinstance(scene_result), SfmResult)

        # TODO: write this conversion
        convert_to_ply_files(results)


if __name__ == "__main__":
    unittest.main()
