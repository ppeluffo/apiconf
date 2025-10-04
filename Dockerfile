FROM spymovil/python38_imagen_base:20250930

# Evitar que Python haga buffering en stdout/stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /apiconf
COPY . .
RUN ls -laR
RUN chmod 777 /apiconf/*

# Asegúrate de que entrypoint sea ejecutable
RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]

EXPOSE 5200