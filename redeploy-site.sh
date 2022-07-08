#!/bin/bash
#tmux kill-server
cd project-engineers-in-production
git fetch && git reset origin/main --hard
#source python3-virtualenv/bin/activate
#pip install -r requirements.txt
#systemctl daemon-reload
#systemctl restart myportfolio
#tmux new -d "flask run --host=0.0.0.0"

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build