# Dashboard Superset

A customized Apache Superset deployment with Docker support.

## Prerequisites

- Docker
- Docker Compose
- Git

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd dashboard-superset
```

2. Create a `.env` file in the project root with the template provided in `env.sample`.

3. Start the services:
```bash
docker-compose up -d
```

4. Import the database (first time only):
```bash
docker exec -it backend /bin/bash
```
```bash
# Make migration for layers app
python manage.py makemigrations 
# Run migrations: 
python manage.py migrate
# Import data: 
python manage.py import_data
```

5. Admin credentials can be found in the entrypoint.sh file


## Development

To make changes to the configuration:

1. Modify `superset_config.py` as needed
2. Rebuild and restart the superset container


## Troubleshooting

If you encounter any issues:

1. Check the logs:
```bash
docker-compose logs -f
```

2. Restart the services:
```bash
docker-compose restart
```

3. For a clean start:
```bash
docker-compose down -v  # Warning: This will remove all data
docker-compose up -d
```

4. For a clean restart:
```bash
./run_dev.sh # Warning: This will remove all data
```
This needs to be followed by the database import step explained above.
