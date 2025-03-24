curl -X POST -H "Content-Type: application/json" -d '{"name": "Project D", "version": "8djdfjg", "status": "PENDING"}' http://localhost:8001/api/add


curl -X POST -H "Content-Type: application/json" -d '{"name": "Project D", "version": "8djdfjg", "status": "COMPLETED"}' http://localhost:8001/api/update


curl -X POST -H "Content-Type: application/json" -d '{"name": "Project A", "version": "v1.0"}' http://localhost:8001/api/delete
