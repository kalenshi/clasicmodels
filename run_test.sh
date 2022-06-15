#!/bin/bash

result=0
coverage erase
pytest --cov-report term-missing --cov=api/

if [[ $? -ne 0 ]]; then
  result=1
fi

coverage report -m

exit $result
