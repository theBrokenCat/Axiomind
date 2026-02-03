from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging

# Configuración básica de logs para Sentinel
logger = logging.getLogger("sentinel")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - Sentinel - %(levelname)s - %(message)s'))
logger.addHandler(handler)

class AuthMiddleware(BaseHTTPMiddleware):
    """
    Sentinel: El Portero.
    Interpreta y valida headers de autorización antes de permitir el paso al controlador.
    """
    async def dispatch(self, request: Request, call_next):
        # Permitir paso libre a enpoints públicos como health checks o docs
        if request.url.path in ["/", "/health", "/docs", "/openapi.json"]:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            logger.warning(f"Acceso denegado: Header Authorization faltante. IP: {request.client.host}")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Missing Authorization Header"},
                headers={"WWW-Authenticate": "Bearer"},
            )

        try:
            scheme, token = auth_header.split()
            if scheme.lower() != 'bearer':
                raise ValueError("Invalid scheme")
        except (ValueError, AttributeError):
             logger.warning(f"Acceso denegado: Esquema de autorización inválido. IP: {request.client.host}")
             return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid Authorization Scheme. Expected: Bearer <token>"},
                headers={"WWW-Authenticate": "Bearer"},
            )

        # MOCK Moltbook API Validation
        # En el futuro esto será una llamada HTTP a la API de Moltbook
        if not self._verify_token_mock(token):
            logger.warning(f"Intruso detectado: Token inválido o karma insuficiente. IP: {request.client.host}")
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={"detail": "Access Denied: Invalid Token or Insufficient Karma"},
            )

        response = await call_next(request)
        return response

    def _verify_token_mock(self, token: str) -> bool:
        """
        Simula la validación con Moltbook.
        Token válido: 'axiomind-secret-key'
        """
        # TODO: Reemplazar con llamada real a Moltbook API
        valid_tokens = ["axiomind-secret-key", "valid-user"]
        return token in valid_tokens
