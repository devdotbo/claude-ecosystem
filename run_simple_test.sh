#!/bin/bash
# Simple script to test Python environment and run simple_test.py

echo "=== Testing Python Environment ==="
echo "Python version:"
python3 --version
echo ""
echo "Python path:"
which python3
echo ""
echo "Current directory:"
pwd
echo ""
echo "=== Running simple_test.py ==="
python3 simple_test.py