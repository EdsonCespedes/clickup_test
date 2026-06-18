import time
from typing import Any, Dict, Optional

import httpx

from core.logger import logger
from core.singleton import Singleton


class RequestManager(metaclass=Singleton):
    """
    Centralized HTTPX request manager.

    Maintains a single HTTP session, injects global headers,
    and handles structured logging.
    """

    def __init__(self) -> None:
        self._client: Optional[httpx.Client] = None
        self._base_url: str = ""
        self._headers: Dict[str, str] = {}

    def initialize(self, base_url: str, token: str) -> None:
        """
        Initialize the HTTPX client with global settings only once.
        """
        if self._client is None:
            self._base_url = base_url
            self._headers = {
                "Authorization": token,
                "Content-Type": "application/json",
            }

            # Optimized connection pooling and strict 15-second timeouts
            self._client = httpx.Client(
                base_url=self._base_url,
                headers=self._headers,
                timeout=httpx.Timeout(15.0),
                limits=httpx.Limits(
                    max_connections=50,
                    max_keepalive_connections=20,
                ),
            )

            logger.info(
                "RequestManager initialized successfully with connection pooling."
            )

    def send_request(
        self,
        method: str,
        endpoint: str,
        payload: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        """
        Send HTTP requests while capturing key execution metrics.
        """
        if not self._client:
            raise RuntimeError(
                "RequestManager has not been initialized. "
                "Call .initialize() first."
            )

        start_time = time.perf_counter()

        logger.info(
            "Sending API Request",
            method=method.upper(),
            endpoint=endpoint,
            payload=payload,
            params=params,
        )

        try:
            response = self._client.request(
                method=method.upper(),
                url=endpoint,
                json=payload,
                params=params,
            )

            duration = time.perf_counter() - start_time

            logger.info(
                "Response Received",
                status_code=response.status_code,
                duration_seconds=f"{duration:.4f}",
                response_body=response.text[:500],
            )

            return response

        except httpx.RequestError as exc:
            duration = time.perf_counter() - start_time

            logger.error(
                "Critical HTTP transport failure",
                method=method.upper(),
                url=str(exc.request.url),
                error=str(exc),
                duration_seconds=f"{duration:.4f}",
            )

            raise

    def close(self) -> None:
        """
        Safely close the HTTPX connection pool.
        """
        if self._client:
            self._client.close()
            self._client = None

            logger.info(
                "RequestManager connection pool closed successfully."
            )
