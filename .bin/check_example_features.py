#!/usr/bin/env python3

import pathlib

from ballet.contrib import _collect_contrib_feature_from_module
from ballet.project import Project
from ballet.util.mod import import_module_at_path
from ballet.validation.feature_acceptance import validate_feature_acceptance
from ballet.validation.feature_api import validate_feature_api

root_dir = pathlib.Path(__file__).parent.parent
examples_dir = root_dir.joinpath('examples')
project = Project.from_path(root_dir)
X_df, y_df = project.load_data()

for filename in examples_dir.iterdir():
    if filename.suffix == '.py' and filename.stem != 'feature_starter':
        modname = filename.stem
        mod = import_module_at_path(modname, filename)
        feature = _collect_contrib_feature_from_module(mod)

        if not validate_feature_api(feature, X_df, y_df):
            print(f'feature api not valid for feature in {filename}')

        if not validate_feature_acceptance(feature, X_df, y_df):
            print(f'feature not accepted for feature in {filename}')

print('done')
