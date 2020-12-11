#!/bin/bash
rm -r public/; python roamtowebsite.py && bash -c 'cd public/; python -m http.server'
