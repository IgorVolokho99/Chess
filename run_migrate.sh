#!/bin/bash
echo "Start of migrate!"
alembic -c src/configs/alembic.ini upgrade head

sleep 5
echo "End of migrate!"
