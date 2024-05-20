#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, 'tests')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immunity2.settings')

if __name__ == '__main__':
    import pytest
    from django.core.management import execute_from_command_line

    args = sys.argv
    args.insert(1, 'test')
    if not os.environ.get('SAMPLE_APP', False):
        args.insert(2, 'immunity_notifications')
        app_dir = ['immunity_notifications']
    else:
        args.insert(2, 'immunity2')
        app_dir = ['tests', 'immunity2', 'sample_notifications']
    execute_from_command_line(args)
    sys.exit(pytest.main([os.path.join(*app_dir, 'tests', 'test_websockets.py')]))
