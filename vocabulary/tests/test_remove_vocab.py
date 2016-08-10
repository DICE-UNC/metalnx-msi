"""
Test Vocabulary removal.
"""

import unittest
import subprocess
import shutil
import os

from tests import VocabConfig


class TestRemoveVocabularyRule(unittest.TestCase, VocabConfig):
    def setUp(self):
        # subprocess.check_call(['su', '-', VOCAB_AUTHOR])
        subprocess.call(['irm', self.VOCAB_NAME])

        if os.path.exists(self.VOCAB_DIR):
            shutil.rmtree(self.VOCAB_DIR)

        VocabConfig.copy_vocab_rules_file_to_etc_irods()

        subprocess.call(self.CREATE_VOCAB_RULE_ARGS)

    def test_remove_vocab(self):
        """
        mlxRemoveVocabulary rule should be executed successfully in iRODS for vocabulary removal.
        """
        self.assertTrue(subprocess.call(['irule', 'mlxRemoveVocabulary', '"null"', '"null"']) == 0)


if __name__ == '__main__':
    unittest.main()