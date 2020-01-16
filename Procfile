web: gunicorn pgsearch.app:app --worker-class roll.worker.Worker -b 0.0.0.0:5000
release: python cmd.py load
