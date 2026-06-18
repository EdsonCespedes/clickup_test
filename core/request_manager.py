import time
from typing import Any, Dict, Optional
import httpx
from core.singleton import Singleton
from core.logger import logger

class RequestManager(metaclass=Singleton):
    """
    Administrador central de peticiones HTTPX.
    Mantiene una única sesión, inyecta headers globales y maneja logging estructurado.
    """
    def __init__(self) -> None:
        self._client: Optional[httpx.Client] = None
        self._base_url: str = ""
        self._headers: Dict[str, str] = {}

    def initialize(self, base_url: str, token: str) -> None:
        """Inicializa el cliente HTTPX con configuraciones globales una sola vez."""
        if self._client is None:
            self._base_url = base_url
            self._headers = {
                "Authorization": token,
                "Content-Type": "application/json"
            }
            # Connection pooling optimizado y timeouts rígidos de 15 segundos
            self._client = httpx.Client(
                base_url=self._base_url,
                headers=self._headers,
                timeout=httpx.Timeout(15.0),
                limits=httpx.Limits(max_connections=50, max_keepalive_connections=20)
            )
            logger.info("RequestManager inicializado correctamente con Connection Pooling.")

    def send_request(
        self, 
        method: str, 
        endpoint: str, 
        payload: Optional[Dict[str, Any]] = None, 
        params: Optional[Dict[str, Any]] = None
    ) -> httpx.Response:
        """Envia peticiones HTTP capturando métricas clave de ejecución."""
        if not self._client:
            raise RuntimeError("RequestManager no ha sido inicializado. Llama a .initialize() primero.")
            
        start_time = time.perf_counter()
        logger.info(
            "Enviando Petición API", 
            method=method.upper(), 
            endpoint=endpoint, 
            payload=payload, 
            params=params
        )

        try:
            response = self._client.request(
                method=method.upper(),
                url=endpoint,
                json=payload,
                params=params
            )
            duration = time.perf_counter() - start_time
            
            logger.info(
                "Respuesta Recibida", 
                status_code=response.status_code, 
                duration_seconds=f"{duration:.4f}",
                response_body=response.text[:500] # Limitar salida para evitar logs masivos
            )
            return response
            
        except httpx.RequestError as exc:
            duration = time.perf_counter() - start_time
            logger.error(
                "Fallo crítico en transporte HTTP", 
                method=method, 
                url=exc.request.url, 
                error=str(exc), 
                duration_seconds=f"{duration:.4f}"
            )
            raise exc

    def close(self) -> None:
        """Cierra el pool de conexiones del cliente HTTPX de forma segura."""
        if self._client:
            self._client.close()
            self._client = None
            logger.info("Pool de conexiones de RequestManager cerrado.")