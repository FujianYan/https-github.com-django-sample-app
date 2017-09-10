#!/bin/bash

find . -name "*[0-9]_auto_*.py" -type f -delete
find . -name "*[0-9]_initial.py" -type f -delete
psql -h localhost -p 5432 -U postgres -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public; GRANT ALL ON SCHEMA public TO postgres; GRANT ALL ON SCHEMA public TO public;"
