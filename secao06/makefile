# Subir os serviços
up:
	docker-compose up -d --build

# Derrubar os serviços
down:
	docker-compose down

# Reiniciar os serviços
restart:
	docker-compose down && docker-compose up -d --build

# Limpar volumes e imagens (cuidado: remove dados persistentes)
clean:
	docker-compose down --volumes --remove-orphans
	docker system prune -f --volumes

# Verificar os logs do PostgreSQL
logs:
	docker-compose logs -f postgres
